pip install langchain-community langchain-text-splitters langchain-chroma pypdf sentence-transformers


1:

import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_chroma import Chroma
import chromadb

# --- Configuration ---
PDF_PATH = "your_document.pdf"  # Replace with your PDF file path
CHROMA_HOST = "localhost"
CHROMA_PORT = 8000
COLLECTION_NAME = "my_pdf_collection"
EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2" # A good, small local model

# --- 1. Load the PDF ---
print(f"Loading document: {PDF_PATH}")
loader = PyPDFLoader(PDF_PATH)
documents = loader.load()

# --- 2. Split into Chunks ---
print(f"Splitting {len(documents)} pages into chunks...")
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=100
)
chunks = text_splitter.split_documents(documents)
print(f"Created {len(chunks)} chunks.")

# --- 3. Initialize Embeddings and Chroma Client ---
print("Initializing embeddings and vector store client...")
# Use Sentence Transformers for local embeddings
embedding_function = SentenceTransformerEmbeddings(model_name=EMBEDDING_MODEL_NAME)

# Connect to the ChromaDB running in Docker
client = chromadb.HttpClient(host=CHROMA_HOST, port=CHROMA_PORT)

# --- 4. Embed and Store in ChromaDB ---
# This step creates the collection if it doesn't exist and adds the documents
vectordb = Chroma.from_documents(
    documents=chunks,
    embedding=embedding_function,
    collection_name=COLLECTION_NAME,
    client=client
)
print(f"Successfully added {len(chunks)} chunks to ChromaDB collection '{COLLECTION_NAME}'.")

# Example retrieval test (optional)
query = "What is the main topic of the first section?"
retriever = vectordb.as_retriever(search_kwargs={"k": 3})
retrieved_docs = retriever.invoke(query)
print("\n--- Retrieval Test ---")
print(f"Query: {query}")
print(f"Retrieved Documents: {len(retrieved_docs)}")
# print(retrieved_docs[0].page_content[:200] + "...")




pip install langchain-community langchain

2.
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_chroma import Chroma
from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA
import chromadb

# --- Configuration (must match ingest script) ---
CHROMA_HOST = "localhost"
CHROMA_PORT = 8000
COLLECTION_NAME = "my_pdf_collection"
EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2"
OLLAMA_MODEL = "llama2" # Ensure this model is pulled in Ollama (e.g., 'ollama pull llama2')

# --- 1. Connect to ChromaDB and Retriever ---
embedding_function = SentenceTransformerEmbeddings(model_name=EMBEDDING_MODEL_NAME)
client = chromadb.HttpClient(host=CHROMA_HOST, port=CHROMA_PORT)

# Load the persisted vector store
vectordb = Chroma(
    client=client,
    collection_name=COLLECTION_NAME,
    embedding_function=embedding_function
)
retriever = vectordb.as_retriever(search_kwargs={"k": 4}) # Retrieve top 4 chunks

# --- 2. Initialize Local LLM (Ollama) ---
llm = Ollama(model=OLLAMA_MODEL)

# --- 3. Create the RAG Chain (RetrievalQA) ---
# The chain automatically takes the query, retrieves documents, and formats the prompt for the LLM
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",  # 'stuff' puts all retrieved docs into the prompt
    retriever=retriever,
    return_source_documents=True
)

# --- 4. Query the LLM ---
user_query = "What is the key takeaway about data privacy mentioned in the document?"
print(f"Querying LLM: {user_query}")

result = qa_chain.invoke({"query": user_query})

print("\n--- LLM Answer ---")
print(result['result'])

print("\n--- Source Documents ---")
for doc in result['source_documents']:
    # The source metadata often includes the page number
    print(f"- Source: {doc.metadata.get('source')} (Page: {doc.metadata.get('page')})")








import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

# ----------------------------------------------------
# CONFIGURATION
# ----------------------------------------------------
PDF_PATH = "sample.pdf"  # path to your PDF
CHROMA_HOST = "http://localhost:8000"  # ChromaDB in Docker
MODEL_RUNNER_URL = "http://localhost:12434/engines/llama.cpp/v1"  # embedding model runner
COLLECTION_NAME = "pdf_collection"

# ----------------------------------------------------
# STEP 1: Load PDF
# ----------------------------------------------------
print("📄 Loading PDF document...")
loader = PyPDFLoader(PDF_PATH)
documents = loader.load()

# ----------------------------------------------------
# STEP 2: Add metadata for traceability
# ----------------------------------------------------
print("🧾 Adding metadata to documents...")
for i, doc in enumerate(documents):
    doc.metadata["source"] = os.path.basename(PDF_PATH)
    doc.metadata["page_number"] = i + 1

# ----------------------------------------------------
# STEP 3: Split text into manageable chunks
# ----------------------------------------------------
print("✂️ Splitting document into chunks...")
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=150,
    length_function=len
)
texts = text_splitter.split_documents(documents)

# Add unique IDs or chunk numbers
for i, doc in enumerate(texts):
    doc.metadata["chunk_id"] = i + 1

print(f"✅ Total chunks created: {len(texts)}")

# ----------------------------------------------------
# STEP 4: Initialize embeddings from Docker model runner
# ----------------------------------------------------
print("🧠 Initializing embedding model...")
embeddings = OpenAIEmbeddings(
    model="ai/nomic-embed-text-v1.5:latest",
    openai_api_key="none",  # local runner doesn’t need auth
    openai_api_base=MODEL_RUNNER_URL
)

# ----------------------------------------------------
# STEP 5: Connect to ChromaDB running on Docker
# ----------------------------------------------------
print("🗄️ Connecting to ChromaDB Docker service...")
vectorstore = Chroma.from_documents(
    documents=texts,
    embedding=embeddings,
    collection_name=COLLECTION_NAME,
    client_settings={
        "chroma_api_impl": "rest",
        "chroma_server_host": "localhost",
        "chroma_server_http_port": "8000",
    }
)

print("✅ Successfully embedded PDF and stored in ChromaDB with metadata!")

# ----------------------------------------------------
# STEP 6: Example semantic search
# ----------------------------------------------------
query = "Summarize the key topic discussed in this PDF."
print(f"\n🔍 Running similarity search for: '{query}'")
results = vectorstore.similarity_search(query, k=2)

for i, doc in enumerate(results, 1):
    print(f"\nResult {i}:")
    print(f"📄 Source: {doc.metadata.get('source', 'N/A')}")
    print(f"📄 Page: {doc.metadata.get('page_number', 'N/A')}")
    print(f"🔢 Chunk ID: {doc.metadata.get('chunk_id', 'N/A')}")
    print("Content:")
    print(doc.page_content[:500], "...")
