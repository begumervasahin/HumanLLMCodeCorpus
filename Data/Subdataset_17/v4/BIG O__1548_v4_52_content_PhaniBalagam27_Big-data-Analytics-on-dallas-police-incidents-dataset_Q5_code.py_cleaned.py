from pyspark import SparkConf, SparkContext
from pyspark.sql import HiveContext, SQLContext
from pyspark.sql.functions import unix_timestamp
from subprocess import call
conf = SparkConf().setAppName("Q2")
sc = SparkContext(conf=conf)
sqlContext = HiveContext(sc)
df = sqlContext.read.load(
    'pxb161930/Police_Incidents.csv',
    format='com.databricks.spark.csv',
    header='true',
    inferSchema='true',
    parserLib='univocity'
)
drop_columns = [
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
df_filtered = df.select([column for column in df.columns if column not in drop_columns])
df_renamed = df_filtered.toDF(*(c.replace(' ', '_').replace('/', '').replace('(', '').replace(')', '') for c in df_filtered.columns))
df_final = df_renamed.toDF(*(c.replace('__', '_') for c in df_renamed.columns))
sqlContext.sql("DROP TABLE IF EXISTS default.q5table")
df_final.registerTempTable("q5data")
sqlContext.sql("CREATE TABLE q5table AS SELECT * FROM q5data")
hive_export_command = [
    "hive",
    "-e",
    "INSERT OVERWRITE LOCAL DIRECTORY '/root/q5data' ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' SELECT * FROM q5table"
]
call(hive_export_command)
sc.close()