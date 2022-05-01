# **Hadoop or Spark?**
### **Table of content**
1. Introduction to Big Data
   - Big Data Customers
2. Distributed Computing
   - Distributed Computing Architecutre
3. Hadoop
    - Hadoop Architecture
    - Hadoop Eco System
4. Apache
    - Apache Architecture
    - Apache Eco System
5. Hadoop VS Spark
    - Analysis based on Resoucre Utilization
    - Analysis based on Application Scope
6. Conclusion
7. References
    
## **Introduction to Big Data**
<p style='text-align: justify;' > Big Data is data of very big size which cannot be processed with usual tools. And to process such data we need to have distributed architecture. This data could be structured or unstructured. Generally, we classify the problems related to the handling of data into three buckets.

1.	Volume- How we would store huge amount of data, Example, Meta handling more than 500TB data per day.
2.	Velocity- Handling so many requests per second. The number of problems received by Facebook or Google per second. 
3.	Variety- If problem at hand is complex or data, we are dealing with are processing is complex. </p>
<br>

<p style='text-align: justify;'> 
The year 2002 is called the beginning of the digital age. Why so? The answer is twofold: Devices, Connectivity On one hand, the devices became cheaper, faster and smaller. Smart Phone is a great example. On another, the connectivity improved. We have wifi, 4G, Bluetooth, NFC etc. This led to a lot of very useful applications such as a very vibrant world wide web, social networks, and Internet of things leading to huge data generation. </p>



**Who are big data customers?**
<p style='text-align: justify;'> 
1.	Government: They have huge data about the citizens. Applications: Fraud Detection and Cyber Security.<br>
2.	Telecom: Uses big data to understand why customers are leaving and how that can be prevented (customer churn)<br>
3.	Healthcare: Healthcare inherently has humongous data and complex problems to solve. </p>

<p style='text-align: justify;'>
After learing about big data, we will get a vivid picture of the need for clusters of machines (distributed systems), and appreciate the use of this architecture in solving critical problems associated with storing and processing humungous data. </p>

## **Distributed Computing**
<p style='text-align: justify;'> 
Distributed computer system consists of multiple software components that are on multiple computers but run as a single system. The computers can be physically closed and are connected by a local network or they can be placed in geographically different places by wide area network. Distributed computing consists of possible configurations like mainframes, personal computers, workstations, minicomputers and so on.

