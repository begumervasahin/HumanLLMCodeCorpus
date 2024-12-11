import os
import re
import math
import pathlib
from collections import defaultdict
from nltk.stem import PorterStemmer
from Data_Parsing_and_Processing import extractingdata
from Forward_Index_Build import indexingEachTerm
from Query_Extraction import extractDifferentQuery
b1 = {}
b2 = defaultdict(int)
b3 = {}
b4 = {}
b5 = {}
b6 = defaultdict(int)
b7 = pathlib.Path('.')
b8 = time.time()
b9 = []
b10 = b7 / 'files' / 'stopwordlist.txt'
with open(b10, 'r') as f:
    b9.extend(word.strip() for line in f for word in line.split())
b11 = []
b12 = []
for i in range(15):
    b13 = b7 / f'ft911/ft911_{i + 1}'
    text_list, b14 = extractingdata(b13, b9)
    b11.extend(text_list)
    b12.extend(b14)
b15 = sorted(set(b11))
for idx, text_token in enumerate(b15, b16 = 1):
    b2[text_token] = idx
for idx, doc_num_string in enumerate(b12, b16 = 1):
    b1[doc_num_string] = idx
b17 = {}
for i in range(15):
    b13 = b7 / f'ft911/ft911_{i + 1}'
    b17.update(indexingEachTerm(b13, b9, b2))
b18 = defaultdict(dict)
for b36, value in b17.items():
    for inner_key, inner_value in value.items():
        if not b18[inner_key]:
            b18[inner_key] = {b36: inner_value}
        else:
            b18[inner_key][b36] = inner_value
b4 = {b36: {inner_key: value for inner_key, value in sorted(idx.items())} for b36, idx in b17.items()}
b3 = {b36: {inner_key: value for inner_key, value in sorted(idx.items())} for b36, idx in b18.items()}
b19 = len(b4)
for b36, value in b4.items():
    b20 = sum(pow(value[inner_key] * math.log(b19 / len(b3[inner_key]), 10), 2) for inner_key in value)
    b5[b36] = math.sqrt(b20)
b21 = []
with open(b7 / 'files' / 'topics.txt', "r+") as fp:
    b22 = fp.read()
    b21 = re.findall(r'<num>.*?([0-9]+)', b22)
b23 = re.findall(r'<b23>(.*?)<desc>', b22)
with open(b7 / 'files' / 'main.qrels') as fp:
    b24 = [line.strip().split(" ") for line in fp if "FT911" in line.strip().split("-")[0]]
def fonk1(score_calculated, query_number_to_evaluate_on):
    b25 = [doc for doc in b24 if doc[0] == query_number_to_evaluate_on and doc[3] == '1']
    b26 = {int(doc[2].split("-")[1]) for doc in b25}
    b27 = len(score_calculated)
    b28 = sum(1 for doc_id in score_calculated.keys() if doc_id in b26)
    b29 = sum(1 for doc_id in score_calculated.keys() if doc_id in b26)
    b30 = b29 / b27 if b27 != 0 else 0
    b31 = b29 / b28 if b28 != 0 else 0
    score_calculated.clear()
    return b30, b31
with open("files/OnlyTitleResults.txt", "w") as query_results:
    b19 = len(b4)
    b6.clear()
    for query_num, query_terms in extractDifferentQuery(b23, b9).items():
        for query_term, tf_query in query_terms.items():
            b32 = b2.get(query_term, 0)
            if b32 != 0:
                b33 = len(b3[b32])
                for doc_id, tf_doc in b3[b32].items():
                    b34 = math.log(b19 / b33, 10)
                    b35 = ((tf_doc * b34) * (tf_query * b34))
                    b6[doc_id] += (b35 / b5[doc_id])
        a1 = 1
        for doc_id, score_value in sorted(b6.items(), b36 = lambda x: x[1], reverse=True):
            query_results.write(f"{query_num}        FT911-{doc_id}        {a1}        {score_value:.15f}\n")
            a1 += 1
        b30, b31 = fonk1(b6, query_num)
        query_results.write(f"  b37 = =>  {b30}  Recall ==>  {b31}\n")