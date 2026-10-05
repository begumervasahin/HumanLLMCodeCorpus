import configparser
import os
from datetime import datetime
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, col, monotonically_increasing_id
from pyspark.sql.functions import year, month, dayofmonth, hour, weekofyear, dayofweek
from pyspark.sql.types import StructType, StructField, DoubleType, StringType, IntegerType
def read_aws_credentials(config_file):
    config = configparser.ConfigParser()
    config.read(config_file)
    return config['S3']['AWS_ACCESS_KEY_ID'], config['S3']['AWS_SECRET_ACCESS_KEY']
def set_aws_credentials(access_key_id, secret_access_key):
    os.environ['AWS_ACCESS_KEY_ID'] = access_key_id
    os.environ['AWS_SECRET_ACCESS_KEY'] = secret_access_key
def create_spark_session():
    spark = SparkSession.builder \
        .config("spark.jars.packages", "org.apache.hadoop:hadoop-aws:2.7.0") \
        .getOrCreate()
    return spark
def process_song_data(spark, input_data, output_data):
    song_data_path = os.path.join(input_data, "song_data/*/*/*/*.json")
    song_schema = StructType([
        StructField("song_id", StringType()),
        StructField("artist_id", StringType()),
        StructField("artist_latitude", DoubleType()),
        StructField("artist_location", StringType()),
        StructField("artist_longitude", DoubleType()),
        StructField("artist_name", StringType()),
        StructField("duration", DoubleType()),
        StructField("num_songs", IntegerType()),
        StructField("title", StringType()),
        StructField("year", IntegerType())
    ])
    song_df = spark.read.json(song_data_path, schema=song_schema)
    songs_table = song_df.select(["song_id", "title", "artist_id", "year", "duration"]).dropDuplicates()
    songs_table.write.partitionBy("year", "artist_id").parquet(os.path.join(output_data, 'songs/'), 'overwrite')
    artist_table = song_df.selectExpr(["artist_id", "artist_name as name", "artist_location as location",
                                       "artist_latitude as latitude", "artist_longitude as longitude"]).dropDuplicates()
    artist_table.write.parquet(os.path.join(output_data, 'artists/'), 'overwrite')
def process_log_data(spark, input_data, output_data):
    log_data_path = os.path.join(input_data, "log_data/*/*/*.json")
    log_df = spark.read.json(log_data_path)
    log_df = log_df.filter(log_df.page == 'NextSong')
    users_table = log_df.selectExpr(["userId as user_id", "firstName as first_name", "lastName as last_name",
                                     "gender", "level"]).dropDuplicates()
    users_table.write.parquet(os.path.join(output_data, 'users/'), 'overwrite')
    get_timestamp = udf(lambda x: datetime.fromtimestamp(x/1000).strftime('%Y-%m-%d %H:%M:%S'))
    log_df = log_df.withColumn("start_time", get_timestamp(log_df.ts))
    time_table = log_df.select("start_time").dropDuplicates() \
        .withColumn("hour", hour(col("start_time"))) \
        .withColumn("day", dayofmonth(col("start_time"))) \
        .withColumn("week", weekofyear(col("start_time"))) \
        .withColumn("month", month(col("start_time"))) \
        .withColumn("year", year(col("start_time"))) \
        .withColumn("weekday", dayofweek(col("start_time")))
    time_table.write.partitionBy("year", "month").parquet(os.path.join(output_data, 'time/'), 'overwrite')
    song_data_path = os.path.join(input_data, "song_data/*/*/*/*.json")
    song_df = spark.read.json(song_data_path)
    songplays_table = log_df.join(song_df,
                                  (log_df.song == song_df.title) &
                                  (log_df.artist == song_df.artist_name) &
                                  (log_df.length == song_df.duration),
                                  'left_outer') \
        .select(log_df.start_time, log_df.userId.alias("user_id"), log_df.level, song_df.song_id,
                song_df.artist_id, log_df.sessionId.alias("session_id"), log_df.location,
                log_df.userAgent.alias("user_agent")) \
        .withColumn("songplay_id", monotonically_increasing_id()) \
        .withColumn("year", year(col("start_time"))) \
        .withColumn("month", month(col("start_time")))
    songplays_table.write.partitionBy('year', 'month').parquet(os.path.join(output_data, 'songplays'), 'overwrite')
def main():
    aws_access_key_id, aws_secret_access_key = read_aws_credentials('dl.cfg')
    set_aws_credentials(aws_access_key_id, aws_secret_access_key)
    spark = create_spark_session()
    input_data = "s3a:
    output_data = "s3a:
    print("Processing song data...")
    process_song_data(spark, input_data, output_data)
    print("Processing log data...")
    process_log_data(spark, input_data, output_data)
    print('Processing complete.')
if __name__ == "__main__":
    main()