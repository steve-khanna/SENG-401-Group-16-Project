# SENG 401: Software Architecture: Group 16 Project
***
### Members: Steve Khanna, Abid Al Labib, David Macababayao, Ragya Mittal, Cobe Reinbold, Long Tran
***
## NOTE: The code for both repositories has been published on GitHub under the following 4 branches:
* https://github.com/steve-khanna/json-schema-validator/tree/SENG-401-Group16-Pattern1-Factory
* https://github.com/steve-khanna/json-schema-validator/tree/SENG-401-Group16-Pattern2-Decorator
* https://github.com/steve-khanna/fastjson/tree/SENG-401-Group16-Pattern3-Singleton
* https://github.com/steve-khanna/fastjson/tree/SENG-401-Group16-Pattern4-Bridge

***
## Overview
| Software System |Original Github Repo |Forked Github Repo | Maven Repo | Size |# of Classes (Total)| # of Classes (Source)| 
| ------------- |:-------------:|:-------------:| :-----:|:-----:|:-----:|----:|
|FastJSON|https://github.com/alibaba/fastjson|https://github.com/steve-khanna/fastjson|https://mvnrepository.com/artifact/com.alibaba/fastjson/1.2.75|15MB|2980|190|
|JSON Schema Validator|https://github.com/java-json-tools/json-schema-validator|https://github.com/steve-khanna/json-schema-validator|https://mvnrepository.com/artifact/com.github.java-json-tools/json-schema-validator/2.2.14|20MB|248|138|


***
## Design Patterns Implemented:

| Software System |Design Pattern 1 | Worked on by |Design Pattern 2 | Worked on by |
| --------------- |:---------------:|:------------:|:---------------:| ------------:|
|JSON Schema Validator| Factory| Steve Khanna, David Macababayao| Decorator| Abid Al Labib, Cobe Reinbold|
|FastJSON| Singleton| Steve Khanna, Long Tran, Ragya Mittal| Decorator| Steve Khanna|

***
## The process:
We used Apache SubVersion to find repositories to work with. This was done using a bash command:

```bash
svn ls -R <Repository URL> | grep "\.java" | wc -l
```

Once we found repositories we were all happy with, we then ran arcade using the following steps.

### Running Arcade
##### Pre-Requistes
* Ensure that the Java Version you are running is 1.8.*
* Ensure that you have Arcade Downloaded: https://bitbucket.org/joshuaga/arcade/downloads/ 

##### Steps
1. **Download** the **source ZIP and release JARs** for both of the above Software Systems.
2. **Create a new folder** under subject_systems for each Software System:
    * **..\subject_systems\fastjson**
    * **..\subject_systems\json-schema-validator**
3. **Extract** the sources into the above folders respectively.
4. **Create a lib folder** within this newly extracted folder:
    * **..\subject_systems\fastjson\fastjson-master\lib**
    * **..\subject_systems\json-schema-validator\json-schema-validator-master\lib**
5. **Move the JAR into lib** for each Software System.
6. **Run** the following commands from the arcade directory:
```bash
java -jar edu.usc.softarch.arcade.AcdcWithSmellDetection.jar subject_systems/fastjson/ subject_systems/fastjson/output/acdc lib

java -jar edu.usc.softarch.arcade.AcdcWithSmellDetection.jar subject_systems/json-schema-validator/ subject_systems/json-schema-validator/output/acdc/ lib
```
