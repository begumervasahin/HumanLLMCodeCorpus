import configparser
from datetime import datetime
import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, col, monotonically_increasing_id
from pyspark.sql.functions import year, month, dayofmonth, hour, weekofyear, dayofweek
from pyspark.sql.types import StructType, StructField, DoubleType, StringType, IntegerType
b1 = configparser.ConfigParser()
b1.read('dl.cfg')
os.environ['AWS_ACCESS_KEY_ID'] = b1['S3']['AWS_ACCESS_KEY_ID']
os.environ['AWS_SECRET_ACCESS_KEY'] = b1['S3']['AWS_SECRET_ACCESS_KEY']
def fonk1():
    b2 = SparkSession.builder \
        .b1("b2.jars.packages", "org.apache.hadoop:hadoop-aws:2.7.0") \
        .getOrCreate()
    return b2
def fonk2(b2, b17, b18):
    b3 = os.path.join(b17, "b3/*/*/*/*.json")
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
    b5 = b2.read.json(b3, b4=b4)
    b6 = b5.select(["song_id", "title", "artist_id", "year", "duration"]).dropDuplicates()
    b6.write.partitionBy("year", "artist_id").parquet(os.path.join(b18, 'songs/'), 'overwrite')
    b7 = b5.selectExpr(["artist_id", "artist_name as name", "artist_location as location",
                                  "artist_latitude as latitude", "artist_longitude as longitude"]).dropDuplicates()
    b7.write.parquet(os.path.join(b18, 'artists/'), 'overwrite')
def fonk3(b2, b17, b18):
    b8 = os.path.join(b17, "b8/*/*/*.json")
    b5 = b2.read.json(b8)
    b5 = b5.filter(b5.page == 'NextSong')
    b9 = b5.selectExpr(["userId as user_id", "firstName as first_name", "lastName as last_name",
                                 "gender", "level"]).dropDuplicates()
    b9.write.parquet(os.path.join(b18, 'users/'), 'overwrite')
    b10 = udf(lambda x: datetime.fromtimestamp(x/1000).strftime('%Y-%m-%d %H:%M:%S'))
    b5 = b5.withColumn("start_time", b10(b5.ts))
    b11 = b5.select("start_time").dropDuplicates() \
        .withColumn("hour", hour(col("start_time"))) \
        .withColumn("day", dayofmonth(col("start_time"))) \
        .withColumn("week", weekofyear(col("start_time"))) \
        .withColumn("month", month(col("start_time"))) \
        .withColumn("year", year(col("start_time"))) \
        .withColumn("weekday", dayofweek(col("start_time")))
    b11.write.partitionBy("year", "month").parquet(os.path.join(b18, 'time/'), 'overwrite')
    b12 = b2.read.json(os.path.join(b17, "b3/*/*/*/*.json"))
    b13 = b5.join(b12,
                              (b5.b14 = = b12.title) &
                              (b5.b15 = = b12.artist_name) &
                              (b5.b16 = = b12.duration),
                              'left_outer') \
        .select(b5.start_time, b5.userId.alias("user_id"), b5.level, b12.song_id,
                b12.artist_id, b5.sessionId.alias("session_id"), b5.location,
                b5.userAgent.alias("user_agent")) \
        .withColumn("songplay_id", monotonically_increasing_id()) \
        .withColumn("year", year(col("start_time"))) \
        .withColumn("month", month(col("start_time")))
    b13.write.partitionBy('year', 'month').parquet(os.path.join(b18, 'songplays'), 'overwrite')
def fonk4():
    b2 = fonk1()
    b17 = "s3a:
    b18 = "s3a:
    print("Processing b14 data...")
    fonk2(b2, b17, b18)
    print("Processing log data...")
    fonk3(b2, b17, b18)
    print('Processing complete.')
if b19 = = "__main__":
    fonk4()