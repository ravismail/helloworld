zero one.

13:59

Yeah, hi. Ramakrishna, can I please come on your video? Yeah. Thank you so much, Ravikant, for joining the call. I'll take a leave now. Sure, yeah, thank you. You may talk.

13:59

You may talk. Hey Rama, you go by Rama, Ramakrishna. Yes, sure. Yeah. Hey Rama, please go ahead and introduce yourself. I carry overall 6.6 years of experience in IT. I started my career in 2019. I worked for four IT companies so far. My last company name is DBS, uh, Development Bank of Singapore. Uh, currently I'm working in banking domain. So coming to my recent project, I worked for IPA, intellectual process automation, where we are mainly dealing with the institutional banking loans. And we are doing all the sales activities for three different countries, Singapore, Hong Kong, and Taiwan. Uh, so each component owning its own uh, workflow, that workflow will be managed by BPMN, business process management, uh, library. And we have like every

14:00

we have like every uh since every country owning its own uh repo, uh there will be so in in that particular country we are using the front end as an angular and back end we are using spring boot uh along with Java 17 and for database we are using my SQL. So coming to uh my roles and responsibility, I worked on few API enhancements and few bug fixes on the front end side. And we have released sprint planning for every two weeks and release activity like on monthly basis. Okay. Yeah. Have you worked on any middleware applications or middleware servers like JBoss, Tomcat? Yeah, JBoss we are currently using, but till then we use JBoss, but recently we have migrated our spring with JBoss to spring boot with Tomcat. Spring boot with Tomcat. So I have

14:01

Tomcat. So, I have then you might have experience like code conversion, right? Uh converting from JBoss to Tomcat, the code compatibility. Yes, yes. So, yeah, can you elaborate more like, you know, what all challenges you faced, what all the steps you uh you changed in the code? So, for uh for this particular migration, we have removed JBoss dependency in our pom.xml and we have since we have embedded Tomcat, right? So, uh just we have removed uh existing uh dependencies and while in our deployment folders also, like we have JBoss related configuration to which server it has to deploy. So, those changes we have done so far during our migration process. Code conversion

14:02

only these two major areas which I have worked so far. Yeah, so basically there will be like, you know, in each Java file, you have all the libraries which are pointing to JBoss. So, how did you manage those the libraries which is specified in the Java classes from Jakarta, sorry, Jakarta to Java X. Java X to Jakarta. Sorry, yeah, vice versa, yeah. So, how did you manage those? You're telling about code changes, right? code change how you fixed it. So, we referred the spring official documentation. Actually, we have migrated in two phases. One is with the spring 2.8 with Java 11 and 2.7 and later we have migrated spring boot 3.5 with Java 17. So, initially we we have upgraded Java first change is we have in pom.xml

14:03

change we have in pom.xml, we have changed the Java version and we made our application up with local configuration setup. So once the application was run, we have done one sanity round of testing. Uh later we slowly change the version, uh sorry, later we change the major spring boot version and uh for the version compatibility, uh I mean the which version we need to add for external dependency which we have which we added in pom.xml. So those we have identified through official documentation and uh so in some scenarios during runtime, uh some dependencies was expected at the runtime. Uh so uh which might not required during our migration part, but at runtime it is expected. That is one scenario which we have observed. And there are few what we can say during this migration we need to take care of the security

14:04

this migration needed to take care of the security vulnerabilities also. So those versions which are expected, I mean which will be coming in in few dependencies as a jar. So that we need to exclude it using exclusion tag. So these are all the steps which we have followed. And and so one another challenge is that for spring 2.7 migration, initially we need to change our application properties to application. files because there is one dependency related to snake. I believe that jar actually snake is a jar which yeah, so that that I mean during runtime actually like once we have fixed it, right? We need to run through Jenkins build and that report once the what we can say report

14:05

Once the, what we can say, dependencies can happen, whatever vulnerability is present in our code fixes, the report will be auto generated. So, one challenge is that even though that snake is not a, it's not identified as a major security vulnerability, but we need to fix the major and minor security vulnerability. So, it was identified as a minor. Uh, sorry, for application properties, which we are getting snake. So, in order to mitigate it, we have changed to application. for for spring boot 2.7 version. And we have fixed it. Once we build our application and once we tested, once the report got generated after running the security vulnerability scans, uh, we, we can able to overcome that particular error. But again, after coming to 3.5, again we, we have rolled back that application to application properties.

14:06

to application. properties. And as you said like major imports, code changes was like we have changed from Java X to Jakarta. Wherever wherever that import statement in whichever classes that change required, we have done it and and so we have migrated Swagger to open AI. Open API, sorry, open API for Spring Boot 3.5. That is also one I mean for Spring Boot 3.5 open API library which which will I mean as per the document that open API considered as a compatible with Spring Boot 3.5. These are all the changes we have done so far in the migration. Yeah, good to know. So,

14:07

Good to know. So, after deploying, like, have you saw any issues, you know, compatibility issues or some other issues that you have been experienced? Yes, yes. We have faced one issue where actually we even that bug was fixed by me. Actually, when when that application we have done testing, one basic sanity testing with end-to-end business scenarios in UAT. Once we got sign off, we have deployed our application to production. And once the production was updated on production date, we like we need to observe the application behavior through logs. One has to monitor. Every application, I mean, ownership is given to a developer. So, the application which I have migrated so far, like, since I am the owner, I have observed the logs where I found one issue where we it's like a fetch by name. We are using

14:08

using uh uh in that application we are using JPQL query in order to fetch. It's like a unlike fetch by ID, it's like a fetch by name. We are fetching one record from a table. Uh so due to this migration, uh like unable to fetch the name actually. The at the point where trying to fetch it, right? We are getting uh so it's long back issue actually, that one particular error. So, but that ID is uh I mean we are able to while debugging the ID which we are passing it from UI, we can able to get it in the back end, but once once DB fetch has done, it's the object is coming as null. So, we we cross checked with other developer also because

