from pyspark import SparkConf, SparkContext
from operator import add
import re
import sys
class WordCountApp:
    def __init__(self):
        self.conf = SparkConf().setAppName('Part 1: Word Count Per Book') \
                               .set('spark.executor.memory', '2g') \
                               .set('spark.ui.port', 6200)
        self.sc = SparkContext(conf=self.conf)
    def process_file(self, document_and_contents):
        document = document_and_contents[0].split('/')[-1]
        word_list = re.compile('\w+').findall(document_and_contents[1])
        return map(lambda word: ((str(document), str(word.lower())), 1), word_list)
    def main(self, input_file, output_file):
        whole_text_files_rdd = self.sc.wholeTextFiles(input_file)
        whole_text_files_rdd.cache()
        word_count = whole_text_files_rdd.flatMap(self.process_file) \
                                         .reduceByKey(add, numPartitions=1) \
                                         .sortByKey()
        word_count.saveAsTextFile(output_file)
if __name__ == '__main__':
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    word_count_app = WordCountApp()
    word_count_app.main(input_file, output_file)