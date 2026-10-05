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
docNum_dict = {}
word_dict = defaultdict(int)
inverted_index_dict = {}
ps = PorterStemmer()
sortedInvertedIndex = {}
sortedForwardIndex = {}
normalizedDoc = {}
score = defaultdict(int)
currentDirectory = pathlib.Path('.')
start_time = time.time()
stopWordList = []
stopwords_filepath = currentDirectory / 'files' / 'stopwordlist.txt'
with open(stopwords_filepath, 'r') as f:
    stopWordList.extend(word.strip() for line in f for word in line.split())
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
forward_file = open("files\\forward_index.txt", "w")
for i in range(15):
    filepath = currentDirectory / f'ft911/ft911_{i + 1}'
    forwardIndex = indexingEachTerm(filepath, stopWordList, word_dict)
inv_indx = defaultdict(int)
for key, value in forwardIndex.items():
    for innerkey, innervalue in value.items():
        if inv_indx[innerkey] == 0:
            inv_indx[innerkey] = {key: innervalue}
        elif inv_indx[innerkey] != 0:
            inv_indx[innerkey].update({key: innervalue})
sortedForwardIndex = {key: {innerkey: value for innerkey, value in sorted(idx.items())} for key, idx in forwardIndex.items()}
sortedInvertedIndex = {key: {innerkey: value for innerkey, value in sorted(idx.items())} for key, idx in inv_indx.items()}
text_file = open("files\\parser_output.txt", "w")
for key, value in word_dict.items():
    text_file.write(f"{value}         {key}\n")
for key, value in docNum_dict.items():
    text_file.write(f"{value}         {key}\n")
for key, value in sortedForwardIndex.items():
    forward_file.write(f"{key}         {value}\n")
forward_file.close()
inverted_file = open("files\\inverted_index.txt", "w")
for key, value in sortedInvertedIndex.items():
    inverted_file.write(f"{key}         {value}\n")
inverted_file.close()
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
with open(currentDirectory / 'files/topics.txt', "r+") as fp:
    for line in fp:
        stripedString = line.strip() + " "
        totalDoc += stripedString
        if "<num>" in stripedString:
            querynum = re.sub('[^0-9]', '', stripedString)
            queryNumber.append(querynum)
Title = re.findall(r'<title>(.*?)<desc>', totalDoc)
Description = re.findall(r'<desc> Description:(.*?)<narr>', totalDoc)
Narrative = re.findall(r'<narr> Narrative:(.*?)</top>', totalDoc)
referenceQueryDoc = []
with open(currentDirectory / 'files/main.qrels') as fp:
    for line in fp:
        stripedString = line.strip().split(" ")
        querydocindicated = stripedString[2].split("-")
        if "FT911" in querydocindicated[0]:
            referenceQueryDoc.append(stripedString)
def calPrecisionRecall(scorecalculated, queryNumberToEvaluateOn):
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
        queryResults.write(f"{queryNumber[querycount]}        FT911-{key}        {counterRank}        {value:.15f}\n")
        counterRank += 1
    prec, recal = calPrecisionRecall(score, queryNumber[querycount])
    queryResults.write(f"  Precision ==>  {prec}  Recall ==>  {recal}\n")
    score.clear()
    querycount += 1