14:09

with the other developer also because like we have in my previous company, we have like 10 components, individual micro services. So we have crossed major dependencies, uh major spring boot versions. Uh so everything looks fine, but uh it's like impacting the uh and what we can say, users of an application. Uh so the since in order to avoid the escalations, what we have done is we have approached, we have fixed it by using criteria query. Internally there might be some library change, uh which we have identified, but fixing that particular bug we considered it as taking longer time than actual actual what you can say ETA, estimated time of resolution. So since it exceeds our ETA and impacting our business users, so we

14:10

So, we have followed another approach and that is one bug I have fixed so far. And there is one more issue which once migration was done, even like production is in like we know it's considered as we can get the issues at any point, right? So, after application was stable at production only, but after few days, one one more bug came into existence where we need to exclude one particular jar from a Maven dependency. Due to that the pod actually we have access to Kubernetes also. That pod was keep on restarting.

14:11

was keep on restarting due to image pull back issue and application instance was not stable. Trying to run the application but due to this bug it's not able to, I mean, the application was not running in production due to this minor change. So that also we have excluded. Apart from that, every change we have done so far, we have documented it. So so that it will easier for us to refer to the changes what we have made so far. We have a confluence page. We have multiple developers since working on multiple applications, right? So we have a common confluence page where once application was stable and running in the production, whatever changes the developer has made, we are documenting it. So major business breaking changes we didn't face then.

14:12

business breaking changes we didn't face any because it's already tested in lower environment, but these are the few minor issue, but that impact will be more. But yeah, we have fixed it with these approaches. Okay, okay. And how about the external connectivity like if you are using Kafka connectivity and if you are using database, so you know, if it is in J boss, you are using in standalone.xml file. How did you manage when did you when you converted them to spring boot? So we are using as a like yeah, we are using profiles only in after migrating also we are continuing the same where the we will be storing environment specific configurations in one particular master table and we are fetching it through at the rate value at run time whenever the spring boot application picks up, we will be

14:13

will be will be making call to that particular DB and dynamically appending it using at the rate value annotation. For that we will be using spring profiles in this project, but in my previous project like we are fetching it through vault. Vault which consists of DB username and password. Basic connection details will be fetching it from DB, but if any external connections we required, we are fetching it through vault. Okay. Uh yeah. Let me go through some core Java question. Uh what are the major difference between Java 17 and 21? Uh I majorly worked on 17 only. 21 only few like only few areas I worked like one is virtual thread which we know basically

14:14

Basically, virtual threads are lightweight and easier to manage. Basically, every thread occupies the some memory space, right? So using virtual thread, we can able to manage the task asynchronously and since these are lightweight, there is no restriction that these many threads has to be created and and since these are also lightweight, it won't create button on the CPU, CPU utilization. And this is the one feature I'm aware of. 21, this is only one area I I learned something and 17, we have enhanced switch switch case and so apart from enhanced, I mean, there is an enhancement in the switch case in Java and apart from that,

14:15

That's okay. That's fine. Can you differentiate between hash map and concurrent hash map? And what are the scenario to use? Hash map is a class, like it store the value in key value pair. And basically it derived from an interface called map. It is since hash map follows hashing mechanism, we cannot read the output. The order the sequence of printing the element will be unordered in hash map since it follows hashing mechanism. And hash map basically used in single threaded environment, where if two resources trying to access the same map concurrently, one is doing delete and another was trying to insert at same time. We will be encountering concurrent modification exception. In order to overcome that particular

14:16

overcome that particular issue, uh we can use synchronized map, but like two threads can access it, but one after the other. In that scenario, we can have a thread safe mechanism, but the execution time may take longer because once thread one executed only thread two will trigger. If you if you want to two threads, I mean, want to access the data at same time, we can go for concurrent hash map. Uh and it's from Java.util. Uh and yeah, these are the basic difference between hash map and concurrent hash map. Okay. Difference between runnable and callable. Uh so runnable and callable, runnable having run method, callable having call method. Uh using runnable we can create a thread, using callable, um

14:17

using callable, both are functional interfaces having single abstract method. And using callable, maybe like it's use a callback function, callback mechanism. Okay, can you list what are all the design patterns you have used or you know, you are aware? I work majorly on creation design pattern where singleton design pattern which I'm aware of. And factory design pattern I'm aware of. And prototype I'm not that much, I don't have much hands on. I create design pattern, singleton, prototype, factory, abstract, abstract design pattern.

14:18

abstract design pattern I believe. Uh yeah, some design patterns I have hands on. Majorly like these are the areas which I have worked so far. Okay. So do you know what what is the difference between component, service and repository from spring boot? annotation like uh basically if we declare any these annotation on top of the class, IOC container, main task of IOC container is to create an object and maintain maintain it uh maintain in spring IOC container. And basically it is to uh internally creates an object, but uh if it I mean if you ask me like can we use service in place of

14:19

at the rate service in place of at the rate component in place of at the rate service means actually there is no difference between component and at the rate service for readability purpose they have like created it documentation but there is a difference between at the rate component and at the rate repository.

14:20

what we can say? It's like a wrapping the DB exceptions into uh spring specific uh DB related exceptions. It will wrap it to spring specific exceptions. Uh so readability wise at the rate component at the rate service, functional wise and like we can differ, but functional wise both same, but at the rate component at the rate repository are different actually. At run time, at the rate repository internally work like this and at the rate component, I mean, both creates an object, but internally like if we have any exceptions, it will be wrapped into spring specific exceptions at run time with the repository. Okay. So what is actuator? Actuator is used to check the health point of a spring boot application. So uh it

14:21

