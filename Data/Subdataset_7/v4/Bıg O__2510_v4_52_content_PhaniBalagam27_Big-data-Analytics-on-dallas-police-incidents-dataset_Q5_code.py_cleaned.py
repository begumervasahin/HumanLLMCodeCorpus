from pyspark import SparkConf, SparkContext
from pyspark.sql import HiveContext, SQLContext
from pyspark.sql.functions import unix_timestamp
from subprocess import call
b1 = SparkConf().setAppName("Q2")
b2 = SparkContext(b1=b1)
b3 = HiveContext(b2)
b4 = b3.read.load('pxb161930/Police_Incidents.csv', format='com.databricks.spark.csv', header='true', inferSchema='true', parserLib='univocity')
b5 = ['Incident Number w/ Year', 'Watch', 'Call (911) Problem', ...]
b6 = b4.select([column for column in b4.columns if column not in b5])
for old_col, new_col in [('_', ''), ('/', ''), ('(', ''), (')', ''), ('__', '_')]:
    b6 = b6.toDF(*(c.replace(old_col, new_col) for c in b6.columns))
b6.registerTempTable("q5data")
b3.sql("drop table if exists default.q5data")
b3.sql("create table q5table as select * from q5data")
b7 = ["hive", "-e", "INSERT OVERWRITE LOCAL DIRECTORY '/root/q5data' ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' select * from q5table;"]
call(b7)
b2.stop()