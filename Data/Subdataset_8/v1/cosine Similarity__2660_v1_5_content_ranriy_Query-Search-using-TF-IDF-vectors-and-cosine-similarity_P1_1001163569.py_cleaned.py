import os
import math
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
nltk.download('punkt')
nltk.download('stopwords')
corpusroot = './presidential_debates'
tokenizer = RegexpTokenizer(r'[a-zA-Z]+')
removewords = stopwords.words('english')
stemmer = PorterStemmer()
df = {}
list_logfreq = []
idf = {}
N = 30
index = 0
docmap = []
def calculate_idf():
    for terms, value in df.items():
        idf[terms] = math.log(N / value, 10)
def calculate_doc_weight(docno):
    weight = {}
    for keys, value in list_logfreq[docno].items():
        weight[keys] = value * idf[keys]
    return weight
def calculate_doc_length(doc_weight):
    return sum(i ** 2 for i in doc_weight.values()) ** 0.5
def calculate_normalized_doc_weight(docno):
    finalweight = {}
    for keys, value in list_weight[docno].items():
        finalweight[keys] = value / length[docno]
    return finalweight
def get_idf(token):
    return idf.get(token, -1)
def get_weight(filename, token):
    p = docmap.index(filename)
    idfreq = get_idf(token)
    dict_weight = list_logfreq[p]
    if token in dict_weight:
        tfreq = dict_weight[token]
        weight = (tfreq * idfreq) / length[p]
        return weight
    else:
        return 0
def sorted_posting_list(term):
    try:
        d = {x: y for x, y in zip(posting_list[term][::2], posting_list[term][1::2])}
        sorted_docs = sorted(d, key=d.get, reverse=True)
        return sorted_docs[:10]
    except KeyError:
        return []
def execute_query(query_string):
    query_string = query_string.lower()
    tokens = tokenizer.tokenize(query_string)
    new_query = [word for word in tokens if word not in removewords]
    stem_query = [stemmer.stem(word) for word in new_query]
    tf_query = {}
    for word in stem_query:
        tf_query[word] = tf_query.get(word, 0) + 1
    query_log_frequency = {keys: 1 + math.log(value, 10) for keys, value in tf_query.items()}
    query_length = (sum(i ** 2 for i in query_log_frequency.values())) ** 0.5
    normalized_query_weight = {keys: value / query_length for keys, value in query_log_frequency.items()}
    query_tokens = [sorted_posting_list(word) for word in query_log_frequency.keys()]
    intersection = query_tokens[0]
    for token in query_tokens:
        intersection = [x for x in token if x in set(intersection)]
    if not intersection:
        return 'None', 0
    score_list = []
    for document in intersection:
        score = sum(normalized_query_weight[word] * list_finalweight[document].get(word, 0) for word in query_log_frequency.keys())
        score_list.append(score)
    max_score = max(score_list)
    max_index = score_list.index(max_score)
    position = intersection[max_index]
    return docmap[position], max_score
for filename in os.listdir(corpusroot):
    with open(os.path.join(corpusroot, filename), "r", encoding='UTF-8') as file:
        docmap.append(filename)
        doc = file.read().lower()
        tokens = tokenizer.tokenize(doc)
        new_doc = [word for word in tokens if word not in removewords]
        stem_doc = [stemmer.stem(word) for word in new_doc]
        tf = {word: stem_doc.count(word) for word in stem_doc}
        log_frequency = {keys: 1 + math.log(value, 10) for keys, value in tf.items()}
        list_logfreq.append(log_frequency)
        for terms in tf.keys():
            if terms not in df:
                df[terms] = 1
            else:
                df[terms] += 1
calculate_idf()
list_weight = [calculate_doc_weight(i) for i in range(index)]
length = [calculate_doc_length(list_weight[i]) for i in range(index)]
list_finalweight = [calculate_normalized_doc_weight(i) for i in range(index)]
posting_list = {}
for docno in range(index):
    for key, value in list_finalweight[docno].items():
        posting_list.setdefault(key, []).extend([docno, value])
def main():
    while True:
        query_string = input("Enter your query (or 'exit' to quit): ")
        if query_string.lower() == 'exit':
            break
        else:
            result = execute_query(query_string)
            print(f"Document: {result[0]}, Score: {result[1]}")
if __name__ == "__main__":
    main()