Uh in our project, we are using our custom endpoint only, like health/health. We'll be returning a map with like up and down. Key will be up and the value will be true. Okay. Uh in general, we are using our application like that. But in actuator, we can measure the metrics also, like how much memory, uh like how many threads consumed the CPU memory. So those kind of checks can be done through actuator, apart from health checks. And metrics also, we can able to get it through actuator. Uh so health is the one info, a few endpoints exist in the actuator through which we can able to get the metrics of its spring boot application in the production. Okay.

14:22

and how the services communicate like So using one way of communication is through rest. Previously for before spring boot latest spring boot version is four, right? So before four or 3.5 not sure, but we are using rest template. Later client came into picture. using less lines of code, we can able to call to a particular endpoint using client. number of lines to make a

14:23

to make a service request will be reduced with the help of client when compared to rest template. And using now we have web client. So basically these are synchronous approaches where we need to wait till we receive the response. And we have asynchronous way of communicating through event driven approach like Kafka, Kafka RabbitMQ. Basically here we have a producer consumer mechanism where Kafka sits between producer and consumer and there is no communication between producer and consumer. Producer sends message to Kafka and Kafka and consumer receive the message message from Kafka. Here keeper is the we have a concept called keeper and we have a concept called Kafka cluster. In Kafka cluster we have a what we can say? We have brokers in brokers

14:24

brokers. In brokers, we'll be having partitions. So for every specific topic we create, uh that topic having multiple partitions stored as an index in the broker. So each message we try to uh what we can say, uh send as an like whenever producer sends message to Kafka, uh it will be stored in the partitions. Uh and these partitions are pointing to one topic. And we have multiple replication factor. Uh partitions can be stored in multiple broker. So that is the reason why Kafka is more frequently used. Since uh we can have since we have multiple replicas, there is no point of losing the data from the broker. And uh in consumer side, we have multiple consumer. And uh there is a rule in the Apache Kafka stating that we cannot have

14:25

cannot have, uh, I mean, we should have more partitions. I mean, the the size of partitions must be less than or equal to the, uh, the the size of consumers must be less than or equal to the partitions. We, I mean, ideally, if we create more consumers, then if the traffic between the consumer and the Kafka is less, then we may over utilize the resources by making the other consumer sitting ideal. So in order to avoid it, there is a rule, ideal rule that the consumers instances should not be, uh, I mean, should should be less than or equal to the partitions we may we make in the Apache Kafka. And, uh, we have a what we can say, so basically in

14:26

in uh in Kafka cluster we have a leader and followers mechanism. That will be applicable to the broker. Each broker acts as a leader and other brokers acts as a followers. So when whenever there is a failure in the broker one, so based on there is internally one one word we call actually I'm unable to recall. That's okay. So have you like what orchestration tool you are using to host your spring boot app? Orchestration Kubernetes. Kubernetes. Where on prem or where it is? On premises. which it's a banking we are using all premises. Uh my previous project I got some exposure to AKS, Azure Kubernetes service. Okay. And we are basically using Open ID. Open ID is an open open source tool which we can able to using a

14:27

we can able to using a Cube CTL commands, you can connect actually one second, just a minute. Sure. So using Open ID, we are connecting, we have a commands to connect to particular name space. Uh so once we, I mean, once we can able to connect to that name space, we will be having a pod. Uh so we will be having a node and inside node we will be having a pod. So in actually, so that is how we could able to connect to Kubernetes as per my knowledge and in my previous project experience. And uh so in the instances and how many instances we want and those configuration can be done in Kubernetes files. Uh

14:28

files. Uh and we have ingress and egress concept also. Ingress basically used to manage the traffic. I mean manage the traffic from outside of application to the like yeah like that like we we have these files in Kubernetes. Uh and we have readiness and liveness probes also. Uh basically it will check once application was able to deploy successfully without any issues. Once the pod was up and running and once we verify the logs of the pod using the readiness probe basically uh it will and we can specify like after how many milliseconds the application was ready to handle the traffic and uh liveness probe I'm not getting the definition right now. That's okay. So using these these things we have specified.

14:29

things we have specified in our sorry in our Kubernetes files and we have monitoring concept also that few areas are not available. That's okay. And what monitoring tools and logging tools you are using? So as I said like I worked on the consumer side, I don't have experience on the producer in the Kafka. So there is one production issue where we have where the consumer not able to receive the data from the Apache Kafka broker. So whether once producer can send the event whether that event was triggered or not those metrics we have we can able to see it in Apache sorry in the and so yeah in that scenario I have like using this production incident I I exposed to few

14:30

and I I exposed to few areas in Grafana. This is the one use case which I'm aware of. And uh CPU utilization, memory utilization, uh and uh heap space. I think heap space we have one more open tool I believe, but CPU and memory utilization can be measured with the help of Grafana for any specific application. Okay. So do you have any experience working with Splunk for logging? Centralized logging mechanism we are not managing actually. Okay. So yeah, uh you you did you know, developed a code, modified a code and you deployed in dev. In dev everything working fine. And when you when you promoted same thing for production and you all of a sudden you started seeing you know, uh unable to start the application.

14:31

unable to start the application and you reached out to platform apps team or you check the logs and you see OM killed. So how do you debug in such situation? Or honestly deploy our application, we are facing few errors in the logs. So I mean to say like, you know, out of memory error. You are seeing that logs in production but not in dev. So how do you debug it? What do you check first? debug it. So first check is to I obviously to collect the logs and to see where that exception is propagating and once we identified it basically if it is out of memory issue, one one straight straight you can say straight away we can

14:32

can say straight away fix is to increase the heap size, but of course, we cannot increase it because it will be over utilization of resources. So, but I get the based on the traffic before deploying into production, we will be performing the load testing, right? So in that load testing, we will be able to know like how many users that application can able to handle using J meter. So, based on that, we can and based on our business requirement also, we can specify the heap size required to handle this much of traffic. And if it exceeds, we'll be rejecting it. We are not able to handle it. Or we will be asking user that application was busy or try again after some time. So, basically like for any e-commerce application, we will be facing this message sometime or another.

