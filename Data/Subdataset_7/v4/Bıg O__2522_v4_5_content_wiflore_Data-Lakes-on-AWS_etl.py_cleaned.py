import configparser
from datetime import datetime
import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, col, monotonically_increasing_id
from pyspark.sql.functions import year, month, dayofmonth, hour, weekofyear, dayofweek
from pyspark.sql.types import StructType, StructField, DoubleType, StringType, IntegerType
b1 = configparser.ConfigParser()
b1.read('dl.cfg')
b2 = b1['AWS_ACCESS_KEY_ID']
b3 = b1['AWS_SECRET_ACCESS_KEY']
os.environ['AWS_ACCESS_KEY_ID'] = b2
os.environ['AWS_SECRET_ACCESS_KEY'] = b3
def fonk1():
    b4 = SparkSession.builder \
        .b1("b4.jars.packages", "org.apache.hadoop:hadoop-aws:2.7.0") \
        .getOrCreate()
    return b4
def fonk2(b4, b19, b20):
    b5 = os.path.join(b19, "song_data/*/*/*/*.json")
    b6 = StructType([
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
    b7 = b4.read.json(b5, b6=b6)
    b8 = b7.select("song_id", "title", "artist_id", "year", "duration").dropDuplicates()
    b8.write.partitionBy("year", "artist_id").parquet(os.path.join(b20, 'songs/'), 'overwrite')
    b9 = b7.selectExpr("artist_id", "artist_name as name", "artist_location as location",
                                  "artist_latitude as latitude", "artist_longitude as longitude").dropDuplicates()
    b9.write.parquet(os.path.join(b20, 'artists/'), 'overwrite')
def fonk3(b4, b19, b20):
    b10 = os.path.join(b19, "log_data/*/*/*.json")
    b7 = b4.read.json(b10)
    b7 = b7.filter(b7.page == 'NextSong')
    b11 = b7.selectExpr("userId as user_id", "firstName as first_name", "lastName as last_name",
                                 "gender", "level").dropDuplicates()
    b11.write.parquet(os.path.join(b20, 'users/'), 'overwrite')
    b12 = udf(lambda x: datetime.fromtimestamp(x/1000).strftime('%Y-%m-%d %H:%M:%S'))
    b7 = b7.withColumn("start_time", b12(b7.ts))
    b13 = b7.select("start_time").dropDuplicates() \
        .withColumn("hour", hour(col("start_time"))) \
        .withColumn("day", dayofmonth(col("start_time"))) \
        .withColumn("week", weekofyear(col("start_time"))) \
        .withColumn("month", month(col("start_time"))) \
        .withColumn("year", year(col("start_time"))) \
        .withColumn("weekday", dayofweek(col("start_time")))
    b13.write.partitionBy("year", "month").parquet(os.path.join(b20, 'time/'), 'overwrite')
    b5 = os.path.join(b19, "song_data/*/*/*/*.json")
    b14 = b4.read.json(b5)
    b15 = b7.join(b14,
                              (b7.b16 = = b14.title) &
                              (b7.b17 = = b14.artist_name) &
                              (b7.b18 = = b14.duration),
                              'left_outer') \
        .select(b7.start_time, b7.userId.alias("user_id"), b7.level, b14.song_id,
                b14.artist_id, b7.sessionId.alias("session_id"), b7.location,
                b7.userAgent.alias("user_agent")) \
        .withColumn("songplay_id", monotonically_increasing_id()) \
        .withColumn("year", year(col("start_time"))) \
        .withColumn("month", month(col("start_time")))
    b15.write.partitionBy('year', 'month').parquet(os.path.join(b20, 'songplays'), 'overwrite')
def fonk4():
    b4 = fonk1()
    b19 = "s3a:
    b20 = "s3a:
    print("Processing b16 data...")
    fonk2(b4, b19, b20)
    print("Processing log data...")
    fonk3(b4, b19, b20)
    print('Finish.')
if b21 = = "__main__":
    fonk4()