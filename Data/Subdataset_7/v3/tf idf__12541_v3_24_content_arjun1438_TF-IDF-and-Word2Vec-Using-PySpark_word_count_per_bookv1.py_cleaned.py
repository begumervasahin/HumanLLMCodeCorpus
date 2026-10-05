from pyspark import SparkConf, SparkContext
from operator import add
import re
import sys
class class1:
    def fonk1(self, b1):
        self.b1 = b1
    def fonk2(self, document_path_and_contents):
        document_path, b2 = document_path_and_contents
        b3 = document_path.split('/')[-1]
        b4 = re.findall(r'\w+', b2.lower())
        return [((b3, word), 1) for word in b4]
    def fonk3(self, b8, b9):
        b5 = self.b1.wholeTextFiles(b8).cache()
        b6 = b5.flatMap(self.process_document).reduceByKey(add, numPartitions=1).sortByKey()
        b6.saveAsTextFile(b9)
def fonk4():
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_file> <output_directory>")
        sys.exit(1)
    b7 = SparkConf().setAppName('Word Count Per Document').set('spark.executor.memory', '2g').set('spark.ui.port', 6200)
    b1 = SparkContext(b7=b7)
    b8 = sys.argv[1]
    b9 = sys.argv[2]
    b10 = class1(b1)
    b10.fonk3(b8, b9)
    b1.stop()
if b11 = = '__main__':
    fonk4()