14:33

some time or another. Uh so or any government websites which I faced personally. So uh one thing is increase the heap size. Second approach is to check the what we can say. Uh there is a tool which will analyze the utilization of heap so that garbage collection. Yeah, yeah, garbage collection and there is a tool I which I'm unable to recall which which will visualize the utilization of heap memory which will consume. Uh on both sides like high traffic and low traffic. So based on that we may require to write a logic as I said like something related to memory cleanup or yeah.

14:34

Yeah, based on these parameters, we can either increase or decrease the memory. Sure. Yeah. Okay. Yeah, I think that's all I have. Do you have any questions for me? Uh, can you schedule for one hour? You can ask me if anything left. That's fine. I don't know like why did they schedule this for one hour. 30 minutes. So, may I know the can you feedback or any areas where I'm lacking? No, I think you did really good, but yeah, uh, Deepika will get back to you on the next round. So, there will be another round with the US team. Yeah, just keep watching your email. Okay, sure. Yeah. Thank you. Thanks. Yeah.

14:35

Yeah, there we go. Thank you. Bye.

-----___

two

14:09

while executing if there is any failures in inclined implementation, like one service is down while doing transactions. So that time we have a written one compensated logic. So all the transactions will be

14:10

transactions will be updated to failure state and again once the service is available, we'll call that service and in Apache Kafka while executing any transactions are failed that time we'll keep the transactions in dead letter queue. So we'll we'll proceed we'll process that transactions manually from UI page manually queue. Based on its retention policy time, so that the transactions are available that that. You mentioned the sequential transactions, right? Sequential transactions. So how do you

14:11

So how do you guarantee sequential processing of for each transactions? In Kafka are you are asking? Yeah, in Kafka, yeah. Okay, okay. We have party partitions. So for every transaction there is an offset message where it unique ID. So if and Apache Kafka broker also have leaders and followers are there and all the followers are copied messages from leader. Once that sequential message offset message is executed that transaction, so that offset message is disappeared. So there is no chance for duplicate transactions in Apache Kafka because it is complete

14:12

because it is completely worked on based on its offset message. Okay, okay. Can you explain your experience with Java 8 features? Java 8 features. Okay. In Java 8 features, we have used functional interface and coming to the functional interface, there is only one abstract method. Okay. In the interface. So example for the functional interface are predicate used for takes one input and return one output. Like sorry, takes input and return boolean. Filter is the example for the predicate functional interface and function functional interface is used to takes one input and return one output and example for the function interface is map.

14:13

and consumer consumer functional interface and it takes no input but return value. for each is the example for the consumer functional interface and we have used optional class. Optional class is used to handle null pointer exceptions. Can you explain checked and unchecked exceptions? Exceptions which occurred at compile time, those are called checked exceptions. Exceptions which occurred during runtime, those are called unchecked exceptions. How do you call them in Spring boot? What is the We have a custom class and

14:14

and we have annotated with at the rate rest controller advice on the top of that class and whatever the custom exceptions we want to implement. So all those exceptions we'll have a separate separate methods and in top of it at the rate exception handler annotation will return. Got it. Okay. How does Spring boot auto configuration works? Okay. Internally auto configuration happen using at the rate enable auto configuration. This it is this annotation is already inside in at the rate Spring boot application. At the rate enable auto configuration annotation main purpose is to find the beans based on its

14:15

beans based on its conditional class. So based on the dependencies, it will automatically configure like we'll have a DB connections. So all the database connections will auto configure using at the rate enable auto configuration. Okay. Can you differentiate between Spring MVC and Spring boot? Spring MVC and Spring boot. Okay. In Spring MVC, there is a lot of configuration we have to do like bean configurations and coming to Spring boot, there is auto configuration is available and all the related dependencies is automatically

14:16

is automatically configured and in Spring boot have internally embedded servers like Tomcat. So it is a production ready ready based code compared to Spring MVC. How does you secure rest API calls using JWT? While implementing JWT security, so for every request while adding spring security dependency, so for every request it intercepts user authentication filter intercepts the request. That request is authentication provider calls user

14:17

also user password authentication filter will call. So based on user, it will fetch the details. Once the user is valid, all the credentials are valid, will generate JWT token using JWT utility class and that token will be sent from for every request from header. This token includes expiry time and user, user, user is valid or not. For every for every request it will it will fetch the details from the token. So once the all the details are valid, so based on its roles, whether it is allowed or denied.

14:18

Can you differentiate between authentication and authorization? Authentication means who you are and authorization means what roles you have. In real time example for a Instagram, so for every user have authentication, authorization means some APIs or some kind of things will only able to allow only for particular user like Elon Musk only have how many users are using. All these data are based on his authorization. Can you explain me Spring data JPA?

14:19

Yeah. Okay. Spring data JPA is used for implementing all the database connections and and it have all inbuilt methods. While implementing Spring data JPA, we'll have we'll have one class name like employee repository, which will extend data JPA repository and with the class name and with the primary key, we have to pass in data JPA. So we'll have inbuilt methods like save and data JPA is internally create a connection and executing the query internally and we'll provide output. Data JPA parent class is the credit repository and Spring data JPA have some more features compared to credit repository like sorting.

14:20

repository like sorting techniques and all these things are available in data JPA. Oh yeah, there is an app that is working fine in dev environment. Now you did release to production. So all of a sudden you started seeing out of memory issues. So how do you debug it? How do you what all things you will check for that application? Like you are saying like CPU utilization out of memory, sir. No, I mean, application is crashing because out of memory. Okay. First of all, I will check all the connections are closed correctly or not. First I will check. Okay. What do you check like from what things you check? Like in legacy applications we have JDBC connections like we will open my

14:21

