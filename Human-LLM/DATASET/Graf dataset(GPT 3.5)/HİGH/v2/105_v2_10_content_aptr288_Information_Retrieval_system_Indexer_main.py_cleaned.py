import os
import re
import time
import math
import pathlib
import collections
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
    TextList, b14 = extractingdata(b13, b9)
    b11.extend(TextList)
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
for b39, value in b17.items():
    for innerkey, innervalue in value.items():
        if b18[innerkey] == {}:
            b18[innerkey] = {b39: innervalue}
        else:
            b18[innerkey][b39] = innervalue
b4 = {b39: {innerkey: value for innerkey, value in sorted(idx.items())} for b39, idx in b17.items()}
b3 = {b39: {innerkey: value for innerkey, value in sorted(idx.items())} for b39, idx in b18.items()}
b19 = len(b4)
for b39, value in b4.items():
    b20 = sum(pow(value[inner_key] * math.log(b19 / len(b3[inner_key]), 10), 2) for inner_key in value)
    b5[b39] = math.sqrt(b20)
b21 = []
with open(b7 / 'files' / 'topics.txt', "r+") as fp:
    b22 = fp.read()
    for match in re.finditer(r'<num>.*?([0-9]+)', b22):
        b21.append(match.group(1))
b23 = re.findall(r'<title>(.*?)<desc>', b22)
b24 = re.findall(r'<desc> b24:(.*?)<narr>', b22)
b25 = re.findall(r'<narr> b25:(.*?)</top>', b22)
b26 = []
with open(b7 / 'files' / 'main.qrels') as fp:
    b26 = [line.strip().split(" ") for line in fp if "FT911" in line.strip().split("-")[0]]
def fonk1(score_calculated, query_number_to_evaluate_on):
    b27 = [doc for doc in b26 if doc[0] == query_number_to_evaluate_on]
    b28 = set(int(doc[2].split("-")[1]) for doc in b27 if doc[3] == '1')
    b29 = len(score_calculated)
    b30 = sum(1 for doc_id in score_calculated.keys() if doc_id in b28)
    b31 = sum(1 for doc_id in score_calculated.keys() if doc_id in b28)
    b32 = b31 / b29 if b29 != 0 else 0
    b33 = b31 / b30 if b30 != 0 else 0
    score_calculated.clear()
    return b32, b33
with open("files/OnlyTitleResults.txt", "w") as queryResults:
    b19 = len(b4)
    b6.clear()
    a1 = 0
    b34 = extractDifferentQuery(b23, b9)
    for query_num, query_terms in b34.items():
        for query_term, tf_query in query_terms.items():
            b35 = b2.get(query_term, 0)
            if b35 != 0:
                b36 = len(b3[b35])
                for doc_id, tf_doc in b3[b35].items():
                    b37 = math.log(b19 / b36, 10)
                    b38 = ((tf_doc * b37) * (tf_query * b37))
                    b6[doc_id] += (b38 / b5[doc_id])
        a2 = 1
        for doc_id, score_value in sorted(b6.items(), b39 = lambda x: x[1], reverse=True):
            queryResults.write(f"{b21[a1]}        FT911-{doc_id}        {a2}        {score_value:.15f}\n")
            a2 += 1
        b32, b33 = fonk1(b6, b21[a1])
        queryResults.write(f"  b40 = =>  {b32}  Recall ==>  {b33}\n")
        a1 += 1