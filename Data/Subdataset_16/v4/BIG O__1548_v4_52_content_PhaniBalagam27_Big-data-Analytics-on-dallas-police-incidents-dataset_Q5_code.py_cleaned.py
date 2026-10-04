from pyspark import SparkConf, SparkContext
from pyspark.sql import HiveContext, SQLContext
from pyspark.sql.functions import unix_timestamp
from subprocess import call
b1 = SparkConf().setAppName("Q2")
b2 = SparkContext(b1=b1)
b3 = HiveContext(b2)
b4 = b3.read.load(
    'pxb161930/Police_Incidents.csv',
    b5 = 'com.databricks.spark.csv',
    b6 = 'true',
    b7 = 'true',
    b8 = 'univocity'
)
b9 = [
    'Incident Number w/ Year', 'Watch', 'Call (911) Problem', 'Type of Incident', 'Penalty Class',
    'Type of Location', 'Type of Property', 'Street Block', 'Street Direction', 'Street Name',
    'Incident Address', 'City', 'X Coordinate', 'Y Coordinate', 'Reporting Area', 'Beat', 'Division',
    'Sector', 'Council District', 'Target Area Action Grids', 'Community', 'Ending Date/Time',
    'Map Date', 'Date of Report', 'Date incident created', 'Offense Entered Time', 'Offense Entered  Date/Time',
    'Call Date Time', 'Call Dispatch Date Time', 'Complainant Age', 'Complainant Age at Offense',
    'Complainant Home Address', 'Complainant Zip Code', 'Complainant City', 'Complainant Business Name',
    'Complainant Business Address', 'Investigating Unit 1', 'Investigating Unit 2', 'Offense Status',
    'Victim Injury Description', 'Victim Condition', 'RMS Code', 'Offense Code CC', 'CJIS Code',
    'Penal Code', 'UCR Offense Name', 'Modus Operandi (MO)', 'Hate Crime', 'Gang Related Offense',
    'Drug Related Incident'
]
b10 = b4.select([column for column in b4.columns if column not in b9])
b11 = b10.toDF(*(c.replace(' ', '_').replace('/', '').replace('(', '').replace(')', '') for c in b10.columns))
b12 = b11.toDF(*(c.replace('__', '_') for c in b11.columns))
b3.sql("DROP TABLE IF EXISTS default.q5table")
b12.registerTempTable("q5data")
b3.sql("CREATE TABLE q5table AS SELECT * FROM q5data")
b13 = [
    "hive",
    "-e",
    "INSERT OVERWRITE LOCAL DIRECTORY '/root/q5data' ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' SELECT * FROM q5table"
]
call(b13)
b2.close()