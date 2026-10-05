from pyspark import SparkConf, SparkContext
from operator import add
import re
import sys
class class1:
    def fonk1(self):
        self.b1 = SparkConf().setAppName('Part 1: Word Count Per Book') \
                               .set('spark.executor.memory', '2g') \
                               .set('spark.ui.port', 6200)
        self.b2 = SparkContext(b1=self.b1)
    def fonk2(self, document_and_contents):
        b3 = document_and_contents[0].split('/')[-1]
        b4 = re.compile('\w+').findall(document_and_contents[1])
        return map(lambda word: ((str(b3), str(word.lower())), 1), b4)
    def fonk3(self, b9, b10):
        b5 = self.b2.wholeTextFiles(b9)
        b5.cache()
        b6 = b5.flatMap(self.process_file) \
                                         .reduceByKey(add, b7 = 1) \
                                         .sortByKey()
        b6.saveAsTextFile(b10)
if b8 = = '__main__':
    b9 = sys.argv[1]
    b10 = sys.argv[2]
    b11 = class1()
    b11.fonk3(b9, b10)