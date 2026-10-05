from pyspark import SparkConf, SparkContext
from pyspark.sql import HiveContext
from subprocess import call
b1 = SparkConf().setAppName("Q2")
b2 = SparkContext(b1=b1)
b3 = HiveContext(b2)
b4 = b3.read.load('pxb161930/Police_Incidents.csv', format='com.databricks.spark.csv', header='true', inferSchema='true', parserLib='univocity')
b5 = ['Incident Number w/ Year', 'Watch', 'Call (911) Problem', 'Type of Incident', 'Penalty Class', 'Type of Location', 'Type of Property', 'Street Block', 'Street Direction', 'Street Name', 'Incident Address', 'City', 'X Coordinate', 'Y Coordinate', 'Reporting Area', 'Beat', 'Division', 'Sector', 'Council District', 'Target Area Action Grids', 'Community','Ending Date/Time', 'Map Date', 'Date of Report', 'Date incident created', 'Offense Entered Time', 'Offense Entered  Date/Time', 'Call Date Time','Call Dispatch Date Time', 'Complainant Age', 'Complainant Age at Offense', 'Complainant Home Address', 'Complainant Zip Code', 'Complainant City', 'Complainant Business Name', 'Complainant Business Address', 'Investigating Unit 1', 'Investigating Unit 2', 'Offense Status', 'Victim Injury Description', 'Victim Condition', 'RMS Code', 'Offense Code CC', 'CJIS Code', 'Penal Code', 'UCR Offense Name', 'Modus Operandi (MO)', 'Hate Crime', 'Gang Related Offense', 'Drug Related Incident']
b6 = b4.select([column for column in b4.columns if column not in b5])
b7 = b6.toDF(*(c.replace(' ', '_') for c in b6.columns))
b8 = b7.toDF(*(c.replace('/', '') for c in b7.columns))
b9 = b8.toDF(*(c.replace('(', '') for c in b8.columns))
b10 = b9.toDF(*(c.replace(')', '') for c in b9.columns))
b11 = b10.toDF(*(c.replace('__', '_') for c in b10.columns))
b3.sql("DROP TABLE IF EXISTS default.q5data")
b11.registerTempTable("q5data")
b3.sql("CREATE TABLE q5table AS SELECT * FROM q5data")
b12 = ["hive", "-e", "INSERT OVERWRITE LOCAL DIRECTORY '/root/q5data' ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' SELECT * FROM q5table"]
call(b12)
b2.stop()