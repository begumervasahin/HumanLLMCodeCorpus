from pyspark import SparkConf, SparkContext
from operator import add
import re
import sys
class class1:
    def fonk1(self, documentAndContents):
        b1 = documentAndContents[0].split('/')[-1]
        b2 = re.compile('\w+').findall(documentAndContents[1])
        return map(lambda word: ((str(b1), str(word.lower())),
                   1), b2)
    def fonk2(self, b8, b9, b10):
        b3 = b8.wholeTextFiles(b9)
        b3.cache()
        b4 = \
            b3.flatMap(self.processFile).reduceByKey(add, b5 = 1).sortByKey()
        b4.saveAsTextFile(b10)
if b6 = = '__main__':
    b7 = SparkConf().setAppName('Part 1: Word Count Per Book'
                                  ).set('spark.executor.memory', '2g').set('spark.ui.port', 6200)
    b8 = SparkContext(b7=b7)
    b9 = sys.argv[1]
    b10 = sys.argv[2]
    b11 = class1()
    b11.fonk2(b8, b9, b10)