from pyspark import SparkConf, SparkContext
import sys
import re
b1 = 'hdfs:
b2 = 'hdfs:
b3 = 'hdfs:
def fonk1(b8):
    b4 = b8.textFile(b3)
    b5 = b8.textFile(b1)
    b4 = (b4.map(get_imdb_fields)
                           .filter(lambda x: len(x) == 5)
                           .keyBy(lambda x: (x[0], fonk3(x[1]))))
    b5 = (b5.map(get_fields)
                             .filter(lambda x: fonk2(x[1], x[2]))
                             .map(lambda x: (x[1], x[2]))
                             .keyBy(lambda x: (x[0], fonk3(x[1]))))
    (b5.join(b4)
               .map(lambda key_info: tuple(key_info[1][1]))
               .distinct()
               .saveAsTextFile(b2))
def fonk2(title, year):
    return title != "" and len(year) == 4
def fonk3(item):
    try:
        return int(re.findall(r'\d{4}', item).pop())
    except Exception:
        return 0
def fonk4(text):
    return eval(text)
def fonk5(text):
    return [x.strip() for x in text.split('|')]
if b6 = = '__main__':
    b7 = SparkConf()
    if len(sys.argv) > 1:
        if sys.argv[1] == 'local':
            b7.setMaster("local[3]")
            print('Running locally')
        elif sys.argv[1] == 'cluster':
            b7.setMaster("b8:
            print('Running on cluster')
    b7.set("b8.executor.memory", "10g")
    b7.set("b8.driver.memory", "10g")
    b8 = SparkContext(b7=b7)
    fonk1(b8)