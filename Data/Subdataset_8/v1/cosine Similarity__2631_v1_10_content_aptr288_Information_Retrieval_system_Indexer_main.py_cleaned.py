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
docNum_dict = {}
word_dict = collections.defaultdict(int)
inverted_index_dict = {}
ps = PorterStemmer()
sortedInvertedIndex = {}
sortedForwardIndex = {}
normalizedDoc = {}
score = defaultdict(int)
currentDirectory = pathlib.Path('.')
start_time = time.time()
stopWordList = []
stopwords_filepath = str(currentDirectory / 'files' / 'stopwordlist.txt')
with open(stopwords_filepath, 'r') as f:
    for line in f:
        for word in line.split():
            stopWordList.append(word)
extractedTextList = []
extractedDocNumList = []
for i in range(15):
    filepath = currentDirectory / f'ft911/ft911_{i + 1}'
    TextList, docNumlist = extractingdata(filepath, stopWordList)
    extractedTextList.extend(TextList)
    extractedDocNumList.extend(docNumlist)
duplicatesRemoved = list(set(extractedTextList))
FinalSortedList = sorted(duplicatesRemoved)
wordCounter = 1
DocCounter = 1
for textToken in FinalSortedList:
    word_dict[textToken] = wordCounter
    wordCounter += 1
for DocNumString in extractedDocNumList:
    docNum_dict[DocNumString] = DocCounter
    DocCounter += 1
for i in range(15):
    filepath = currentDirectory / f'ft911/ft911_{i + 1}'
    forwardIndex = indexingEachTerm(filepath, stopWordList, word_dict)
inv_indx = defaultdict(int)
for key, value in forwardIndex.items():
    for innerkey, innervalue in value.items():
        intermediate_dict = {}
        if inv_indx[innerkey] == 0:
            inv_indx[innerkey] = {key: innervalue}
        elif inv_indx[innerkey] != 0:
            intermediate_dict = inv_indx[innerkey]
            intermediate_dict.update({key: innervalue})
            inv_indx[innerkey] = intermediate_dict
for key, value in forwardIndex.items():
    intermediate_forward_dict = {}
    for innerkey in sorted(value.items()):
        intermediate_forward_dict.update({innerkey[0]: value[innerkey[0]]})
    sortedForwardIndex.update({key: intermediate_forward_dict})
for key in sorted(inv_indx.items()):
    intermediate_inverted_dict = {}
    wordIdFreq = inv_indx[key[0]]
    for innerkey in sorted(inv_indx[key[0]].items()):
        intermediate_inverted_dict.update({innerkey[0]: wordIdFreq[innerkey[0]]})
    sortedInvertedIndex.update({key[0]: intermediate_inverted_dict})
N = len(sortedForwardIndex)
for key, value in sortedForwardIndex.items():
    sumofsquares = 0
    for innerkey, innervalue in value.items():
        df = len(sortedInvertedIndex[innerkey])
        idf = math.log(N / df, 10)
        sumofsquares += pow(innervalue * idf, 2)
    sqrsum = math.sqrt(sumofsquares)
    normalizedDoc[key] = sqrsum
totalDoc = ""
queryNumber = []
with open(str(currentDirectory / 'files' / 'topics.txt'), "r+") as fp:
    line = fp.readline()
    counter = 1
    while line:
        stripedString = line.strip() + " "
        totalDoc += stripedString
        if "<num>" in stripedString:
            querynum = re.sub('[^0-9]', '', stripedString)
            queryNumber.append(querynum)
            counter += 1
        line = fp.readline()
Title = re.findall(r'<title>(.*?)<desc>', totalDoc)
Description = re.findall(r'<desc> Description:(.*?)<narr>', totalDoc)
Narrative = re.findall(r'<narr> Narrative:(.*?)</top>', totalDoc)
filepath = str(currentDirectory / 'files' / 'main.qrels')
referenceQueryDoc = []
with open(filepath) as fp:
    line = fp.readline()
    while line:
        stripedString = line.strip().split(" ")
        querydocindicated = stripedString[2].split("-")
        if "FT911" in querydocindicated[0]:
            referenceQueryDoc.append(stripedString)
        line = fp.readline()
def calPrecisionRecal(scorecalculated, queryNumberToEvaluateOn):
    numberofDocGiven = 0
    numberofRelaventDocsGiven = 0
    truePositive = 0
    for x in range(len(referenceQueryDoc)):
        if queryNumberToEvaluateOn == referenceQueryDoc[x][0]:
            numberofDocGiven += 1
            if referenceQueryDoc[x][3] == '1':
                docnumInref = referenceQueryDoc[x][2].split("-")
                if int(docnumInref[1]) in scorecalculated.keys():
                    truePositive += 1
                numberofRelaventDocsGiven += 1
    precisionCal = truePositive / len(score)
    recallCal = truePositive / numberofRelaventDocsGiven
    numberofRelaventDocsGiven = 0
    truePositive = 0
    scorecalculated.clear()
    return precisionCal, recallCal
queryResults = open("files/OnlyTitleResults.txt", "w")
N = len(sortedForwardIndex)
querycount = 0
score.clear()
QueryWithTitle = extractDifferentQuery(Title, stopWordList)
for queryNum in QueryWithTitle.keys():
    for queryTerm, tfQ in QueryWithTitle[queryNum].items():
        queryId = word_dict[queryTerm]
        if queryId != 0:
            df = len(sortedInvertedIndex[queryId])
            for inverKey, tfD in sortedInvertedIndex[queryId].items():
                idf = math.log(N / df, 10)
                tfidf = ((tfD * idf) * (tfQ * idf))
                score[inverKey] += (tfidf / normalizedDoc[inverKey])
    counterRank = 1
    for key, value in sorted(score.items(), key=lambda kv: kv[1], reverse=True):
        queryResults.write(queryNumber[querycount] + "        " + "FT911-" + str(key) + "        " + str(counterRank) + "        " + str('{:.15f}'.format(value)) + '\n')
