from pyspark import SparkConf, SparkContext
from pyspark.sql import HiveContext
from subprocess import call
def initialize_spark_context(app_name):
    conf = SparkConf().setAppName(app_name)
    sc = SparkContext(conf=conf)
    return sc
def load_csv_file(spark_context, file_path):
    sql_context = HiveContext(spark_context)
    df = sql_context.read.load(file_path, format='com.databricks.spark.csv', header='true', inferSchema='true', parserLib='univocity')
    return df
def drop_and_create_table(sql_context, df, table_name):
    sql_context.sql(f"DROP TABLE IF EXISTS default.{table_name}")
    df.registerTempTable(table_name)
    sql_context.sql(f"CREATE TABLE {table_name} AS SELECT * FROM {table_name}")
def export_to_local_directory(sql_context, table_name, directory_path):
    hive_query = f"INSERT OVERWRITE LOCAL DIRECTORY '{directory_path}' ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' SELECT * FROM {table_name}"
    args = ["hive", "-e", hive_query]
    call(args)
def main():
    sc = initialize_spark_context("Q2")
    df = load_csv_file(sc, 'pxb161930/Police_Incidents.csv')
    columns_to_drop = [
    ]
    df_filtered = df.select([column for column in df.columns if column not in columns_to_drop])
    drop_and_create_table(HiveContext(sc), df_final, "q5data")
    export_to_local_directory(HiveContext(sc), "q5table", "/root/q5data")
    sc.stop()
if __name__ == "__main__":
    main()