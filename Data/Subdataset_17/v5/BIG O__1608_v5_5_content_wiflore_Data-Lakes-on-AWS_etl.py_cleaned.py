import configparser
import os
from datetime import datetime
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, col, year, month, dayofmonth, hour, weekofyear, dayofweek, monotonically_increasing_id
from pyspark.sql.types import StructType, StructField, DoubleType, StringType, IntegerType
def create_spark_session():
    spark = SparkSession.builder \
        .config("spark.jars.packages", "org.apache.hadoop:hadoop-aws:2.7.0") \
        .getOrCreate()
    return spark
def process_song_data(spark, input_data, output_data):
    song_data = os.path.join(input_data, "song_data/*/*/*/*.json")
    schema = StructType([
        StructField("song_id", StringType(), True),
        StructField("artist_id", StringType(), True),
        StructField("artist_latitude", DoubleType(), True),
        StructField("artist_location", StringType(), True),
        StructField("artist_longitude", DoubleType(), True),
        StructField("artist_name", StringType(), True),
        StructField("duration", DoubleType(), True),
        StructField("num_songs", IntegerType(), True),
        StructField("title", StringType(), True),
        StructField("year", IntegerType(), True)
    ])
    df = spark.read.json(song_data, schema=schema)
    songs_table = df.select("song_id", "title", "artist_id", "year", "duration").dropDuplicates()
    songs_table.write.partitionBy("year", "artist_id").parquet(os.path.join(output_data, 'songs/'), mode='overwrite')
    artists_table = df.selectExpr(
        "artist_id",
        "artist_name as name",
        "artist_location as location",
        "artist_latitude as latitude",
        "artist_longitude as longitude"
    ).dropDuplicates()
    artists_table.write.parquet(os.path.join(output_data, 'artists/'), mode='overwrite')
def process_log_data(spark, input_data, output_data):
    log_data = os.path.join(input_data, "log_data/*/*/*.json")
    df = spark.read.json(log_data)
    df = df.filter(df.page == 'NextSong')
    users_table = df.selectExpr(
        "userId as user_id",
        "firstName as first_name",
        "lastName as last_name",
        "gender",
        "level"
    ).dropDuplicates()
    users_table.write.parquet(os.path.join(output_data, 'users/'), mode='overwrite')
    get_timestamp = udf(lambda x: datetime.fromtimestamp(x / 1000.0))
    df = df.withColumn("start_time", get_timestamp(df.ts))
    time_table = df.select("start_time").dropDuplicates().withColumn("hour", hour(col("start_time"))).withColumn("day", dayofmonth(col("start_time"))).withColumn("week", weekofyear(col("start_time"))).withColumn("month", month(col("start_time"))).withColumn("year", year(col("start_time"))).withColumn("weekday", dayofweek(col("start_time")))
    time_table.write.partitionBy("year", "month").parquet(os.path.join(output_data, 'time/'), mode='overwrite')
    song_df = spark.read.json(os.path.join(input_data, "song_data/*/*/*/*.json"))
    songplays_table = df.join(song_df, (df.song == song_df.title) & (df.artist == song_df.artist_name) & (df.length == song_df.duration), 'left_outer') \
        .select(
            df.start_time,
            df.userId.alias("user_id"),
            df.level,
            song_df.song_id,
            song_df.artist_id,
            df.sessionId.alias("session_id"),
            df.location,
            df.userAgent.alias("user_agent")
        ) \
        .withColumn("songplay_id", monotonically_increasing_id()) \
        .withColumn("year", year(col("start_time"))) \
        .withColumn("month", month(col("start_time")))
    songplays_table.write.partitionBy('year', 'month').parquet(os.path.join(output_data, 'songplays'), mode='overwrite')
def main():
    config = configparser.ConfigParser()
    config.read('dl.cfg')
    os.environ['AWS_ACCESS_KEY_ID'] = config['S3']['AWS_ACCESS_KEY_ID']
    os.environ['AWS_SECRET_ACCESS_KEY'] = config['S3']['AWS_SECRET_ACCESS_KEY']
    spark = create_spark_session()
    input_data = "s3a:
    output_data = "s3a:
    print("Processing song data ...")
    process_song_data(spark, input_data, output_data)
    print("Song data processing complete.")
    print("Processing log data ...")
    process_log_data(spark, input_data, output_data)
    print("Log data processing complete.")
if __name__ == "__main__":
    main()