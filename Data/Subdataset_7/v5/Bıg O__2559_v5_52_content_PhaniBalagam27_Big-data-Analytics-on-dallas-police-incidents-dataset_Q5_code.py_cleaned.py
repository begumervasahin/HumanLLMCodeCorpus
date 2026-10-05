from pyspark import SparkConf, SparkContext
from pyspark.sql import HiveContext
from subprocess import call
b1 = SparkConf().setAppName("Q2")
b2 = SparkContext(b1=b1)
b3 = HiveContext(b2)
def fonk1():
    b4 = b3.read.load('pxb161930/Police_Incidents.csv',
                              b5 = 'com.databricks.spark.csv',
                              b6 = 'true', inferSchema='true',
                              b7 = 'univocity')
    return b4
def fonk2(b4):
    b8 = ['Incident Number w/ Year', 'Watch', 'Call (911) Problem', ...]
    b9 = b4.select([column for column in b4.columns if column not in b8])
    for old_col, new_col in [('_', ''), ('/', ''), ('(', ''), (')', ''), ('__', '_')]:
        b9 = b9.toDF(*(c.replace(old_col, new_col) for c in b9.columns))
    return b9
def fonk3(b4):
    b4.registerTempTable("q5data")
def fonk4():
    b3.sql("drop table if exists default.q5data")
    b3.sql("create table q5table as select * from q5data")
def fonk5():
    b10 = ["hive", "-e", "INSERT OVERWRITE LOCAL DIRECTORY '/root/q5data' ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' select * from q5table;"]
    call(b10)
def fonk6():
    b4 = fonk1()
    b9 = fonk2(b4)
    fonk3(b9)
    fonk4()
    fonk5()
    b2.stop()
if b11 = = "__main__":
    fonk6()