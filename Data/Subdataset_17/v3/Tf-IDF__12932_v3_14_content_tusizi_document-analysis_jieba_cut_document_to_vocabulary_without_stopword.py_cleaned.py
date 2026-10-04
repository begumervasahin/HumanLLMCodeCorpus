import json
import jieba
from pyspark import SparkContext
sc = SparkContext(appName='CutDocument')
def encode_text(text):
    return text.encode("utf-8")
def cut_and_encode(text):
    segmented_list = jieba.cut(text, cut_all=False)
    filtered_list = [seg for seg in segmented_list if seg != ""]
    encoded_list = [encode_text(seg) for seg in filtered_list]
    return encoded_list
def write_to_file(items):
    output_file = "/vagrant/result/jieba_cut_word.txt"
    with open(output_file, "a+", encoding="utf-8") as file:
        file.write(" ".join(items) + "\n")
def filter_stop_words(word_list, stop_words):
    return [word for word in word_list if word not in stop_words]
def main():
    source_file = '/vagrant/data/data.txt'
    content_rdd = sc.textFile(source_file).map(lambda x: json.loads(x)['content'])
    stop_words = sc.textFile("stop_words.txt").map(lambda x: x.encode("utf-8")).collect()
    cut_word_rdd = content_rdd.map(cut_and_encode)
    filtered_rdd = cut_word_rdd.map(lambda word_list: filter_stop_words(word_list, stop_words))
    filtered_rdd.foreach(write_to_file)
if __name__ == "__main__":
    main()