connections like we will open manually. And in finally block we will close DB connection. close. If we suppose miss that finally block, so whenever the transactions, bulk transactions will occur, so multiple connections get opened. So if it is not closed, so the application will remain stuck in that in that stage. Okay. So other than that what you will check? Other than that in Apache Kafka I check partitions. How many number of partitions are available in Apache Kafka and for synchronous transaction thread pool size I will check. So yeah, you found there is an you know memory leak. So how do you fix it?

14:22

Actually for that we are using tool J tool like for to find exact where actually the memory leaks are happening. So suppose the previous version of that code base is working fine and if any new release have that memory leaks in that time we'll check whatever the new changes have done in that latest code base line by line. So we'll go through that and we'll solve we'll try to solve it. Yeah, so yeah, I you found there is a memory leak and how do you you know fix those and retest it like can you give some example?

14:23

Can you give some examples? while using with the try with resource, there is no possibility of memory leaks will happen. And we'll check on for garbage collection, we have a JDK arguments. You mentioned you're working on JBoss, right? Wildfly or EAP? Sorry. You worked on EAP or Wildfly in JBoss? Wildfly. Wildfly 22 version, 31 version also I have worked on it. So yeah, there is like somebody from in a

14:24

Yeah, there is like somebody from in operations team reached out to you, hey, there is your application is, you know, running low with memory. So what things you change in JBoss configuration? Actually, previously we have an issue with bulk transaction, that time we have a JCA connection is automatically down for a particular period of time. So we have we have increased connection pool size on that time. In JBoss for handling bulk transactions. Later the issue is solved after increasing that size. Okay, okay.

14:25

So where did you increase those? Like what configuration changes you made? I don't remember exactly, but I have done some changes in a standalone.xml file. Okay. So what was the reason like migrating monolith apps to microservice? The reason behind it is we want to implement microservice and Java 17. Previously previously legacy application is totally EJB and all the packages are expiring. So in future we'll face some and also security issues also there in legacy application. Okay. And client wants

14:26

And at the end once new technologies we have to implement for that migration project. And also during monolithic application, we have third party connections are there. So if any issue with that with that third party, so entire application is is got stuck. So while implementing microservice application, we have a lot of type of transactions like USSD channel is there and pause channel is there, mobile app channel is there. So we can do recharge from anywhere. Suppose everything is a monolithic application. So once one channel is application is down, so we are unable to do transaction from all the channels. For microservice application, once

14:27

So suppose if there is a pause channel or any other third party is down, so remaining channels will execute parallelly. So that that problem we have solved using micro services implementation. So have you like where these micro services were running in which platform? In local servers only. Local servers means can you elaborate? Local servers means we are not implemented AWS. We have our own local servers. So our is completely production product based. So it only handle all this. Yeah, I know like yeah, it is on your local servers means like where what platform, what orchestration?

14:28

what platform, what orchestration tool you are using to run the microservice? Is it Docker, is it Kubernetes, is it what on VMs? Kubernetes only. Okay. But we have a manual script. So based on that script and they will deploy all those applications and we have a DevOps team for maintenance. So once once we have completed all the implementation in the code base, so we'll push into Git and from Git to Jenkins we have once all the test cases are executed in a QC environment and they will deploy it in IOT, that is client side testing environment. Once everything goes in IOT, we'll deploy in contingency, that is production platform base only.

14:29

production platform base only, but not complete completely production platform base, like production and contingency both are parallelly running, but any new changes, any new clear base will implement, will deploy in contingency. Once everything goes fine in contingency, so all the load is shifted from contingency to production, production environment. During no load time only will deploy in contingency. So do you have any experience in working with Docker files? We have not implemented Docker. Okay. That's all I have. Do you have any questions?

14:30

you have or you have any question for me? Yeah, by the way, I forgot to ask. Have you ever exposed to a co-pilot or any AI tools that you are working on? Still now we have not implemented. Okay. But I'm learning but I'm learning co-pilot. Okay. Okay. So no cloud experience like AWS services. So you know worked on that. I have not worked but I have an idea on AWS. Okay. Okay. Yeah, that's all I have. Do you have any questions for me? Okay. Is it a product based or service based type? No, this is all product based like it's all in house projects. Okay. Like

14:31

Okay, like we are using legacy technology or modern technology? We are using both. We are using monolith apps and we are using, you know, microservices apps as well. And everything runs on JBoss and that will be migrating to Tomcat. From JBoss to Tomcat. Tomcat, yes, yeah. Yes, that's all I have. Yeah, Deepika will get back to you on the next round, okay? Okay, okay, sir. Thank you, sir. Yeah, bye.



----

three

14:00

Hey Deepika, hey Pawan. Yeah, Deepika, you have all the information? Uh, yes, Ravikant. Okay. Thank you. I'll just drop from. Sure. Hey Pawan. Yeah, go ahead and you know, explain yourself.

14:01

yourself. So, I'm Pawan. I worked for three years as a product developer. So there I worked on a product called hiring status. So what what we do is is a talent experience platform. There we offer something called CRM to the client. So CRM is nothing but jobs and candidates data. So we get that jobs and candidates from ATS. So ATS is nothing but work day as well as this. So we we get so for the recruiter, the experience is candidate from review to screening, screening to interview, interview to offer. So when a recruiter is logged in CRM, they have to move the candidate from one stage to another stage. That is the problem I solved. So to move from one stage to another stage, there will be certain conditions.

14:02

there will be certain conditions that's why. So each stage has a end number of steps and each step has multiple conditions. So we get those conditions from Excel file from the client. So I write one micro service in Java which is called rule parser. So what it does is it traverse all those files and produces so the files will have some structure. So based on that structure the the service will parse those files and produces something called DRL file. So we what does this DRL means? So it contains something called step name and what is the when condition. So when this is condition what you have to do. Then then so step name when and then. So this will be produced by this service. then we have something called rule engine service. So the service so the the DRL

14:03

