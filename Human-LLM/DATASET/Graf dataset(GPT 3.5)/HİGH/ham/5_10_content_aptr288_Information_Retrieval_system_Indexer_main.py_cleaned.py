import collections
import pathlib
import re
from nltk.stem import PorterStemmer
from collections import defaultdict
import collections
import time
import math
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
from Data_Parsing_and_Processing import extractingdata
import os
b11 = os.getcwd()
b12 = []
b11 = os.getcwd()
b13 = str(b11) + '\\files\\stopwordlist.txt'
with open(b13, 'r') as f:
    for b35 in f:
        for word in b35.split():
            b12.append(word)
b14 = []
b15 = []
for i in range(15):
    b16 = str(b9) + '/ft911/ft911_' + str(i + 1)
    TextList, b17 = extractingdata(b16,b12)
    b14 = b14 + TextList
    b15 = b15 + b17
b18 = list(set(b14))
b19 = sorted(b18)
a1 = 1
a2 = 1
for textToken in b19:
    b2[textToken] = a1
    a1 = a1 + 1
for DocNumString in b15:
    b1[DocNumString] = a2
    a2 = a2 + 1
b20 = open("files\\forward_index.txt", "w")
b9 = pathlib.Path('.')
for i in range(15):
    b16 = str(b9) + '/ft911/ft911_' + str(i + 1)
    b21 = indexingEachTerm(b16,b12,b2)
b22 = defaultdict(int)
for b51, value in b21.items():
    print(b51)
    for innerkey, innervalue in value.items():
        b23 = {}
        if (b22[innerkey] == 0) :
            b22[innerkey] = {b51:innervalue}
        elif(b22[innerkey] != 0) :
            b23 = b22[innerkey]
            b23.update({b51: innervalue})
            b22[innerkey] = b23
for b51, value in b21.items():
    b24 = {}
    for innerkey in sorted(value.items()):
        b24.update({innerkey[0]: value[innerkey[0]]})
    b6.update({b51 : b24})
for b51 in sorted(b22.items()):
    b25 = {}
    b26 = b22[b51[0]]
    for innerkey in sorted(b22[b51[0]].items()):
        b25.update({innerkey[0] : b26[innerkey[0]]})
    b5.update({b51[0] : b25})
b27 = open("files\\parser_output.txt", "w")
for b51, value in b2.items():
    b27.write(str(value) + "         " + str(b51) + '\n')
for b51, value in b1.items():
    b27.write(str(value) + "         " + str(b51) + '\n')
for b51, value in b6.items():
    b20.write(str(b51) + "         " + str(value) + '\n')
b28 = open("files\\inverted_index.txt", "w")
for b51, value in b5.items():
    b28.write(str(b51) + "         " + str(value) + '\n')
b29 = len(b6)
for b51, value in b6.items():
    a3 = 0
    for innerkey, innervalue in value.items():
        b30 = len(b5[innerkey])
        b31 = math.log(b29 / b30, 10)
        a3 = a3 + pow(innervalue*b31, 2);
    b32 = math.sqrt(a3)
    b7[b51] = b32
b33 = ""
b34 = []
with open(str(b9) + '/files/topics.txt', "r+") as fp:
    b35 = fp.readline()
    a4 = 1
    while b35:
        b36 = b35.strip() + " "
        b33 = b33 + b36
        if "<num>" in b36:
            b37 = re.sub('[^0-9]', '', b36)
            b34.append(b37)
            a4 = a4 + 1
        b35 = fp.readline()
b38 = re.findall(r'<title>(.*?)<desc>', b33)
b39 = re.findall(r'<desc> b39:(.*?)<narr>', b33)
b40 = re.findall(r'<narr> b40:(.*?)</top>', b33)
b16 = str(b9) + '/files/main.qrels'
b41 = []
with open(b16) as fp:
    b35 = fp.readline()
    while b35:
        b36 = b35.strip().split(" ")
        b42 = b36[2].split("-")
        if "FT911" in b42[0]:
            b41.append(b36)
        b35 = fp.readline()
