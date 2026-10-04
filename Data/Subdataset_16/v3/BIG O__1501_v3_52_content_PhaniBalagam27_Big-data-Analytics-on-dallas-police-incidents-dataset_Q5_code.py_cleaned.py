from pyspark import SparkConf, SparkContext
from pyspark.sql import HiveContext
from subprocess import call
def fonk1():
    b1 = SparkConf().setAppName("Q2")
    b2 = SparkContext(b1=b1)
    b3 = HiveContext(b2)
    b4 = 'pxb161930/Police_Incidents.csv'
    b5 = b3.read.load(b4, format='csv', header='true', inferSchema='true')
    b6 = [
        'Incident Number w/ Year', 'Watch', 'Call (911) Problem', 'Type of Incident', 'Penalty Class', 'Type of Location',
        'Type of Property', 'Street Block', 'Street Direction', 'Street Name', 'Incident Address', 'City', 'X Coordinate',
        'Y Coordinate', 'Reporting Area', 'Beat', 'Division', 'Sector', 'Council District', 'Target Area Action Grids',
        'Community', 'Ending Date/Time', 'Map Date', 'Date of Report', 'Date incident created', 'Offense Entered Time',
        'Offense Entered  Date/Time', 'Call Date Time', 'Call Dispatch Date Time', 'Complainant Age',
        'Complainant Age at Offense', 'Complainant Home Address', 'Complainant Zip Code', 'Complainant City',
        'Complainant Business Name', 'Complainant Business Address', 'Investigating Unit 1', 'Investigating Unit 2',
        'Offense Status', 'Victim Injury Description', 'Victim Condition', 'RMS Code', 'Offense Code CC', 'CJIS Code',
        'Penal Code', 'UCR Offense Name', 'Modus Operandi (MO)', 'Hate Crime', 'Gang Related Offense', 'Drug Related Incident'
    ]
    b7 = [col for col in b5.columns if col not in b6]
    b8 = b5.select(b7)
    b9 = [
        c.replace(' ', '_').replace('/', '').replace('(', '').replace(')', '').replace('__', '_')
        for c in b8.columns
    ]
    b10 = b8.toDF(*b9)
    b10.registerTempTable("q5data")
    b3.sql("DROP TABLE IF EXISTS default.q5table")
    b3.sql("CREATE TABLE default.q5table AS SELECT * FROM q5data")
    b11 = "INSERT OVERWRITE LOCAL DIRECTORY '/root/q5data' ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' SELECT * FROM default.q5table"
    call(["hive", "-e", b11])
    b2.stop()
if b12 = = '__main__':
    fonk1()