So the the DRL file produced by rule parser is uploaded to S3. Then rule engine service which I also worked on this service. So we what it does is so we get the request from CRM in JSON format. So based on the JSON request contain and ATS. So is nothing but client and ATS. So one client might have multiple files based on the ATS. So we based on the and ATS this service will fetch from S3 that DRL file. So internally we use something called rules. So the conditions we can't hard code in Java applications. So we use we externalize those conditions and use something called rules. So the rules will compile this file and give the next steps of the. So this is overall. Okay. So you are proficient in you know in Java coding.

14:04

in Java coding. Okay. So how about the middleware like what all middleware you are aware? Uh middleware like uh where the application is deployed like Tomcat, Spring boot, uh yes, so it's Spring boot Tomcat. Tomcat. Okay. And how about Jboss? What Jboss you are using? Uh so Jboss is not server. Jboss is Jboss. Jboss. So do you have any experience working on those? Uh I mean in Jboss we use Tomcat server. Okay. Okay. So yeah, let me go through your resume.

14:05

Okay. So yeah, you mentioned you are proficient in coding, right? Let's go in technically. So can you tell me the differences between hash map, concurrent hash map, and hash tables? Yeah, so hash map is is not a type safe. Concurrent hash map is type safe. So, so when we have multithreading environment, we can use concurrent hash maps. And so hash map can accept one null value, one null key and one null value. But concurrent hash map don't accept any null values because in multithreading environment, it causes some ambiguity whether the thread got a thread is updated or not. So and concurrent hash map achieves concurrent

14:06

concurrent hash map achieves the concurrent I mean thread safety using something called internally. So comparing this this is main difference between hash map and concurrent hash map. And coming to hash table. That's okay. That's okay. Explain the final, finally and finalize. Yeah, so final is a keyword which we give for classes or variables to to make them immutable. And finally is a block in a try catch environment where if we want to have some mandatory closings or mandatory things which we want to execute, we use that finally block. And finally, finalize is a GC method which which which runs in background.

14:07

which which runs in background. Okay. And difference between comparable and comparator. Yeah, so comparable is a is used for the own class sorting. Like, so if I have list of movies, movies movies is a class which which contains this comparable which internally uses this comparable interface and it overrides compare method and have some default sorting for the that movie object. So if movie has some name, it will it will override that compare and it will give the order in that manner. So comparator we can use in external classes.

14:08

pattern. Sorry, comparable contains compare to method and comparator contains compare method. So we we can have default sorting using comparator. We can use that comparator in our sorting like connection. sort of list comma that class name what where we implemented the comparator for custom sort. Okay. Uh and do you know any uh root cause for concurrent modification exception? Uh yeah, we have something called fail fail safe iterator and fast fail iterator. So when we when we try to modify the fail fast iterator, we get something called concurrent modification exception.

14:09

Uh, can you explain me what are optional? Uh, so optional is introduced in Java 8. It is primarily for null safe, I mean, to not throw the null pointer exception at runtime. So it has some methods internally, optional. is nullble and and optional. of which gives the optional object, optional. is nullble. I think that method will check whether this object is null or not. And there we can have some chain method. else. throw. If it is null, do something like that. And if you want to use optional, we can mostly can use in the method return type. So we can force the user

14:10

force the user to have that null check mandatory. So when we are declaring method, when we are trying to write a method, instead of writing string, we can we can force the method to return type as optional string. So that users can not get null pointer exception. Okay. So somebody from, you know, operations team reached out to you where you are running application in some middleware or a spring boot. They noticed there is, you know, frequent restart of an application or some exception related to memory. So what you ask to an operators who manages the environment for especially the memory issues? So instead of being checking, what I asked that operation team, yeah, to, you know, to get the more details.

14:11

not to get the more details or to collect some information. So what do you ask them? So first thing is if the application is running for multiple clients, so for our I mean in our environment each application is responsible for multiple clients. So first thing I will ask is is there any new client on board for the for our platform? So that I can assess the so that I can first check that customer load and so we actually pull that jobs data. So first thing I will ask that question. Uh later is there is there any more I mean existing customer data got updated from the client side. Okay. Okay. So other what about the specific memory leaks? What do you ask them?

14:12

memory. Yeah, okay, let me take it in different way. So, so there is explain me about garbage collection and the Java memory areas. Yeah, so garbage collector is responsible for the removal of object removal of objects which are still which are not referenced by any any of the variables in our in our program. There will be few things based on the age of the variable it might be I mean that might be removed in the partial or it might be removed in the full. So how how it is removed in the partial and full based on the so if the object is in young memory, young step

14:13

young memory, young state, that will be removed in partial, I mean, partial GC. If it move to the next day, half memory. Okay. That will be removed in the full GC. So we can check whether if there is frequent full GC, that might cause the high latency. Okay, so, okay, so as an I'm an operator, like I'll share a garbage collection data to you. So how do you, you know, do that? What tools you, you know, use to analyze the GC logs? Uh, we can use some visualization like, I mean, I didn't use before, but there there is something like thread dumps visualization, we can use some visual editor. There is some support for based on that

14:14

based on that visualization report, we can check the which which block of the method and which which line of the thread is causing the memory. Okay. Okay. Let's let's go with spring boot and rest questions. Okay. So can you describe spring boot application architecture? Yeah, so spring boot on a high level. Yeah, so on high level it will have three line three level of architecture. One is presentation level. Second is service level architecture. The third is data access. Okay. Data access. Okay. So first I mean, okay. Presentation we have controller and service will have service classes and data access will have repository to get the data. Okay. Okay. Any difference between comp

14:15

Okay, any difference between component, service and repository? Yeah, component, so component is something to tell this is a beam you have to consider and the service is telling this is a service class and repository means it is a repository which is responsible for connecting into the DB. Do you know anything about auto configurations? which creates beans. I mean spring boot auto configuration. I mean auto configuration means we can use data JPA there we can in application properties we can simply there are spring data database URL DB username password.

