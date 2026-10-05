import re
from nltk.stem import PorterStemmer
def extract_data(filepath, stop_words):
    ps = PorterStemmer()
    total_doc = ""
    final_word_list = []
    doc_num_list = []
    with open(filepath) as file:
        lines = file.readlines()
    for line in lines:
        striped_string = line.strip() + " "
        total_doc += striped_string
        if "<DOCNO>" in striped_string:
            doc_num = re.search(r'<DOCNO>(.*?)</DOCNO>', striped_string).group(1)
            doc_num_list.append(doc_num)
    total_text = re.findall(r'<TEXT>(.*?)</TEXT>', total_doc)
    for text in total_text:
        text = re.sub(r'\W+|\d+', ' ', text).lower()
        word_list = text.split()
        word_list = [word for word in word_list if word not in stop_words]
        stemmed_list = [ps.stem(word) for word in word_list if word]
        final_word_list.extend(stemmed_list)
    return final_word_list, doc_num_list
stop_words = ["the", "and", "is", "in", "it", "on"]
file_path = "sample.txt"
final_words, doc_numbers = extract_data(file_path, stop_words)
print("Final Word List:", final_words)
print("Doc Number List For Each File:", doc_numbers)