from pyspark import SparkConf, SparkContext
from pyspark.sql import HiveContext, SQLContext
from pyspark.sql.functions import unix_timestamp
from subprocess import call
def fonk1():
    b1 = SparkConf().setAppName("Q2")
    b2 = SparkContext(b1=b1)
    b3 = HiveContext(b2)
    b4 = fonk2(b3, 'pxb161930/Police_Incidents.csv')
    b5 = [
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
    b6 = fonk3(b4, b5)
    fonk5(b3, b6, "default.q5table")
    fonk6()
    b2.stop()
def fonk2(b3, file_path):
    return b3.read.load(
        file_path,
        b7 = 'com.databricks.spark.csv',
        b8 = 'true',
        b9 = 'true',
        b10 = 'univocity'
    )
def fonk3(b4, b5):
    b11 = b4.select([column for column in b4.columns if column not in b5])
    b12 = b11.toDF(*(fonk4(c) for c in b11.columns))
    b6 = b12.toDF(*(c.replace('__', '_') for c in b12.columns))
    return b6
def fonk4(column_name):
    return column_name.replace(' ', '_').replace('/', '').replace('(', '').replace(')', '')
def fonk5(b3, b4, table_name):
    b3.sql(f"DROP TABLE IF EXISTS {table_name}")
    b4.registerTempTable("temp_table")
    b3.sql(f"CREATE TABLE {table_name} AS SELECT * FROM temp_table")
def fonk6():
    b13 = [
        "hive",
        "-e",
        "INSERT OVERWRITE LOCAL DIRECTORY '/root/q5data' ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' SELECT * FROM default.q5table"
    ]
    call(b13)
if b14 = = '__main__':
    fonk1()