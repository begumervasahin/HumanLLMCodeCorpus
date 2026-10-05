import re
from nltk.stem import PorterStemmer
def extract_data(filepath, stop_words):
    ps = PorterStemmer()
    total_doc = ""
    final_word_list = []
    doc_num_list = []
    with open(filepath) as file:
        for line in file:
            striped_string = line.strip() + " "
            total_doc += striped_string
            if "<DOCNO>" in striped_string:
                doc_num = re.search(r'<DOCNO>(.*?)</DOCNO>', striped_string).group(1)
                doc_num_list.append(doc_num)
    total_text = re.findall(r'<TEXT>(.*?)</TEXT>', total_doc)
    for text in total_text:
        text = str(text).strip()
        text = re.sub(r'\w*-*\d+-*\w*', " ", text)
        text = re.sub(r'\d+', " ", text)
        text = re.sub(r'\W+', " ", text)
        lowercase_text = text.lower()
        word_list = re.split('\s+', lowercase_text)
        word_list = [word for word in word_list if word not in stop_words]
        stemmed_list = [ps.stem(word) for word in word_list if word]
        final_word_list.extend(stemmed_list)
    return final_word_list, doc_num_list