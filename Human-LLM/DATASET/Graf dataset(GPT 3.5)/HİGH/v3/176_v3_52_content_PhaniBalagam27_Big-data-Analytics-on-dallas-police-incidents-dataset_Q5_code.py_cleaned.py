from pyspark import SparkConf, SparkContext
from pyspark.sql import HiveContext
from subprocess import call
def fonk1(app_name):
    b1 = SparkConf().setAppName(app_name)
    b2 = SparkContext(b1=b1)
    return b2
def fonk2(spark_context, file_path):
    b3 = HiveContext(spark_context)
    b4 = b3.read.load(file_path, format='com.databricks.spark.csv', header='true', inferSchema='true', parserLib='univocity')
    return b4
def fonk3(b3, b4, table_name):
    b3.sql(f"DROP TABLE IF EXISTS default.{table_name}")
    b4.registerTempTable(table_name)
    b3.sql(f"CREATE TABLE {table_name} AS SELECT * FROM {table_name}")
def fonk4(b3, table_name, directory_path):
    b5 = f"INSERT OVERWRITE LOCAL DIRECTORY '{directory_path}' ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' SELECT * FROM {table_name}"
    b6 = ["hive", "-e", b5]
    call(b6)
def fonk5():
    b2 = fonk1("Q2")
    b4 = fonk2(b2, 'pxb161930/Police_Incidents.csv')
    b7 = [
    ]
    b8 = b4.select([column for column in b4.columns if column not in b7])
    fonk3(HiveContext(b2), df_final, "q5data")
    fonk4(HiveContext(b2), "q5table", "/root/q5data")
    b2.stop()
if b9 = = "__main__":
    fonk5()