14:16

username, password. The JPA will auto configure the DB and connects to the DB. Similarly with the Mongo. Okay. So yeah, so in rest APIs, like how do you handle exceptions, uh, global exceptions? Yeah, we can use something called controller advice. Uh, then we can have some class which which is annotated with controller advice. And and it has some methods which is which we can annotated with exception handler. Uh, it it expects what exception it has to caught. So when an application throws that exception, this method caught that exception and sends the generalized response what we want to send for this exception. So whenever the entire application

14:17

in entire application, how many times you are throwing that exception, this method will throw return the same response. Okay, so what is the difference between transactional and the class class and the method levels? transactional at class and method level. Yeah. Okay, that's okay. That's okay. Have you ever worked on microservice, like these spring boots are part of microservices or what? The one which you worked on. So where did you deploy them? So we we deployed them in the. Okay. I mean, I wrote the docker files for the application to manage that jar to package into a jar and that we deploy into the instance.

14:18

Okay. So when you say Docker file, like, you know, how did you, can you explain me like what images that you are using to run this and what all the tools that needed to run your Java to spring boot app? First we import the Java image from Docker Docker hub. then we can import the Maven to package that application. then we we give some commands to package that application like generally use install, right? So we we give that install command in the Docker too. So that when we run there will be I mean different parts in Docker. There might be multi stage

14:19

multi-stage Docker files where we first build the image in environment, then from runtime we we go to we again pull that image and again compile that image. So there will be generally I'm not getting so this is the high level. If there is single thing we directly build and run. If it is multi-stage Docker file, we first use the environment for building, then there will be operating environment for that. Okay. For microservices, like what are the main challenges you know, yeah, do you uh noticed any challenges? So first thing is we need to maintain each and service each service. So I mean if we compare with monolith if the service is small,

14:20

small, the maintenance will be easier in monolith. One person can do, but for microservice, we need we the operation. I mean, each application we need to deploy and sync and that is one thing. Second thing is if the microservice in monolithic, if the service needs to call another service, it can directly call as a method call. But in microservices, we need to have different communication strategy based on our load and use case. that is so in this communication, there might be some issues like one service got slowed and another service is becoming fast and one service will be restarting. Okay. you know,

14:21

you know, what are the types of service service communications that you come across or can you explain like what are those? So we have mainly synchronous and asynchronous service calls. First synchronous means we call the service and wait until the response is coming. That is one thing. Second thing is asynchronous. We just make a call and forget about the response. And for this, we can also use the Kafka message queues where the service just sends the event what sends the event and the other service just consumes that event and produces it. How do you handle failures for from during service to service communication? We can use something called

14:22

we can use something called circuit breaker pattern. So we can so I would say first we can do for some retry. So if the service is failing after a threshold, I mean three times or something, then we can send the response to the user. This is failed. That is one thing or we can use something called circuit breaker. So in circuit breaker, it is like after some time the service after after reaching a threshold, it it just stops the stops the calling the circuit, I mean that failing service. Instead of calling the service, it it sends the some static response if you have something in the service. That is one thing. Other thing in this circuit breaker itself has something like after some time it will again retry even threshold time.

14:23

if it still is failing again, it still it still avoids calling that call. That is one thing. So the third thing is instead of retrying the every time, we can use some exponential backup. So first call is failed for one second, then you wait for two seconds, then you wait for four seconds and so exponentially you can increase until some level and it will try. So these are three things you can use in communication. Okay. You mentioned that, you know, you are running this on KTS, right? So who's who manage that cluster? That is you or your team or somebody operations team does that? So we have a centralized DevOps team and we have some SRE team. The cluster is maintained by DevOps. Okay.

14:24

So rules and rule engines, right? You mentioned JBoss rules. Can you explain the role of rules in your application? So as I told that we need so the application candidates from one stage to another stage. From review to screen, screen to interview. Each stage will have N number of steps, like 10, 20 steps. And each step will have some condition. So condition in the sense, so we know we primarily deal with the job and candidates data. So the conditions will be like, if the candidate is in America and his age is greater than 18, then only and also if he is immediate joiner, like then only move from the review to the screening stage or screening to the interview stage. So

14:25

into the interview stage. So this is the sample condition I gave. So for each step, we'll have different conditions. So what is so we can't hard code those conditions in our application, right? Because that conditions will grow keep on growing and we need to redeploy the service every time. So and and that is also not feasible. So the what rules is rules expect a file something something in the rules language. So it it follows some it's language called rules language. So it contains the when condition when current state is all these in the DRL file. So how this DRL file contains is so the rule the service contains the pojo. So so the the service so the job object will have all the entries and candidate has all entries in our depend in our service.

14:26

depend in our service. So candidate age. So candidate is a class and age is a field. So this age only this age will be given in the DRL file. So that when rules loads the DRL file into memory, the age is not something it it is not known. I mean data type etc. Because we already gave the age data type in the in our class. We can try for the DRL file the condition. So that so that rules know the data types data types from our Java pojo and conditions from the DRL file. So internally it it will something called retain network. So retain network is something like graph. So well so I would say when candidate is Pawan, age is 18 and country is India. This will be one flow.

14:27

India, this will be one flow. And this is candidate flow and there might be different job object also. So job when the job is in India and job job is external, then only you have to process. So this will go in another flow and both will get matched in that. It has something called I didn't remember the exact name. So there will be something something where it merges and checks, okay, this is qualified. Then then it gives the next step. So this is how it compiles the files very fast. So even the condition got repeated multiple times in our DRL file. So each step might have the condition repeated. So the age condition might be in all steps, but in rules internally, it will build the flow one and and and it what it does is it attaches instead of

14:28

