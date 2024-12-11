import configparser
import os
from datetime import datetime
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, col, monotonically_increasing_id
from pyspark.sql.functions import year, month, dayofmonth, hour, weekofyear, dayofweek
from pyspark.sql.types import StructType, StructField, DoubleType, StringType, IntegerType
def fonk1(config_file):
    b1 = configparser.ConfigParser()
    b1.read(config_file)
    return b1['S3']['AWS_ACCESS_KEY_ID'], b1['S3']['AWS_SECRET_ACCESS_KEY']
def fonk2(access_key_id, secret_access_key):
    os.environ['AWS_ACCESS_KEY_ID'] = access_key_id
    os.environ['AWS_SECRET_ACCESS_KEY'] = secret_access_key
def fonk3():
    b2 = SparkSession.builder \
        .b1("b2.jars.packages", "org.apache.hadoop:hadoop-aws:2.7.0") \
        .getOrCreate()
    return b2
def fonk4(b2, b18, b19):
    b3 = os.path.join(b18, "song_data/*/*/*/*.json")
    b4 = StructType([
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
    b5 = b2.read.json(b3, schema=b4)
    b6 = b5.select(["song_id", "title", "artist_id", "year", "duration"]).dropDuplicates()
    b6.write.partitionBy("year", "artist_id").parquet(os.path.join(b19, 'songs/'), 'overwrite')
    b7 = b5.selectExpr(["artist_id", "artist_name as name", "artist_location as location",
                                       "artist_latitude as latitude", "artist_longitude as longitude"]).dropDuplicates()
    b7.write.parquet(os.path.join(b19, 'artists/'), 'overwrite')
def fonk5(b2, b18, b19):
    b8 = os.path.join(b18, "log_data/*/*/*.json")
    b9 = b2.read.json(b8)
    b9 = b9.filter(b9.page == 'NextSong')
    b10 = b9.selectExpr(["userId as user_id", "firstName as first_name", "lastName as last_name",
                                     "gender", "level"]).dropDuplicates()
    b10.write.parquet(os.path.join(b19, 'users/'), 'overwrite')
    b11 = udf(lambda x: datetime.fromtimestamp(x/1000).strftime('%Y-%m-%d %H:%M:%S'))
    b9 = b9.withColumn("start_time", b11(b9.ts))
    b12 = b9.select("start_time").dropDuplicates() \
        .withColumn("hour", hour(col("start_time"))) \
        .withColumn("day", dayofmonth(col("start_time"))) \
        .withColumn("week", weekofyear(col("start_time"))) \
        .withColumn("month", month(col("start_time"))) \
        .withColumn("year", year(col("start_time"))) \
        .withColumn("weekday", dayofweek(col("start_time")))
    b12.write.partitionBy("year", "month").parquet(os.path.join(b19, 'time/'), 'overwrite')
    b3 = os.path.join(b18, "song_data/*/*/*/*.json")
    b5 = b2.read.json(b3)
    b13 = b9.join(b5,
                                  (b9.b14 = = b5.title) &
                                  (b9.b15 = = b5.artist_name) &
                                  (b9.b16 = = b5.duration),
                                  'left_outer') \
        .select(b9.start_time, b9.userId.alias("user_id"), b9.level, b5.song_id,
                b5.artist_id, b9.sessionId.alias("session_id"), b9.location,
                b9.userAgent.alias("user_agent")) \
        .withColumn("songplay_id", monotonically_increasing_id()) \
        .withColumn("year", year(col("start_time"))) \
        .withColumn("month", month(col("start_time")))
    b13.write.partitionBy('year', 'month').parquet(os.path.join(b19, 'songplays'), 'overwrite')
def fonk6():
    aws_access_key_id, b17 = fonk1('dl.cfg')
    fonk2(aws_access_key_id, b17)
    b2 = fonk3()
    b18 = "s3a:
    b19 = "s3a:
    print("Processing b14 data...")
    fonk4(b2, b18, b19)
    print("Processing log data...")
    fonk5(b2, b18, b19)
    print('Processing complete.')
if b20 = = "__main__":
    fonk6()