***“In other words, distributed computing uses distributed systems to solve problems”*** </p>
<br>
<br>
![](https://stringfixer.com/files/205061474.jpg)
Source: https://stringfixer.com/files/205061474.jpg

**Distributed System Architecture**
<p style='text-align: justify;'> 

- Distributed systems must have a network that connects all components (machines, hardware, or software) together so they can transfer messages to communicate with each other.
- That network could be connected with an IP address or use cables or even on a circuit board. The messages passed between machines contain forms of data that the systems want to share like databases, objects, and files. 
- The way the messages are communicated reliably whether it’s sent, received, acknowledged or how a node retries on failure is an important feature of a distributed system.

Hadoop and Spark, both developed by the Apache Software Foundation, are widely used open-source frameworks for big data architectures. Each framework contains an extensive ecosystem of open-source technologies that prepare, process, manage and analyse big data sets. 

With each year, there seem to be more and more distributed systems on the market to manage data volume, variety, and velocity. Among these systems, Hadoop and Spark are the two that continue to get the most mindshare. But how can you decide which is right for you? </p>

## **Hadoop**
<p style='text-align: justify;'> 
The Apache Hadoop software library is a framework that allows for the distributed processing. Hadoop manages to process and store vast amounts of data by using interconnected affordable commodity hardware. Hundreds or even thousands of low-cost dedicated servers working together to store and process data within a single ecosystem. Apache Hadoop was released was on April 1, 2006. </p>

**Architecture**
<p style='text-align: justify;'> 
The Hadoop Distributed File System (HDFS), YARN, and MapReduce are at the heart of that ecosystem. HDFS is a set of protocols used to store large data sets, while MapReduce efficiently processes the incoming data. </p>
<br>

![](https://media.springernature.com/full/springer-static/image/art%3A10.1186%2Fs40537-020-00388-5/MediaObjects/40537_2020_388_Fig1_HTML.png?as=webp)
Source:http://hadoop.apache.org/.

**Hadoop Ecosytem**
<p style='text-align: justify;'> 
Hadoop supports advanced analytics for stored data (e.g., predictive analysis, data mining, machine learning (ML), etc.). It enables big data analytics processing tasks to be split into smaller tasks. The small tasks are performed in parallel by using an algorithm (e.g., MapReduce), and are then distributed across a Hadoop cluster (i.e., nodes that perform parallel computations on big data sets). 
Hadoop has become a very popular platform in the IT industry and academia for its ability to handle large amounts of data, along with extensive processing and analysis facilities. Different users produce these large datasets, and most of data are unstructured, increasing the requirements for memory and I/O. Besides, the advent of many new applications and technologies brought much larger volumes of complex data, including social media, e.g., Meta, Twitter, YouTube, online shopping, machine data, system data, and browsing history. This massive amount of digital data becomes a challenging task for the management to store, process, and analyse.

The conventional database management tools are unable to handle this type of data. Big data technologies, tools, and procedures allowed organizations to capture, process speedily, and analyse large quantities of data and extract appropriate information at a reasonable cost. </p>

## **Spark**
<p style='text-align: justify;'> 
Apache Spark is an open-source cluster computing framework which is setting the world of Big Data on fire. Sparks performance is up to 100 times faster in memory and 10 times faster on disk when compared to Hadoop. Apache Spark was inistally released on 2016, May 26. It is designed to cover a wide range of workloads such as batch applications, iterative algorithms, interactive queries, and streaming.
Apache Spark has a well-defined layered architecture where all the spark components and layers are loosely coupled. This architecture is further integrated with various extensions and libraries. Apache Spark Architecture is based on two main abstractions.

1. Resilient Distributed Dataset(RDD)
2. Directed Acyclic Graph(DAG)
</p>

![](https://media.springernature.com/full/springer-static/image/art%3A10.1186%2Fs40537-020-00388-5/MediaObjects/40537_2020_388_Fig2_HTML.png?as=webp)
Source: http://hadoop.apache.org/.

**Spark Ecosystem**
<p style='text-align: justify;'> 
Apache Spark, the largest open-source project in data processing, is the only processing framework that combines data and artificial intelligence (AI). This enables users to perform large-scale data transformations and analyses, and then run state-of-the-art machine learning (ML) and AI algorithms.
</p>

## **Hadoop VS Spark Analysis based on Resource Utilization and Application Scope**
### Analysis based on Resource Utilization
**1. Performance**

| Parameter | Hadoop(MapReduce) | Spark |
|:--------------|:-------------------|-------|
|Data Processing| Persist backs to the disk after a map or reduce action| In-memory|
|Memory| Kill process as soon as the  job is done and release the memory| A lot of memory needed|
|Running| Processes run alongside other service too| Processes run alone|
|Iterative Computation| It was designed for one-pass ETL-like jobs| Give the best result in itervative  the same data many times|
<p style='text-align: justify;'> 
When data fits in the memory (buffer memory) the performance of the Spark is better. When the data does not fit in the memory, performance of Hadoop MapReduce would be excellent.
</p>

**2. Ease of Use**


|Parameter|Hadoop(Map Reduce) | Spark|
|:--------|:------------------|------|
|APIs Support| Yes(only Java)| Yes(Java, Scala, Python)|
|Language Support| Java Only| Java, Scala, Python|
|SQL Compatibility| Yes (Hive)| Yes (Spark SQL)|
|Programming model| Withing MapReduce programming model| Within user defined function|
|Inactive| No (command line)| Yes|
<p style='text-align: justify;'> 
Spark is easier in context of programming and it's interactive mode gives the smooth drive to the user as compared to Hadoop. 
</p>

**3. Cost**

|Parameter| Hadoop (Map Reduce) | Spark|
|:--------|:--------------------|------|
|Open Source|Yes|Yes|
|Run-on-clo-ud| Yes| Yes|
|Cores| 4| 8-16|
|Memory|24BG| 8GB|
|Disk| 4-6 one TB disks| 4-8|
<p style='text-align: justify;'> 
Spark is more cost-effective than Hadoop MapReduce according to benchmarks. </p>

**4. Compatibility**

|Parameter| Hadoop (Map Reduce) | Spark|
|:--------|:--------------------|------|
|Support of data sources of Hadoop| Yes| Yes|
|Support file format| Yes|Yes|
|Work with BI| No|Yes|
|Code Size| Very Long (due to only Java support)| Less (due to python and scala support)|

**5. Failure to Tolerance**


|Parameter| Hadoop (Map Reduce) | Spark|
|:--------|:--------------------|------|
|Retires per task| Yes|Yes|
|Speculative Executive|Yes|Yes|
|Relies on| Hard Drive| Buffer|
|Time is taken| Less| More|
<p style='text-align: justify;'> 
 Spark and Hadoop MapReduce both retires per task and follows speculative execution. However, MapReduce starts on the hard drives, which give an advantage to Hadoop over Spark.
 </p>

### Analysis based on Application Scope
**1. Machine Learning Support**

|Parameter| Hadoop (Map Reduce) | Spark|
|:--------|:--------------------|------|
|Tools for ML| Mahout| MLLib|
APIs support| Java Only| Java, Scala, Python|
|Iterative algorithm performance| Slower| Very Fast|
|Support In-memory processing| Yes| No|
<p style='text-align: justify;'> 
The machine learning a feature-based comparison of both the frameworks for batter understating and suitability in Big Data Analytics.
</p>

**2. SQL Support**

|Parameter| Hadoop (Map Reduce) | Spark|
|:--------|:--------------------|------|
|Engine| Hive| Spark SQL|
|Language| HiveQL| HiveQL and RDD programming language (Java, Scala, Python)|
|Scale| Petabytes| Terabytes|
|Formats| CSV, JASON, Parquet| CSV, JASON, Parquet|

**Quick Overview** 

|Functionality| Hadoop (Map Reduce) | Spark|
|:------------|:--------------------|------|
|Operational Principle| Distributed Compute + Distrbiuted Storage| Only Distributed Compute|
|Computation Type| Based on Map Reduce| Widespread Computation|
|Storage Area| Typically, data on HDFS| Both In-memory and On-disk|
|Iterative support| Not ideal for iterative workload| Perform Efficiently at Iterative workloads|
|Coding support| Java supported, Compact code| Java, Scala, Python, Compact Code|
|Flexibilty of progamming model| Less flexible| More Flexible| 
|Usability| Relatively complex| Easy as compare to Hadoop|
Mutiple API support| No (Java only)| Yes (Java, Scala, Python)|
|Distributed Storage| Use HDFS| Enable Cloud Storage such as NFS mounts or Amazon S3|

## Summing up
<p style='text-align: justify;'> 
So is it Hadoop or Spark? These systems are two of the most prominent distributed systems for processing data on the market today. Hadoop is used mainly for disk-heavy operations with the MapReduce paradigm, and Spark is a more flexible, but more costly in-memory processing architecture. Both are Apache top-level projects, are often used together, and have similarities, but it’s important to understand the features of each when deciding to implement them.
</p>

References:
1. Ketu,Shweta.Mishra.Kumar,Pramod.Agarwal,Sonali.(2020,March5). Performance Analysis of Distributed Computing Frameworks for Big Data Analytics: Hadoop Vs Spark.http://www.scielo.org.mx/scielo.php?pid=S1405-55462020000200669&script=sci_arttext&tlng=en<br>

2. Ahmed,N. L.C,Barczak, Andre.Susnjak,Teo. A.Rahid, Mohammed.(2020, December 14). A comprehensive performance analysis of Apache Hadoop and Apache Spark for large scale data sets using HiBench . https://journalofbigdata.springeropen.com/articles/10.1186/s40537-020-00388-5#Sec3<br>

3. (2021, April 19).What is distributed computing. https://www.ibm.com/docs/en/txseries/8.2?topic=overview-what-is-distributed-computing <br>

4. (2021,April).What is Distributed computing, its Pros and Cons.https://opencirrus.org/distributed-computing-pros-cons/<br>
5. Apache Hadoop. https://hadoop.apache.org/#:~:text=The%20Apache%20Hadoop%20software%20library,offering%20local%20computation%20and%20storage<br>
6. (2020, May 5).Apache Hadoop Architecture Explained(with Diagrams).https://phoenixnap.com/kb/apache-hadoop-architecture-explained  <br>
7. K,Vagdevi.(2021,April 18). Introduction to Big Data and Distributed Systems. https://cloudxlab.com/blog/introduction-to-big-data-and-distributed-computing/ <br>
8. Kalron,Amir.(2020, January 16). How do Hadoop and Spark Stack up?. https://logz.io/blog/hadoop-vs-spark/ <br>