it attaches instead of this come I mean drawing that graph again and again, it reuses that condition so that rules gives the better performance. So this is how rules internally works. So what so we also faced some issue with the rules which caused the memory and CPU intensive and it caused the application to restart. So what is what we so why it caused restart is rules uses something called Kai container all these libraries. So that Kai container contains the knowledge of all this DRL file. So so before I mean before I worked on it, what it enabling is every time the file is getting loaded into memory and every time the file is compiling for every request. So what happening so that compiling and construction of that

14:29

and construction of that return network internally is intensive. And so for for a single ref, loading the file from so if if a ref gets the request 10 times, it has to load the same file 10 times into the memory and has to compile. So what it caused the memory and CPU intensive and application started restarting because now customers keep growing, right? So what I did was I I cached that container. So when the request comes first time, it cached. So I used something called library caffeine like caffeine to caching that container. So from next time onwards, it just uses instead of compiling the file, it just this is the request based on that compiled object. Okay, okay. So for microservice, what type of tests you are doing? I mean, you are written.

14:30

you written. Yeah, I did the unit test. I mean J unit. So I also did the integration test for end to end testing. Okay. So for integration test, I used the test component. Got it. Okay. Okay. So have you done any regression tests or performance tests? For performance test, I did. I mean for this for this caching thing, I did some performance test. Okay. So there I found I figured out the numbers for 295 how much time it is taking. I mean 95 requests are taking. So how did I do was I used some

14:31

it was I used something called Gatling script. So Gatling script contains the hacker model. So in a given minute, so the testing is like so when the method I said right when the first request is come, we are going to catch the object. So from next time onwards, there won't be any CPU spike. But when the pod is restarted, when I deploy something, there will be pump of request will come to the pod, right? So how many so how we try to reduce that pump and make the pod stable is I used the thread pool. So maximum threads I put it as equal to number of CPU cores in our how many cores I'm going to configure in our health check. So because why

14:32

So because why did I make both are equally? Uh because the compilation is CPU intensive. So each core will will be responsible for one request. So I I put the minimum and maximum threads to be equal to the CPU core. So the thread there won't be any high CPU because I limited the thread how many remaining will wait in the queue after the thread pool. So that is one and and using this Gatling script for so in Gatling script I put the number of users to be spin up in first 10 seconds and after 10 second after 10 20 seconds you have to gradually increase the load and to up to 200 users or 300 users for and sit on that user for a few minutes then slowly come out.

14:33

and slowly come out. So Gatling itself will give the one HTML file after executing the all the script. It clearly contains P95, P99, execution time. Got it. Okay. So have you used any AI tools in your organization? Yeah, I worked on the cursor. So we have the that is subscription by the company. So whenever we can so what I did was to make the I mean what to the development in faster in the spring. So first I put the I mean that skills file to the so first one is agent.md file will be there. I mean I configured initially. So that agent.md file will be will contain all the project structure. So what is

14:34

the project structure. So what is module is responsible for. So even tomorrow instead of if I use the cloud, this isn't that will be I mean, we can use directly instead of anything. So that cloud will also cloud model will also get to know the project structure easily in and I used something called skills folder in the project folder itself. So skills folder contain the critical there will be some critical execution. How many threads I'm maintaining, how many how how caching is running, how many cache key, what it is and that is that folder will contain all these critical sections and there is there will be some condition folder which which is like don't push the code to the main branch or don't those will be some things that

14:35

some things that do not do by the cursor. I've put in the cloud and when I'm getting any feature I have to develop, I used to I mean there will be some plan mode in the cursor itself. it will give the I mean when we I will give the specs, it will generate the I mean how how the plan will be going and I will later I execute that I will review that I mean spec driven development, right? So based on the specs it give the design and I review the design and then I will execute it. So that's how I use that. Okay. And what coding standards do you follow? standards like uh uh construct injections, immutable objects, do you follow?

14:36

immutable objects, do you follow those coding standards? Yeah, yeah. Okay. whenever it's possible, we we use the constructor constructor injection only instead of field or setter injection because it will it will be easy for testing in unit test cases. Right. And I also I also avoid using most private and static methods because it is also hard to test using unit testing. Uh that is one thing and we we try to follow the solid principles when I when I designing that classes and methods. Okay. And whenever a new thing is there, we used to maintain 90% of test coverage. Okay. Okay. So have you used any CD tools or currently are you using it? Uh we use the Jenkins as a CD tool.

14:37

Jenkins as a email building and Argo CD to deploy those images in the Okay, you're using Argo CD. Okay. So can you explain me in Argo CD like how do you deploy it? What changes you'll make in order to you know roll the new application or new part. So actually this Jenkins and Argo CD will is maintained by other team. How we we use them? How we use them? We just modify image tags in the helm charts and helm and whatever configuration I mean there will be some application.ml files right we mount them in the volume mount. So we can just go and refresh in Argo CD and it will give the changes. We we just check that changes are correct or not in the UI itself. So if the changes are correct, we

14:38

the changes are correct, we we use the the parts will come up. Okay. So you mentioned developed modular helm chart. Can you explain me what is that? Yeah, to helm chart, I mean, there will be to deploy a service in K. we we we use the helm chart. So helm chart there will be different files in helm charts like for deployment, there will be deployment.ml file and there will be service.ml file. So and there will be values.ml file. So I mean I worked on this when I was I mean helm charts I've written when I joined initially because initially I worked on some legacy product that I moved that is not in K that is in VMs. So I moved them to the helm charts. I mostly written the values.ml.

14:39

mostly written the values. There will be some command to generate the helm charts. It will auto generate all helm charts. I use it to modify those values in the deployment and service. So we follow them. So values file will be like different values file for each environment. Okay. I think that's all I have. Yeah, Deepika will get back to you on the next round. Stay tuned for the response. Do you have any questions for me? any feedback you want to give me? Yeah, we'll provide the feedback. Yeah, definitely. Sure. Thanks. Thanks.

