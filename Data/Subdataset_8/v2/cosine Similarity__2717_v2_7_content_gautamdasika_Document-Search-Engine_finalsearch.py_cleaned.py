import nltk
import math
import os
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from math import log10, sqrt
from collections import Counter
nltk.download('stopwords')
stemmer = PorterStemmer()
tokenizer = RegexpTokenizer(r'[a-zA-Z]+')
corpus_root = './presidential_debates'
vectors = {}
df = Counter()
tfs = {}
lengths = Counter()
postings_list = {}
def calculate_weight(filename, token):
    idf = get_inverse_document_frequency(token)
    return (1 + log10(tfs[filename][token])) * idf
def get_inverse_document_frequency(token):
    if df[token] == 0:
        return -1
    return log10(len(tfs) / df[token])
for filename in os.listdir(corpus_root):
    with open(os.path.join(corpus_root, filename), "r", encoding='UTF-8') as file:
        doc = file.read().lower()
        tokens = tokenizer.tokenize(doc)
        sw = set(stopwords.words('english'))
        tokens = [stemmer.stem(token) for token in tokens if token not in sw]
        tf = Counter(tokens)
        df += Counter(list(set(tokens)))
        tfs[filename] = tf.copy()
        tf.clear()
for filename in tfs:
    vectors[filename] = Counter()
    length = 0
    for token in tfs[filename]:
        weight = calculate_weight(filename, token)
        vectors[filename][token] = weight
        length += weight ** 2
    lengths[filename] = math.sqrt(length)
for filename in vectors:
    for token in vectors[filename]:
        vectors[filename][token] = vectors[filename][token] / lengths[filename]
        if token not in postings_list:
            postings_list[token] = Counter()
        postings_list[token][filename] = vectors[filename][token]
def get_weight(filename, token):
    return vectors[filename][token]
def query(qstring):
    qstring = qstring.lower()
    qtf = {}
    qlength = 0
    flag = 0
    loc_docs = {}
    tenth = {}
    cos_sims = Counter()
    for token in qstring.split():
        token = stemmer.stem(token)
        if token not in postings_list:
            continue
        if get_inverse_document_frequency(token) == 0:
            loc_docs[token], weights = zip(*postings_list[token].most_common())
        else:
            loc_docs[token], weights = zip(*postings_list[token].most_common(10))
        tenth[token] = weights[9]
        if flag == 1:
            commondocs = set(loc_docs[token]) & commondocs
        else:
            commondocs = set(loc_docs[token])
            flag = 1
        qtf[token] = 1 + log10(qstring.count(token))
        qlength += qtf[token] ** 2
    qlength = sqrt(qlength)
    for doc in vectors:
        cos_sim = 0
        for token in qtf:
            if doc in loc_docs[token]:
                cos_sim += (qtf[token] / qlength) * postings_list[token][doc]
            else:
                cos_sim += (qtf[token] / qlength) * tenth[token]
        cos_sims[doc] = cos_sim
    max = cos_sims.most_common(1)
    ans, wght = zip(*max)
    try:
        if ans[0] in commondocs:
            return ans[0], wght[0]
        else:
            return "fetch more", 0
    except UnboundLocalError:
        return "None", 0
print("(%s, %.12f)" % query("health insurance wall street"))
print("(%s, %.12f)" % query("security conference ambassador"))
print("(%s, %.12f)" % query("particular constitutional amendment"))
print("(%s, %.12f)" % query("terror attack"))
print("(%s, %.12f)" % query("vector entropy"))