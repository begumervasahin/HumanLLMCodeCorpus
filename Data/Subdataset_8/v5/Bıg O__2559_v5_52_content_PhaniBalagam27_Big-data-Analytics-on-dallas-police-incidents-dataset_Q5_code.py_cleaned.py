from pyspark import SparkConf, SparkContext
from pyspark.sql import HiveContext
from subprocess import call
conf = SparkConf().setAppName("Q2")
sc = SparkContext(conf=conf)
sqlContext = HiveContext(sc)
def load_data():
    df = sqlContext.read.load('pxb161930/Police_Incidents.csv',
                              format='com.databricks.spark.csv',
                              header='true', inferSchema='true',
                              parserLib='univocity')
    return df
def clean_data(df):
    columns_to_drop = ['Incident Number w/ Year', 'Watch', 'Call (911) Problem', ...]
    df_cleaned = df.select([column for column in df.columns if column not in columns_to_drop])
    for old_col, new_col in [('_', ''), ('/', ''), ('(', ''), (')', ''), ('__', '_')]:
        df_cleaned = df_cleaned.toDF(*(c.replace(old_col, new_col) for c in df_cleaned.columns))
    return df_cleaned
def create_temp_table(df):
    df.registerTempTable("q5data")
def create_hive_table():
    sqlContext.sql("drop table if exists default.q5data")
    sqlContext.sql("create table q5table as select * from q5data")
def export_to_csv():
    args = ["hive", "-e", "INSERT OVERWRITE LOCAL DIRECTORY '/root/q5data' ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' select * from q5table;"]
    call(args)
def main():
    df = load_data()
    df_cleaned = clean_data(df)
    create_temp_table(df_cleaned)
    create_hive_table()
    export_to_csv()
    sc.stop()
if __name__ == "__main__":
    main()