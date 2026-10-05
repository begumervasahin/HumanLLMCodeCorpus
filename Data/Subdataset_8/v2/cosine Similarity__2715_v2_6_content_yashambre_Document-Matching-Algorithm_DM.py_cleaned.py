import os
import math
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from collections import Counter
def getidf(token):
    if any(x.isupper() for x in token):
        return -1.0000
    if token in DocFreq:
        return DocFreq[token]
    else:
        return -1.0000
def getqvec(qstring):
    Qtoken_para = []
    token = RegexpTokenizer(r'[a-zA-Z]+')
    Qtoken_para = token.tokenize(qstring.lower())
    stop_words = set(stopwords.words('english'))
    Querystopw = [wor for wor in Qtoken_para if wor not in stop_words]
    QstemmedData = [Qstemmer.stem(s) for s in Querystopw]
    QueryTOkF = {wor: 1 + math.log(QstemmedData.count(wor), 10) for wor in QstemmedData}
    N = len(stemmedData)
    QueryDocFreq = {}
    for wor, freq in QueryTOkF.items():
        freq = 0
        for para, t in TF.items():
            if wor in TF[para].keys():
                freq += 1
        QueryDocFreq[wor] = math.log(N / freq, 10) if freq > 0 else 0
    QueryWT = {lett: QueryTOkF[lett] * QueryDocFreq[lett] for lett in QstemmedData}
    sum_sq = sum(QueryWT[lett] ** 2 for lett in QueryWT)
    QueryWT_norm = {lett: QueryWT[lett] / math.sqrt(sum_sq) for lett in QueryWT}
    return QueryWT_norm
def query(query_string):
    QueryWT = getqvec(query_string)
    QuerySimilarity = {}
    for para in WT.keys():
        sum_sim = sum(QueryWT[key] * WT[para].get(key, 0) for key in QueryWT)
        QuerySimilarity[para] = sum_sim
    max_similarity_value = max(QuerySimilarity.values())
    max_similarity_value_key = max(QuerySimilarity, key=QuerySimilarity.get)
    if max_similarity_value == 0:
        return "NO MATCH\n", max_similarity_value
    else:
        return debate_transcript[max_similarity_value_key], max_similarity_value
stop_words = set(stopwords.words('english'))
filename = './debate.txt'
file = open(filename, "r", encoding='UTF-8')
doc = file.readlines()
file.close()
debate_transcript = {}
token = RegexpTokenizer(r'[a-zA-Z]+')
for k in doc:
    if not k.isspace():
        tok = token.tokenize(k.lower())
        stopw = [token for token in tok if token not in stop_words]
        stemmedData = [PorterStemmer().stem(key) for key in stopw]
        debate_transcript["para " + str(len(debate_transcript) + 1)] = stemmedData
TF = {para: Counter(data) for para, data in debate_transcript.items()}
N = len(debate_transcript)
DocFreq = {token: math.log(N / sum(1 for data in debate_transcript.values() if token in data), 10) for token in set(token for data in debate_transcript.values() for token in data)}
WT = {para: {token: TF[para][token] * DocFreq[token] for token in TF[para]} for para in debate_transcript}
for para in WT:
    sum_weights = math.sqrt(sum(weight ** 2 for weight in WT[para].values()))
    WT[para] = {token: weight / sum_weights for token, weight in WT[para].items()}
query_string = "What are the benefits of renewable energy?"
result, similarity_score = query(query_string)
print("Most similar paragraph:")
print(result)
print("Similarity score:", similarity_score)