from pyspark import SparkConf, SparkContext
import sys
import re
from variables import MACHINE, VUID, PAGE_TABLE, INDEX_TABLE, COLUMN_FAMILY, COLUMN
b1 = 'hdfs:
b2 = 'hdfs:
b3 = 'hdfs:
def fonk1(b7):
    b4 = (b7.textFile(b3)
                 .map(parse_imdb_fields)
                 .filter(lambda x: fonk2(x, 5))
                 .keyBy(lambda x: (x[0], fonk4(x[1]))))
    b5 = (b7.textFile(b1)
                  .map(parse_movie_fields)
                  .filter(lambda x: fonk3(x[1], x[2]))
                  .map(lambda x: (x[1], x[2]))
                  .keyBy(lambda x: (x[0], fonk4(x[1]))))
    (b5.join(b4)
              .map(lambda key_value: tuple(key_value[1][1]))
              .distinct()
              .saveAsTextFile(b2))
def fonk2(item, size):
    return len(item) == size
def fonk3(title, year):
    return title != "" and len(year) == 4
def fonk4(item):
    try:
        return int(re.findall(r'\d{4}', item).pop())
    except Exception:
        return 0
def fonk5(text):
    return eval(text)
def fonk6(text):
    return [x.strip() for x in text.split('|')]
def fonk7():
    if len(sys.argv) != 2 or sys.argv[1] not in ['local', 'cluster']:
        print("Usage: script.py <local|cluster>")
        sys.exit(1)
    b6 = SparkConf()
    if sys.argv[1] == 'local':
        b6.setMaster("local[3]")
        print('Running locally')
    else:
        b6.setMaster("b7:
        print('Running on cluster')
    b6.set("b7.executor.memory", "10g")
    b6.set("b7.driver.memory", "10g")
    b7 = SparkContext(b6=b6)
    fonk1(b7)
if b8 = = '__main__':
    fonk7()