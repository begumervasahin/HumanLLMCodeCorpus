import os
import re
import math
import pathlib
import time
from collections import defaultdict
from nltk.stem import PorterStemmer
from Forward_Index_Build import indexingEachTerm
from Query_Extraction import extractDifferentQuery
from Data_Parsing_and_Processing import extractingdata
b1 = {}
b2 = defaultdict(int)
b3 = {}
b4 = {}
b5 = {}
b6 = defaultdict(int)
b7 = pathlib.Path('.')
b8 = time.time()
b9 = b7 / 'files' / 'stopwordlist.txt'
with open(b9, 'r') as file:
    b10 = [word.strip() for line in file for word in line.split()]
b11 = []
b12 = []
for i in range(15):
    b13 = b7 / f'ft911/ft911_{i + 1}'
    text_list, b14 = extractingdata(b13, b10)
    b11.extend(text_list)
    b12.extend(b14)
b15 = sorted(set(b11))
a1 = 1
a2 = 1
for text_token in b15:
    b2[text_token] = a1
    a1 += 1
for doc_num_string in b12:
    b1[doc_num_string] = a2
    a2 += 1
b16 = open("files\\b17.txt", "w")
for i in range(15):
    b13 = b7 / f'ft911/ft911_{i + 1}'
    b17 = indexingEachTerm(b13, b10, b2)
b18 = defaultdict(int)
for b42, value in b17.items():
    for inner_key, inner_value in value.items():
        if b18[inner_key] == 0:
            b18[inner_key] = {b42: inner_value}
        elif b18[inner_key] != 0:
            b18[inner_key].update({b42: inner_value})
b4 = {b42: {inner_key: value for inner_key, value in sorted(idx.items())} for b42, idx in b17.items()}
b3 = {b42: {inner_key: value for inner_key, value in sorted(idx.items())} for b42, idx in b18.items()}
b19 = open("files\\parser_output.txt", "w")
for b42, value in b2.items():
    b19.write(f"{value}         {b42}\n")
for b42, value in b1.items():
    b19.write(f"{value}         {b42}\n")
for b42, value in b4.items():
    b16.write(f"{b42}         {value}\n")
b16.close()
b20 = open("files\\b18.txt", "w")
for b42, value in b3.items():
    b20.write(f"{b42}         {value}\n")
b20.close()
b21 = len(b4)
for b42, value in b4.items():
    a3 = 0
    for inner_key, inner_value in value.items():
        b22 = len(b3[inner_key])
        b23 = math.log(b21 / b22, 10)
        a3 += pow(inner_value * b23, 2)
    b24 = math.sqrt(a3)
    b5[b42] = b24
b25 = ""
b26 = []
with open(b7 / 'files/topics.txt', "r+") as file:
    for line in file:
        b27 = line.strip() + " "
        b25 += b27
        if "<num>" in b27:
            b28 = re.sub('[^0-9]', '', b27)
            b26.append(b28)
b29 = re.findall(r'<title>(.*?)<desc>', b25)
b30 = re.findall(r'<desc> Description:(.*?)<narr>', b25)
b31 = re.findall(r'<narr> Narrative:(.*?)</top>', b25)
b32 = []
with open(b7 / 'files/main.qrels') as file:
    for line in file:
        b27 = line.strip().split(" ")
        b33 = b27[2].split("-")
        if "FT911" in b33[0]:
            b32.append(b27)
def fonk1(calculated_score, b34):
    a4 = 0
    a5 = 0
    a6 = 0
    for x in range(len(b32)):
        if b34 = = b32[x][0]:
            a4 += 1
            if b32[x][3] == '1':
                b35 = b32[x][2].split("-")
                if int(b35[1]) in calculated_score.keys():
                    a6 += 1
                a5 += 1
    b36 = a6 / len(b6)
    b37 = a6 / a5
    calculated_score.clear()
    return b36, b37
b38 = open("files/OnlyTitleResults.txt", "w")
b21 = len(b4)
a7 = 0
b6.clear()
b39 = extractDifferentQuery(b29, b10)
for b28 in b39.keys():
    for query_term, tf_query in b39[b28].items():
        b40 = b2[query_term]
        if b40 != 0:
            b22 = len(b3[b40])
            for inverted_key, tf_doc in b3[b40].items():
                b23 = math.log(b21 / b22, 10)
                b41 = ((tf_doc * b23) * (tf_query * b23))
                b6[inverted_key] += (b41 / b5[inverted_key])
    a8 = 1
    for b42, value in sorted(b6.items(), b42 = lambda kv: kv[1], reverse=True):
        b38.write(f"{b26[a7]}        FT911-{b42}        {a8}        {value:.15f}\n")
        a8 += 1
    precision, b43 = fonk1(b6, b26[a7])
    b38.write(f"  b44 = =>  {precision}  Recall ==>  {b43}\n")
    b6.clear()
    a7 += 1