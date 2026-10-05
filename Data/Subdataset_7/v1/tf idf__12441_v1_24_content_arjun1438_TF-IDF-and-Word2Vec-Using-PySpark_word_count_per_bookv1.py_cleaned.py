from pyspark import SparkConf, SparkContext
from operator import add
import re
import sys
class class1:
    def fonk1(self, documentAndContents):
        b1 = documentAndContents[0].split('/')[-1]
        b2 = re.compile('\w+').findall(documentAndContents[1])
        return map(lambda word: ((str(b1), str(word.lower())), 1), b2)
    def fonk2(self, b7, b8, b9):
        b3 = b7.wholeTextFiles(b8)
        b3.cache()
        b4 = b3.flatMap(self.processFile).reduceByKey(add, numPartitions=1).sortByKey()
        b4.saveAsTextFile(b9)
if b5 = = '__main__':
    if len(sys.argv) != 3:
        print("Usage: python script.py <b8> <output_directory>")
        sys.exit(1)
    b6 = SparkConf().setAppName('Part 1: Word Count Per Book').set('spark.executor.memory', '2g').set('spark.ui.port', 6200)
    b7 = SparkContext(b6=b6)
    b8 = sys.argv[1]
    b9 = sys.argv[2]
    b10 = class1()
    b10.fonk2(b7, b8, b9)