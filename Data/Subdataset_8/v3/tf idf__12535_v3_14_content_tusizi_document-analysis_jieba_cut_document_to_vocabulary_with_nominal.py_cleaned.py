import json
import jieba.posseg as pseg
from pyspark import SparkContext
sc = SparkContext(appName='CutDocument')
def tokenize_text(text):
    tokens_with_flags = pseg.cut(text)
    allowed_pos = ["n", "nr", "nr1", "nr2", "nrj", "nrf", "ns", "nsf", "nt", "nz", "nl", "ng", "s", "f", "v", "vd", "vn", "vf",
                   "vx", "vi", "vl", "vga", "ad", "an", "ag", "al"]
    filtered_tokens = [token.word.encode("utf-8") for token in tokens_with_flags if token.flag in allowed_pos]
    return filtered_tokens
def write_tokens_to_file(tokens):
    output_file = "/vagrant/vocabulary/mominal.txt"
    tokens_string = " ".join(tokens)
    with open(output_file, "a+") as file:
        file.write(tokens_string + "\n")
def filter_stop_words(tokens):
    return [token for token in tokens if token not in stop_word_list]
source_file = '/vagrant/data/data.txt'
text_rdd = sc.textFile(source_file).map(lambda x: json.loads(x)['content'])
stop_word_list = sc.textFile("stop_words.txt").map(lambda word: word.encode("utf-8")).collect()
result = text_rdd.flatMap(tokenize_text).filter(filter_stop_words).foreachPartition(write_tokens_to_file)
sc.stop()