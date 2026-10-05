from pyspark import SparkConf, SparkContext
import sys
import re
def fonk1(b12):
    b1 = 'hdfs:
    b2 = 'hdfs:
    b3 = 'hdfs:
    b4 = b12.textFile(b2)
    b5 = b12.textFile(b1)
    b4 = b4.map(parse_imdb_fields) \
                         .filter(lambda x: fonk2(x, 5)) \
                         .keyBy(lambda x: (x[0], fonk4(x[1])))
    b5 = b5.map(parse_movie_fields) \
                           .filter(lambda x: fonk3(x[1], x[2])) \
                           .map(lambda x: (x[1], x[2])) \
                           .keyBy(lambda x: (x[0], fonk4(x[1])))
    b5.join(b4) \
              .map(lambda key, (key2, info): tuple(info)) \
              .distinct() \
              .saveAsTextFile(b3)
def fonk2(item, size):
    return len(item) == size
def fonk3(b6, b7):
    return not (b6 = = "" or len(b7) != 4)
def fonk4(item):
    try:
        b7 = int(re.findall(r'\d{4}', item).pop())
    except Exception as e:
        return 0
    return b7
def fonk5(b8):
    return eval(b8)
def fonk6(b8):
    b8 = b8.split('|')
    b9 = [x.strip() for x in b8]
    return b9
if b10 = = '__main__':
    b11 = SparkConf()
    if sys.argv[1] == 'local':
        b11.setMaster("local[3]")
        print('Running locally')
    elif sys.argv[1] == 'cluster':
        b11.setMaster("b12:
        print('Running on cluster')
    b11.set("b12.executor.memory", "10g")
    b11.set("b12.driver.memory", "10g")
    b12 = SparkContext(b11=b11)
    fonk1(b12)