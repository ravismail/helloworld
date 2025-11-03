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
