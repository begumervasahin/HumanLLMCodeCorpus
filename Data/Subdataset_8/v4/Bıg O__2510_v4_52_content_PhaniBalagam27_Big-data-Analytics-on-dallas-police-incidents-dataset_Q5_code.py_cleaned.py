from pyspark import SparkConf, SparkContext
from pyspark.sql import HiveContext, SQLContext
from pyspark.sql.functions import unix_timestamp
from subprocess import call
conf = SparkConf().setAppName("Q2")
sc = SparkContext(conf=conf)
sqlContext = HiveContext(sc)
df = sqlContext.read.load('pxb161930/Police_Incidents.csv', format='com.databricks.spark.csv', header='true', inferSchema='true', parserLib='univocity')
columns_to_drop = ['Incident Number w/ Year', 'Watch', 'Call (911) Problem', ...]
df_cleaned = df.select([column for column in df.columns if column not in columns_to_drop])
for old_col, new_col in [('_', ''), ('/', ''), ('(', ''), (')', ''), ('__', '_')]:
    df_cleaned = df_cleaned.toDF(*(c.replace(old_col, new_col) for c in df_cleaned.columns))
df_cleaned.registerTempTable("q5data")
sqlContext.sql("drop table if exists default.q5data")
sqlContext.sql("create table q5table as select * from q5data")
args = ["hive", "-e", "INSERT OVERWRITE LOCAL DIRECTORY '/root/q5data' ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' select * from q5table;"]
call(args)
sc.stop()