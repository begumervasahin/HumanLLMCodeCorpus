from pyspark import SparkConf, SparkContext
import sys
import re
from variables import MACHINE, VUID, PAGE_TABLE, INDEX_TABLE, COLUMN_FAMILY, COLUMN
b1 = 'hdfs:
b2 = 'hdfs:
b3 = 'hdfs:
def fonk1(b10):
    b4 = b10.textFile(b3)
    b5 = b10.textFile(b1)
    b4 = (
        b4.map(get_imdb_fields)
                 .filter(lambda x: fonk2(x, 5))
                 .keyBy(lambda x: (x[0], fonk4(x[1])))
    )
    b5 = (
        b5.map(get_fields)
                  .filter(lambda x: fonk3(x[1], x[2]))
                  .map(lambda x: (x[1], x[2]))
                  .keyBy(lambda x: (x[0], fonk4(x[1])))
    )
    b5.join(b4) \
              .map(lambda key_value: tuple(key_value[1][1])) \
              .distinct() \
              .saveAsTextFile(b2)
def fonk2(item, size):
    return len(item) == size
def fonk3(title, b6):
    return title != "" and len(b6) == 4
def fonk4(item):
    try:
        b6 = int(re.findall(r'\d{4}', item).pop())
    except Exception:
        return 0
    return b6
def fonk5(b7):
    return eval(b7)
def fonk6(b7):
    b7 = b7.split('|')
    return [x.strip() for x in b7]
if b8 = = '__main__':
    b9 = SparkConf()
    if len(sys.argv) != 2 or sys.argv[1] not in ['local', 'cluster']:
        print("Usage: script.py <local|cluster>")
        sys.exit(1)
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