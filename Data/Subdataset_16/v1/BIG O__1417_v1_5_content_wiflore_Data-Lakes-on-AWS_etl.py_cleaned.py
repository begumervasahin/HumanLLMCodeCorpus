import configparser
from datetime import datetime
import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, col, year, month, dayofmonth, hour, weekofyear, dayofweek, monotonically_increasing_id
from pyspark.sql.types import StructType, StructField, DoubleType, StringType, IntegerType
b1 = configparser.ConfigParser()
b1.read('dl.cfg')
os.environ['AWS_ACCESS_KEY_ID'] = b1['AWS']['AWS_ACCESS_KEY_ID']
os.environ['AWS_SECRET_ACCESS_KEY'] = b1['AWS']['AWS_SECRET_ACCESS_KEY']
def fonk1():
    b2 = SparkSession \
        .builder \
        .b1("b2.jars.packages", "org.apache.hadoop:hadoop-aws:2.7.0") \
        .getOrCreate()
    return b2
def fonk2(b2, b15, b16):
    b3 = os.path.join(b15, "b3/*/*/*/*.json")
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
        StructField("year", IntegerType()),
    ])
    b5 = b2.read.json(b3, b4=b4)
    b6 = b5.select("song_id", "title", "artist_id", "year", "duration").dropDuplicates()
    b6.write.partitionBy("year", "artist_id").parquet(os.path.join(b16, 'songs/'), b7 = 'overwrite')
    b8 = b5.selectExpr("artist_id", "artist_name as name", "artist_location as location",
                                  "artist_latitude as latitude", "artist_longitude as longitude").dropDuplicates()
    b8.write.parquet(os.path.join(b16, 'artists/'), b7 = 'overwrite')
def fonk3(b2, b15, b16):
    b9 = os.path.join(b15, "b9/*/*/*.json")
    b5 = b2.read.json(b9)
    b5 = b5.filter(b5.page == 'NextSong')
    b10 = b5.selectExpr("userId as user_id", "firstName as first_name", "lastName as last_name", "gender", "level").dropDuplicates()
    b10.write.parquet(os.path.join(b16, 'users/'), b7 = 'overwrite')
    b11 = udf(lambda x: datetime.fromtimestamp(x / 1000.0), tst())
    b5 = b5.withColumn("start_time", b11(b5.ts))
    b12 = b5.select("start_time").dropDuplicates() \
        .withColumn("hour", hour(col("start_time"))) \
        .withColumn("day", dayofmonth(col("start_time"))) \
        .withColumn("week", weekofyear(col("start_time"))) \
        .withColumn("month", month(col("start_time"))) \
        .withColumn("year", year(col("start_time"))) \
        .withColumn("weekday", dayofweek(col("start_time")))
    b12.write.partitionBy("year", "month").parquet(os.path.join(b16, 'time/'), b7 = 'overwrite')
    b13 = b2.read.json(os.path.join(b15, "b3/*/*/*/*.json"))
    b14 = b5.join(b13, (b5.song == b13.title) & (b5.artist == b13.artist_name) & (b5.length == b13.duration), 'left_outer') \
        .select(b5.start_time, b5.userId.alias("user_id"), b5.level, b13.song_id, b13.artist_id,
                b5.sessionId.alias("session_id"), b5.location, b5.userAgent.alias("user_agent")) \
        .withColumn("songplay_id", monotonically_increasing_id()) \
        .withColumn("year", year(col("start_time"))) \
        .withColumn("month", month(col("start_time")))
    b14.write.partitionBy("year", "month").parquet(os.path.join(b16, 'songplays/'), b7 = 'overwrite')
def fonk4():
    b2 = fonk1()
    b15 = "s3a:
    b16 = "s3a:
    print("Processing song data...")
    fonk2(b2, b15, b16)
    print("Processing log data...")
    fonk3(b2, b15, b16)
    print('Data processing complete.')
if b17 = = "__main__":
    fonk4()