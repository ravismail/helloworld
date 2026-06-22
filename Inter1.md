Summary
Overview: Java backend interview for Hartford insurance systems
Technical interview covering Java, JBoss, Tomcat, Kubernetes, Docker, Kafka, performance tuning, and migration work
Participants: Ravikant Masanal from Hartford and Akash as the candidate; Deepika briefly joined near the end
Critical outcomes:
Candidate described strong deployment and usage experience in JBoss and Tomcat
Candidate explained performance troubleshooting using logs, autoscaling, indexes, pagination, and Kafka
Candidate rated himself 9/10 on JBoss usage, 7.5/10 on JBoss configuration, and similarly on Tomcat
Candidate background across monolith and microservices
Two active projects: one monolithic application and one microservices platform
Monolith modules included product master, metal master, and global wholesale pricing
Microservices included order processing, invoicing, payment, shipment, and notification services
Role split: 60% individual contributor work and 40% team lead responsibilities
IC work covered feature enhancement, new development, and critical production fixes
Team lead work covered mentoring junior engineers, PR review, approval, deployment support, and build activities
Hartford-related work included the UI call icon application, agency portal, and Connectify integration
Invest project work focused on improving Connectify integration for RTS real-time services and upload transactions
Inputs arrived mostly as XML from teams such as OQP and FastPath
XML was processed with a DOM parser and routed to backend endpoints for BOP, workers compensation, and automobile policies
JBoss deployment, runtime setup, and enterprise edition usage
Current project used JBoss, likely version 6
JBoss stack identified as EE Enterprise edition
Deployment process relied on Jenkins for building release branches
Build produced an artifact version
UDeploy handled deployment to dev, UAT, and production
Production deployments required coordination with the IT team during release windows
Microservices ran in Kubernetes with Docker for containerization
Runtime environment was an open private cloud managed internally by the company
JBoss configuration covered RAM, CPU, heap memory size, and related server parameters
Standalone configuration file was described as the self-contained JBoss server configuration
Domain.xml was described as the deployment/configuration file for deployment setup
Maven pom.xml was used for project dependencies, with libraries downloaded into the M2 folder
Tomcat usage, versions, and migration approach
Apache Tomcat was used as a lightweight web server for JSP and WAR deployment
Some services ran on Tomcat 9 and others on Tomcat 10
Planned target version for migration was Tomcat 11
Tomcat was described as non-Spring in this context, unlike Spring Boot’s embedded server model
Candidate emphasized that embedded servers can be problematic for larger applications
Tomcat migration approach centered on:
Compatibility checks between source and target versions
Validation of support libraries and framework compatibility
Updating configuration files as needed
Testing locally first
Deploying to dev, then QA/UAT
Running QA validation and backend log checks
Scheduling production release after successful verification
JBoss-to-Tomcat migration was not yet done, but candidate outlined a trial approach based on compatibility, dependencies, JDBC/database config, and server-side libraries
JVM tuning, heap and stack concepts, and performance troubleshooting
JVM tuning primarily relied on garbage collector logs
High CPU situations were often mitigated through auto-scaling and horizontal resource expansion
Thread pool configuration was known conceptually, including pool size and maximum pool size, but not personally configured
Connection pool tuning was also understood at a high level, including minimum pool size, maximum pool size, and connection timeout
Performance improvements included:
Query optimization
Database read improvements through indexing
Pagination to avoid loading 100 or 200 records at once
Method rewrites to complete the same operation in less time
Heap memory was described as holding instance variables and being shared across threads
Stack memory was described as holding method calls, being thread-specific, smaller, and faster
Heap was framed as larger and slower to access than stack
Production incidents, DDoS response, and Kafka-based scaling
Recent history included two or three performance incidents in the last six months
One incident involved high database load due to high process/thread counts
Thread dumps and application logs were used to identify resource-heavy operations
Database slowdowns were addressed through indexes and pagination
A DDoS-like event caused the application to be bombarded with large numbers of requests
Auto-scaling was enabled to create more servers and absorb load
A firewall service was added for long-term protection
IPs seen over 30 days or 90 days were whitelisted
Additional IPs during the attack window were blocked
Another slow REST service was moved to Kafka-based processing
The REST path was too slow at about 1–2 seconds per request
Kafka improved throughput by processing in batches instead of real time
Candidate cited Kafka components such as producer, consumer, topic, partitions, broker, and consumer groups
Kafka was presented as better for scalability, durability, retry behavior, fault tolerance, and heavy-load handling
Monolith-to-microservices split and Spring Boot evolution
Not the full monolith, but selected server modules were extracted into microservices when separate scaling was needed
Order processing was cited as a module originally part of the monolith and converted to microservices about two years earlier
Extraction process included analyzing service dependencies, workflow operations, and boundaries for separation
API calls between modules were replaced so each service became individual and independently deployable
Validation included integration, regression, and performance testing before deployment
Monolithic application was built in Spring framework
Microservices were built in Spring Boot
Initial service-to-service communication used RestTemplate with explicit HTTP endpoints and port numbers
The architecture later shifted to Netflix Client and Eureka server
The new approach reduced the need to manually define port numbers and endpoints
Scaling nodes no longer required as much endpoint management
AI tooling, hands-on confidence, and self-ratings
Copilot was integrated about 6 to 9 months earlier
Latest AI tooling mentioned was Opus 4.8, adopted about two weeks before the interview
AI tools were used for:
Log analysis
Code generation from FRDs
Requirement checking
Feature development
Debugging
Unit test generation
TDD support
Self-rating:
JBoss usage and deployment/analysis: 9/10
JBoss configuration: 7.5/10
Tomcat: same rating pattern as JBoss
Action Items
Akash: Share the exact JBoss version in use, since “JBoss 6” was only an estimate
Akash: Confirm the current Tomcat versions for all services and the migration target timeline to Tomcat 11
Akash: Provide a concrete example of a JBoss-to-Tomcat migration plan, including dependency and JDBC compatibility checks
Akash: Detail one production incident end-to-end, including logs reviewed, root cause, and fix applied
Akash: Document the Kafka migration case with before/after latency and throughput numbers
Ravikant / hiring team: Decide whether the candidate’s configuration depth is sufficient for the next round
Your Notes
Click 'Edit Notes' to add your own notes or provide instructions to regenerate summary (e.g. correct spellings to fix transcription errors)
