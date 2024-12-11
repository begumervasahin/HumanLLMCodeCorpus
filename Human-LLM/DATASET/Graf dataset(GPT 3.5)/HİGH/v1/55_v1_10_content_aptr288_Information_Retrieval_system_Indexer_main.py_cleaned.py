import collections
import math
import os
import pathlib
import re
import time
from collections import defaultdict
from nltk.stem import PorterStemmer
from Data_Parsing_and_Processing import extractingdata
from Forward_Index_Build import indexingEachTerm
from Query_Extraction import extractDifferentQuery
b1 = {}
b2 = collections.defaultdict(int)
b3 = {}
b4 = PorterStemmer()
b5 = {}
b6 = {}
b7 = {}
b8 = defaultdict(int)
b9 = pathlib.Path('.')
b10 = time.time()
b11 = []
b12 = str(b9 / 'files' / 'stopwordlist.txt')
with open(b12, 'r') as f:
    for b31 in f:
        for word in b31.split():
            b11.append(word)
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
for i in range(15):
    b15 = b9 / f'ft911/ft911_{i + 1}'
    b19 = indexingEachTerm(b15, b11, b2)
b20 = defaultdict(int)
for b47, value in b19.items():
    for innerkey, innervalue in value.items():
        b21 = {}
        if b20[innerkey] == 0:
            b20[innerkey] = {b47: innervalue}
        elif b20[innerkey] != 0:
            b21 = b20[innerkey]
            b21.update({b47: innervalue})
            b20[innerkey] = b21
for b47, value in b19.items():
    b22 = {}
    for innerkey in sorted(value.items()):
        b22.update({innerkey[0]: value[innerkey[0]]})
    b6.update({b47: b22})
for b47 in sorted(b20.items()):
    b23 = {}
    b24 = b20[b47[0]]
    for innerkey in sorted(b20[b47[0]].items()):
        b23.update({innerkey[0]: b24[innerkey[0]]})
    b5.update({b47[0]: b23})
b25 = len(b6)
for b47, value in b6.items():
    a3 = 0
    for innerkey, innervalue in value.items():
        b26 = len(b5[innerkey])
        b27 = math.log(b25 / b26, 10)
        a3 += pow(innervalue * b27, 2)
    b28 = math.sqrt(a3)
    b7[b47] = b28
b29 = ""
b30 = []
with open(str(b9 / 'files' / 'topics.txt'), "r+") as fp:
    b31 = fp.readline()
    a4 = 1
    while b31:
        b32 = b31.strip() + " "
        b29 += b32
        if "<num>" in b32:
            b33 = re.sub('[^0-9]', '', b32)
            b30.append(b33)
            a4 += 1
        b31 = fp.readline()
b34 = re.findall(r'<title>(.*?)<desc>', b29)
b35 = re.findall(r'<desc> b35:(.*?)<narr>', b29)
b36 = re.findall(r'<narr> b36:(.*?)</top>', b29)
b15 = str(b9 / 'files' / 'main.qrels')
b37 = []
with open(b15) as fp:
    b31 = fp.readline()
    while b31:
        b32 = b31.strip().split(" ")
        b38 = b32[2].split("-")
        if "FT911" in b38[0]:
            b37.append(b32)
        b31 = fp.readline()
def fonk1(scorecalculated, b39):
    a5 = 0
    a6 = 0
    a7 = 0
    for x in range(len(b37)):
        if b39 = = b37[x][0]:
            a5 += 1
            if b37[x][3] == '1':
                b40 = b37[x][2].split("-")
                if int(b40[1]) in scorecalculated.keys():
                    a7 += 1
                a6 += 1
    b41 = a7 / len(b8)
    b42 = a7 / a6
    a6 = 0
    a7 = 0
    scorecalculated.clear()
    return b41, b42
b43 = open("files/OnlyTitleResults.txt", "w")
b25 = len(b6)
a8 = 0
b8.clear()
b44 = extractDifferentQuery(b34, b11)
for queryNum in b44.keys():
    for queryTerm, tfQ in b44[queryNum].items():
        b45 = b2[queryTerm]
        if b45 != 0:
            b26 = len(b5[b45])
            for inverKey, tfD in b5[b45].items():
                b27 = math.log(b25 / b26, 10)
                b46 = ((tfD * b27) * (tfQ * b27))
                b8[inverKey] += (b46 / b7[inverKey])
    a9 = 1
    for b47, value in sorted(b8.items(), b47 = lambda kv: kv[1], reverse=True):
        b43.write(b30[a8] + "        " + "FT911-" + str(b47) + "        " + str(a9) + "        " + str('{:.15f}'.format(value)) + '\n')