def fonk1(scorecalculated,b43):
    a5 = 0
    a6 = 0
    a7 = 0
    for x in range(len(b41)):
        if b43 = = b41[x][0]:
            a5 += 1
            if b41[x][3] == '1':
                b44 = b41[x][2].split("-")
                if int(b44[1]) in scorecalculated.keys():
                    a7 += 1
                a6 += 1
    b45 = a7 / len(b8)
    b46 = a7 / a6
    a6 = 0
    a7 = 0
    scorecalculated.clear()
    return b45, b46
b47 = open("files/OnlyTitleResults.txt", "w")
b29 = len(b6)
a8 = 0
b8.clear()
b48 = extractDifferentQuery(b38,b12)
for queryNum in b48.keys():
    for queryTerm, tfQ in b48[queryNum].items():
        b49 = b2[queryTerm]
        if b49 != 0:
            b30 = len(b5[b49])
            for inverKey, tfD in b5[b49].items():
                b31 = math.log(b29 / b30, 10)
                b50 = ((tfD * b31) * (tfQ * b31))
                b8[inverKey] += (b50 / b7[inverKey])
    a9 = 1
    for b51, value in sorted(b8.items(), b51 = lambda kv: kv[1], reverse=True):
        b47.write(b34[a8] + "        " + "FT911-" + str(b51) + "        " + str(a9) + "        " + str('{:.15f}'.format(value)) + '\n')
        a9 = a9 + 1
    prec, b52 = fonk1(b8,b34[a8])
    b47.write("
    b47.write("  b53 = =>  " + str(prec) + "  Recall ==>  " + str(b52)+"\n")
    b8.clear()
    a8 = a8 + 1
b54 = open("files/titleWithDescriptionResults.txt", "w")
b55 = []
for x in range(len(b38)):
    b56 = str(b38[x] + " " + b39[x])
    b55.append(b56)
a8 = 0
b8.clear()
b57 = extractDifferentQuery(b55,b12)
for queryNum in b57.keys():
    for queryTerm, tfQ in b57[queryNum].items():
        b49 = b2[queryTerm]
        if b49 != 0:
            b30 = len(b5[b49])
            for inverKey, tfD in b5[b49].items():
                b31 = math.log(b29 / b30, 10)
                b50 = ((tfD * b31) * (tfQ * b31))
                b8[inverKey] += (b50 / b7[inverKey])
    a9 = 1
    for b51, value in sorted(b8.items(), b51 = lambda kv: kv[1], reverse=True):
        b54.write(b34[a8] + "        " + "FT911-" + str(b51) + "        " + str(a9) + "        " + str('{:.15f}'.format(value)) + '\n')
        a9 = a9 + 1
    prec, b52 = fonk1(b8, b34[a8])
    b54.write("
    b54.write("  b53 = =>  " + str(prec) + "  Recall ==>  " + str(b52) + "\n")
    b8.clear()
    a8 = a8 + 1
b58 = open("files/titleWithNarrativeResults.txt", "w")
b59 = []
for x in range(len(b38)):
    b60 = str(b38[x] + " " + b40[x])
    b59.append(b60)
a8 = 0
b8.clear()
b61 = extractDifferentQuery(b59,b12)
for queryNum in b61.keys():
    for queryTerm, tfQ in b61[queryNum].items():
        b49 = b2[queryTerm]
        if b49 != 0:
            b30 = len(b5[b49])
            for inverKey, tfD in b5[b49].items():
                b31 = math.log(b29 / b30, 10)
                b50 = ((tfD * b31) * (tfQ * b31))
                b8[inverKey] += (b50 / b7[inverKey])
    a9 = 1
    for b51, value in sorted(b8.items(), b51 = lambda kv: kv[1], reverse=True):
        b58.write(b34[a8] + "        " + "FT911-" + str(b51) + "        " + str(a9) + "        " + str('{:.15f}'.format(value)) + '\n')
        a9 = a9 + 1
    prec, b52 = fonk1(b8, b34[a8])
    b58.write("
    b58.write("  b53 = =>  " + str(prec) + "  Recall ==>  " + str(b52) + "\n")
    b8.clear()
    a8 = a8 + 1
def fonk2(queryForwardIndexExtracted):
    b29 = len(b6)
    a8 = 0
    b8.clear()
    for queryNum in queryForwardIndexExtracted.keys():
        for queryTerm, tfQ in queryForwardIndexExtracted[queryNum].items():
            b49 = b2[queryTerm]
            if b49 != 0:
                b30 = len(b5[b49])
                for inverKey, tfD in b5[b49].items():
                    b31 = math.log(b29 / b30, 10)
                    b50 = ((tfD * b31) * (tfQ * b31))
                    b8[inverKey] += (b50 / b7[inverKey])
        a9 = 1
        for b51, value in sorted(b8.items(), b51 = lambda kv: kv[1], reverse=True):
            queryResultFunc.write(b34[a8] + "        " + "FT911-" + str(b51) + "        " + str(a9) + "        " + str('{:.15f}'.format(value)) + '\n')
            a9 = a9 + 1
        b8.clear()
        a8 = a8 + 1
    return None
b58.close()
b54.close()
b47.close()
b20.close()
b28.close()
b27.close()
print("--- %s Secs ---" % (time.time() - b10))
print("User interface to check results for particular query and combinations")
b62 = True;
while(b62):
    b63 = input(" Please select a query number 352 353 354 359  or 0 to b62\n")
    if b63 = = "0":
        break
    else:
        print("Please select what all should be included in query")
        b64 = int(input("\n 1==> b38 only,  2==> b40 + b38 , 3==> Desc + b38, 4==> All"))
        if b64 = = 1:
            b65 = b38
        elif b64 = = 2:
            b65 = []
            for x in range(len(b38)):
                b66 = str(b38[x] + " " + b40[x])
                b65.append(b66)
        elif b64 = = 3:
            b65 = []
            for x in range(len(b38)):
                b66 = str(b38[x] + " " + b39[x])
                b65.append(b66)
        else:
            b65 = []
            for x in range(len(b38)):
                b66 = str(b38[x] + " " + b39[x] + " " + b40[x])
                b65.append(b66)
        b67 = b34.index(b63) + 1
        b68 = extractDifferentQuery(b65,b12)
        b29 = len(b6)
        for queryTerm, tfQ in b68[b67].items():
            b49 = b2[queryTerm]
            if b49 != 0:
                b30 = len(b5[b49])
                for inverKey, tfD in b5[b49].items():
                    b31 = math.log(b29 / b30, 10)
                    b50 = ((tfD * b31) * (tfQ * b31))
                    b8[inverKey] += b50 / b7[inverKey]
        print("Scores")
        a9 = 1
        for b51, value in sorted(b8.items(), b51 = lambda kv: kv[1], reverse=True):
            print(str(b51) + " b51 value" + " " + str(a9) + " " + str(value) + " " + b63)
            a9 = a9 + 1
        for b51, value in b8.items():
            print(str(b51) + " b51 value" + str(value))
        print("NumberOfFilesRetrived " + str(len(b8)))
        a5 = 0
        a6 = 0
        a7 = 0
        for x in range(len(b41)):
            if b63 = = b41[x][0]:
                a5 += 1
                if b41[x][3] == '1':
                    b44 = b41[x][2].split("-")
                    if int(b44[1]) in b8.keys():
                        a7 += 1
                    a6 += 1
        print(a5)
        print(a6)
        print(a7)
        print("b53")
        print(a7 / len(b8))
        print("Recall")
        print(a7 / a6)
        a6 = 0
        a7 = 0
        b8.clear()
        continue