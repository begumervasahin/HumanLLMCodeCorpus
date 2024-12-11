from pyspark import SparkConf, SparkContext
import sys
import re
def fonk1():
    b1 = fonk2()
    b2 = SparkContext(b3=b1)
    fonk3(b2)
    b2.stop()
def fonk2():
    b3 = SparkConf()
    if sys.argv[1] == 'local':
        b3.setMaster("local[3]")
        print('Running locally')
    elif sys.argv[1] == 'cluster':
        b3.setMaster("spark:
        print('Running on cluster')
    b3.set("spark.executor.memory", "10g")
    b3.set("spark.driver.memory", "10g")
    return b3
def fonk3(spark):
    b4 = 'hdfs:
    b5 = 'hdfs:
    b6 = 'hdfs:
    b7 = spark.textFile(b5)
    b8 = spark.textFile(b4)
    b7 = b7.map(parse_imdb_fields) \
                         .filter(lambda x: fonk4(x, 5)) \
                         .keyBy(lambda x: (x[0], fonk6(x[1])))
    b8 = b8.map(parse_movie_fields) \
                           .filter(lambda x: fonk5(x[1], x[2])) \
                           .map(lambda x: (x[1], x[2])) \
                           .keyBy(lambda x: (x[0], fonk6(x[1])))
    b8.join(b7) \
              .map(lambda key, (key2, info): tuple(info)) \
              .distinct() \
              .saveAsTextFile(b6)
def fonk4(item, size):
    return len(item) == size
def fonk5(title, b9):
    return bool(title) and len(b9) == 4
def fonk6(item):
    try:
        b9 = int(re.findall(r'\d{4}', item).pop())
    except Exception as e:
        return 0
    return b9
def fonk7(b10):
    return eval(b10)
def fonk8(b10):
    b10 = b10.split('|')
    b11 = [x.strip() for x in b10]
    return b11
if b12 = = '__main__':
    fonk1()