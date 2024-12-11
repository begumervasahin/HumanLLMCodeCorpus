from pyspark import SparkConf, SparkContext
import sys
import omdb
import csv
import re
from variables import MACHINE, VUID, PAGE_TABLE, INDEX_TABLE, COLUMN_FAMILY, COLUMN
b1 = 'hdfs:
b2 = 'hdfs:
b3 = 'hdfs:
def fonk1(b10):
    b4 = b10.textFile(b3)
    b5 = b10.textFile(b1)
    b4 = b4.map(get_imdb_fields)\
                         .filter(lambda x: fonk2(x, 5))\
                         .keyBy(lambda x: (x[0], fonk5(x[1])))
    b5 = b5.map(get_fields)\
                           .filter(lambda x: fonk3(x[1], x[2]))\
                           .map(lambda x: (x[1], x[2]))\
                           .keyBy(lambda x: (x[0], fonk5(x[1])))
    b5.join(b4)\
              .map(lambda key, (key2, info): tuple(info))\
              .distinct()\
              .saveAsTextFile(b2)
def fonk2(item, size):
    return len(item) == size
def fonk3(b6, b7):
    return not (b6 = = "" or len(b7) != 4)
def fonk4(item):
    if not item[1]:
        return 0
    if item[1][1] in movie_awards:
        return 2
    else:
        assert item[1][1] in actor_awards
        return 1
def fonk5(item):
    try:
        b7 = int(re.findall(r'\d{4}', item).pop())
    except Exception as e:
        return 0
    return b7
if b8 = = '__main__':
    b9 = SparkConf()
    if sys.argv[1] == 'local':
        b9.setMaster("local[3]")
        print('Running locally')
    elif sys.argv[1] == 'cluster':
        b9.setMaster("b10:
        print('Running on cluster')
    b9.set("b10.executor.memory", "10g")
    b9.set("b10.driver.memory", "10g")
    b10 = SparkContext(b9=b9)
    fonk1(b10)