dsconnect - Power your data connections with python
===================================================

| 1.Overview_
| 2.Installation_
| 3.Usages-Guidelines_
| 4.Examples_
| 5.Support_
| 6.Upcoming-Integrations_
| 7.References_ 

1.Overview
==========
**dsconnect** is prepared for connecting multiple data source by using a single configuration file where a user can maintain a huge list of reusable connection list and can use it by calling single **conid** parameter.
Its main features are the variety of popular data source connection capabilities. It is a single wrapper of all most popular data connection python libraries into a single library.

dsconnect is purley implemented in Python.

2.Installation
==============
| **To install the library, use below command**
|    $ pip install dsconnect

.. note::

    During the installation of package please verify that all the required dependencies installed successfully, if not try to install them one by one.

3.Usages-Guidelines
===================
| This python library need a configured input file which will include list of all datasource details.File should be in below format:-

 +---------+-------------+------------+--------+------------+------------+------------------+-------------+-----------------+
 |**conid**|**host**     |**dbname**  |**port**|**username**|**password**|**datasourcetype**|**conString**|**PythonLibrary**|
 +---------+-------------+------------+--------+------------+------------+------------------+-------------+-----------------+
 |1        |127.0.0.1    |employee    |5433    |livexyz     |live@123    |Redshift          |NA           |psycopg2         |
 +---------+-------------+------------+--------+------------+------------+------------------+-------------+-----------------+

| Once file is prepared with all available datasource connection details, follow the below steps to get data/connect to respective datasource

| **Step 1:** Load  connection details *.csv* file into pandas dataframe             
|             >> import dsconnect as p
|             >> <pandas dataframe name> = pandas.read_csv(<filepath>)
|             >> con = p.config_df(df = <pandas dataframe name>)

| **Step 2:** Pass query with respective conid and get result into pandas
|             >> df = con.mysql(conid=1,sql="select top 10 * from employeesalary")
|             >> df = con.redshift(conid=2,sql="select top 10 * from students")

.. note::

    01. Use the same header name which is provided in sample file format for more help a user can use **p.config_df_sample()** command to see structure of sample configuration file format.
    
    02. Before using conid, verify the datatype of your conid column and pass the same in query for eg. if 1 is string then pass '1', if 1 is int then pass 1.

4.Examples
==========
MySQL
~~~~~~~
| *Package Used:* mysql-connector-python
| Eg. df = con.mysql(conid=<uniqueid>,sql="select top 10 * from <table>")

MS SQL Server
~~~~~~~~~~~~~
| *Package Used:* pyodbc
| Eg. df = con.mssql(conid=<uniqueid>,sql="select top 10 * from <table>")

MS Azure SQL Database
~~~~~~~~~~~~~~~~~~~~~
| *Package Used:* pyodbc
| Eg. df = con.msazuresql(conid=<uniqueid>,sql="select top 10 * from <table>")

Oracle
~~~~~~
| *Package Used:* cx_Oracle
| Eg. df = con.oracle(conid=<uniqueid>,sql="select top 10 * from <table>")

DB2
~~~~~~~
| *Package Used:* ibm_db
| Eg. df = con.ibmdb(conid=<uniqueid>,sql="select top 10 * from <table>")

PostgreSQL
~~~~~~~~~~
| *Package Used:* psycopg2
| Eg. df = con.postgresql(conid=<uniqueid>,sql="select top 10 * from <table>")

Redshift
~~~~~~~~
| *Package Used:* psycopg2
| Eg. df = con.redshift(conid=<uniqueid>,sql="select top 10 * from <table>")

Gsheet
~~~~~~
| *Package Used:* pygsheets
| Eg. con = con.gsheet(conid=<uniqueid>) then proceed with pygsheets documentation with *con* as connection object.
| **conString** column should be use to store client_secret.json path(Obtained from Google Gsheet API OAuth).

 +-----+----+------+----+--------+--------+--------------+---------+------------------+-------------+
 |conid|host|dbname|port|username|password|datasourcetype|conString                   |PythonLibrary|
 +-----+----+------+----+--------+--------+--------------+---------+------------------+-------------+
 |1    |NA  |NA    |NA  |NA      |NA      |Gsheet        |<D:/Test/client_secret.json>|pygsheets    |
 +-----+----+------+----+--------+--------+--------------+---------+------------------+-------------+

URL Download
~~~~~~~~~~~~
| *Package Used:* requests
| A user can directly pass download url.
| Eg. p.byurl(url<download url>,targetpath=<path to store downloaded file>)

SFTP
~~~~
| *Package Used:* pysftp
| Eg. con = con.sftp(conid=1) then proceed with pysftp documentation with *con* as connection object.

 +-----+---------+------+--------+--------+--------+--------------+---------+-------------+
 |conid|host     |dbname|port    |username|password|datasourcetype|conString|PythonLibrary|
 +-----+---------+------+--------+--------+--------+--------------+---------+-------------+
 |1    |127.0.0.1|NA    |NA      |xxxxxx  |xxxxxx  |SFTP          |NA       |pysftp       |
 +-----+---------+------+--------+--------+--------+--------------+---------+-------------+

AWS S3
~~~~~~
| *Package Used:* boto3
| Eg. con = con.s3connect(conid=1) then proceed with boto3 documentation with *con* as connection object for S3 bucket.

 +-----+----+------+----+--------+--------+--------------+-------------------------------------+-------------+
 |conid|host|dbname|port|username|password|datasourcetype|conString                            |PythonLibrary|
 +-----+----+------+----+--------+--------+--------------+-------------------------------------+-------------+
 |1    |NA  |NA    |NA  |NA      |NA      |AWS S3        |{'accesskey':'XXX','secretkey':'XXX'}|boto3        |
 +-----+----+------+----+--------+--------+--------------+-------------------------------------+-------------+

S3 SELECT
~~~~~~~~~
| *Package Used:* boto3
| Eg. df = con.s3select(conid=1,bucket=<bucket name>,select_stmnt=<SQL expr>,output_format=<CSV/JSON>,fielddelimiter=<',','|' etc. Only applicable for csv/txt files>)



5.Support
==========
 +--------------------+------------------------------------+
 |**Operating System**|Linux/OSX/Windows                   |
 +--------------------+------------------------------------+
 |**Python Version**  |2/2.7/3/3.2/3.3/3.4/3.5/3.7 etc.    |
 +--------------------+------------------------------------+ 

6.Upcoming-Integrations
=======================

| Below are the list of datasources planned to add in next version of **dsconnect**

| 01. Mixpanel
| 02. ElasticSearch
| 03. HDFS
| 04. Hive
| 05. Google Analytics
| 06. Google Adwords
| 07. Sisense BI - REST API Connect and many more.
| 08. Dropbox

7.References
============
| Many thanks to the developers of dependent packages. Please use the below links to get deeper knowledge about required packages:-

| **PYSFTP:** https://pypi.org/project/pysftp/
| **ORACLE:** https://pypi.org/project/cx_Oracle/
| **MYSQL:** https://pypi.org/project/mysql-connector-python/
| **PSYCOPG2:** https://pypi.org/project/psycopg2/
| **PYODBC:** https://pypi.org/project/pyodbc/
| **PYGSHEETS:** https://pypi.org/project/pygsheets/
| **BOTO3:** https://pypi.org/project/boto3/
| **IBM DB2:** https://pypi.org/project/ibm_db/