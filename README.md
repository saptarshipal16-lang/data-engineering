# data-engineering






https://ap-south-1.console.aws.amazon.com/s3/upload/netflixdataset-saptarshi?region=ap-south-1

CONNECT SNF TO AWS

EXTERNAL 7 STAGE, STORAGE INTEGRATION



Stored in which .dbt root

2. INITCAP(...)
This stands for Initial Capitalization. It transforms the string so that the first letter of every word is uppercase and the rest are lowercase.


To put the output in a specified schema lets say DEV




Incremental table is created so that we just capture any new change on the model not to create the whole table again and again

Ephemeral - this table will be created on backend, no physical table. It can be consumed and then only it can be seen


Seeds-
Csv file

It will go under the tables

SNAPSHOT-
To use scd in dbt we use snapshot    scd 6
Dbt snapshot


WE NEED TO CREATE PACKAGE.YAML TO USE UTILS FUNCTION

RUN 
DBT DEPS


In the config also we can put the schema name



Testing







We need to keep the testing schema.yml inside model folder




Macros - function



Dbt documentation--

Dbt docs generate


Dbt docs serve
http://localhost:8080/#!/source_list/netflix<img width="1597" height="6204" alt="image" src="https://github.com/user-attachments/assets/ebc17b1b-613c-4c0e-adbc-adfcd7164c3e" />
