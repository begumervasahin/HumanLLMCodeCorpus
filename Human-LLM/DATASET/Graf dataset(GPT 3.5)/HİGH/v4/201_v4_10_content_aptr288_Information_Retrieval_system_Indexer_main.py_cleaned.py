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
b4 = PorterStemmer()
b5 = {}
b6 = {}
b7 = {}
b8 = defaultdict(int)
b9 = pathlib.Path('.')
b10 = time.time()
b11 = []
b12 = b9 / 'files' / 'stopwordlist.txt'
with open(b12, 'r') as f:
    b11.extend(word.strip() for line in f for word in line.split())
b13 = []
b14 = []
for i in range(15):
    b15 = b9 / f'ft911/ft911_{i + 1}'
    TextList, b16 = extractingdata(b15, b11)
    b13.extend(TextList)
    b14.extend(b16)
b17 = list(set(b13))
b18 = sorted(b17)
a1 = 1
a2 = 1
for textToken in b18:
    b2[textToken] = a1
    a1 += 1
for DocNumString in b14:
    b1[DocNumString] = a2
    a2 += 1
b19 = open("files\\forward_index.txt", "w")
for i in range(15):
    b15 = b9 / f'ft911/ft911_{i + 1}'
    b20 = indexingEachTerm(b15, b11, b2)
b21 = defaultdict(int)
for b45, value in b20.items():
    for innerkey, innervalue in value.items():
        if b21[innerkey] == 0:
            b21[innerkey] = {b45: innervalue}
        elif b21[innerkey] != 0:
            b21[innerkey].update({b45: innervalue})
b6 = {b45: {innerkey: value for innerkey, value in sorted(idx.items())} for b45, idx in b20.items()}
b5 = {b45: {innerkey: value for innerkey, value in sorted(idx.items())} for b45, idx in b21.items()}
b22 = open("files\\parser_output.txt", "w")
for b45, value in b2.items():
    b22.write(f"{value}         {b45}\n")
for b45, value in b1.items():
    b22.write(f"{value}         {b45}\n")
for b45, value in b6.items():
    b19.write(f"{b45}         {value}\n")
b19.close()
b23 = open("files\\inverted_index.txt", "w")
for b45, value in b5.items():
    b23.write(f"{b45}         {value}\n")
b23.close()
b24 = len(b6)
for b45, value in b6.items():
    a3 = 0
    for innerkey, innervalue in value.items():
        b25 = len(b5[innerkey])
        b26 = math.log(b24 / b25, 10)
        a3 += pow(innervalue * b26, 2)
    b27 = math.sqrt(a3)
    b7[b45] = b27
b28 = ""
b29 = []
with open(b9 / 'files/topics.txt', "r+") as fp:
    for line in fp:
        b30 = line.strip() + " "
        b28 += b30
        if "<num>" in b30:
            b31 = re.sub('[^0-9]', '', b30)
            b29.append(b31)
b32 = re.findall(r'<title>(.*?)<desc>', b28)
b33 = re.findall(r'<desc> b33:(.*?)<narr>', b28)
b34 = re.findall(r'<narr> b34:(.*?)</top>', b28)
b35 = []
with open(b9 / 'files/main.qrels') as fp:
    for line in fp:
        b30 = line.strip().split(" ")
        b36 = b30[2].split("-")
        if "FT911" in b36[0]:
            b35.append(b30)
def fonk1(scorecalculated, b37):
    a4 = 0
    a5 = 0
    a6 = 0
    for x in range(len(b35)):
        if b37 = = b35[x][0]:
            a4 += 1
            if b35[x][3] == '1':
                b38 = b35[x][2].split("-")
                if int(b38[1]) in scorecalculated.keys():
                    a6 += 1
                a5 += 1
    b39 = a6 / len(b8)
    b40 = a6 / a5
    scorecalculated.clear()
    return b39, b40
b41 = open("files/OnlyTitleResults.txt", "w")
b24 = len(b6)
a7 = 0
b8.clear()
b42 = extractDifferentQuery(b32, b11)
for queryNum in b42.keys():
    for queryTerm, tfQ in b42[queryNum].items():
        b43 = b2[queryTerm]
        if b43 != 0:
            b25 = len(b5[b43])
            for inverKey, tfD in b5[b43].items():
                b26 = math.log(b24 / b25, 10)
                b44 = ((tfD * b26) * (tfQ * b26))
                b8[inverKey] += (b44 / b7[inverKey])
    a8 = 1
    for b45, value in sorted(b8.items(), b45 = lambda kv: kv[1], reverse=True):
        b41.write(f"{b29[a7]}        FT911-{b45}        {a8}        {value:.15f}\n")
        a8 += 1
    prec, b46 = fonk1(b8, b29[a7])
    b41.write(f"  b47 = =>  {prec}  Recall ==>  {b46}\n")
    b8.clear()
    a7 += 1