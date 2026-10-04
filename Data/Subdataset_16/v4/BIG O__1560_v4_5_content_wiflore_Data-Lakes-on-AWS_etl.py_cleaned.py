import configparser
import os
from datetime import datetime
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, col, year, month, dayofmonth, hour, weekofyear, dayofweek, monotonically_increasing_id
from pyspark.sql.types import StructType, StructField, DoubleType, StringType, IntegerType
def fonk1():
    b1 = SparkSession \
        .builder \
        .b14("b1.jars.packages", "org.apache.hadoop:hadoop-aws:2.7.0") \
        .getOrCreate()
    return b1
def fonk2(b1, b15, b16):
    b2 = os.path.join(b15, "b2/*/*/*/*.json")
    b3 = StructType([
        StructField("song_id", StringType()),
        StructField("artist_id", StringType()),
        StructField("artist_latitude", DoubleType()),
        StructField("artist_location", StringType()),
        StructField("artist_longitude", DoubleType()),
        StructField("artist_name", StringType()),
        StructField("duration", DoubleType()),
        StructField("num_songs", IntegerType()),
        StructField("title", StringType()),
        StructField("year", IntegerType()),
    ])
    b4 = b1.read.json(b2, b3=b3)
    b5 = b4.select("song_id", "title", "artist_id", "year", "duration").dropDuplicates()
    b5.write.partitionBy("year", "artist_id").parquet(os.path.join(b16, 'songs/'), b6 = 'overwrite')
    b7 = b4.selectExpr(
        "artist_id",
        "artist_name as name",
        "artist_location as location",
        "artist_latitude as latitude",
        "artist_longitude as longitude"
    ).dropDuplicates()
    b7.write.parquet(os.path.join(b16, 'artists/'), b6 = 'overwrite')
def fonk3(b1, b15, b16):
    b8 = os.path.join(b15, "b8/*/*/*.json")
    b4 = b1.read.json(b8)
    b4 = b4.filter(b4.page == 'NextSong')
    b9 = b4.selectExpr(
        "userId as user_id",
        "firstName as first_name",
        "lastName as last_name",
        "gender",
        "level"
    ).dropDuplicates()
    b9.write.parquet(os.path.join(b16, 'users/'), b6 = 'overwrite')
    b10 = udf(lambda x: datetime.fromtimestamp(x / 1000).strftime('%Y-%m-%d %H:%M:%S'))
    b4 = b4.withColumn("start_time", b10(b4.ts))
    b11 = b4.select("start_time").dropDuplicates().withColumn("hour", hour(col("start_time"))).withColumn("day", dayofmonth(col("start_time"))).withColumn("week", weekofyear(col("start_time"))).withColumn("month", month(col("start_time"))).withColumn("year", year(col("start_time"))).withColumn("weekday", dayofweek(col("start_time")))
    b11.write.partitionBy("year", "month").parquet(os.path.join(b16, 'time/'), b6 = 'overwrite')
    b12 = b1.read.json(os.path.join(b15, "b2/*/*/*/*.json"))
    b13 = b4.join(b12, (b4.song == b12.title) & (b4.artist == b12.artist_name) & (b4.length == b12.duration), 'left_outer') \
        .select(
            b4.start_time,
            b4.userId.alias("user_id"),
            b4.level,
            b12.song_id,
            b12.artist_id,
            b4.sessionId.alias("session_id"),
            b4.location,
            b4.userAgent.alias("user_agent")
        ) \
        .withColumn("songplay_id", monotonically_increasing_id()) \
        .withColumn("year", year(col("start_time"))) \
        .withColumn("month", month(col("start_time")))
    b13.write.partitionBy('year', 'month').parquet(os.path.join(b16, 'songplays'), b6 = 'overwrite')
def fonk4():
    b14 = configparser.ConfigParser()
    b14.read('dl.cfg')
    os.environ['AWS_ACCESS_KEY_ID'] = b14['S3']['AWS_ACCESS_KEY_ID']
    os.environ['AWS_SECRET_ACCESS_KEY'] = b14['S3']['AWS_SECRET_ACCESS_KEY']
    b1 = fonk1()
    b15 = "s3a:
    b16 = "s3a:
    print("Processing song data ... ")
    fonk2(b1, b15, b16)
    print("Song data processing complete.")
    print("Processing log data ...")
    fonk3(b1, b15, b16)
    print('Log data processing complete.')
if b17 = = "__main__":
    fonk4()