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
docNum_dict = {}
word_dict = collections.defaultdict(int)
inverted_index_dict = {}
ps = PorterStemmer()
sortedInvertedIndex = {}
sortedForwardIndex = {}
normalizedDoc = {}
score  = defaultdict(int)
currentDirectory = pathlib.Path('.')
start_time = time.time()
from Data_Parsing_and_Processing import extractingdata
import os
cwd = os.getcwd()
stopWordList = []
cwd = os.getcwd()
path = str(cwd) + '\\files\\stopwordlist.txt'
with open(path, 'r') as f:
    for line in f:
        for word in line.split():
            stopWordList.append(word)
extractedTextList = []
extractedDocNumList = []
for i in range(15):
    filepath = str(currentDirectory) + '/ft911/ft911_' + str(i + 1)
    TextList, docNumlist = extractingdata(filepath,stopWordList)
    extractedTextList = extractedTextList + TextList
    extractedDocNumList = extractedDocNumList + docNumlist
duplicatesRemoved = list(set(extractedTextList))
FinalSortedList = sorted(duplicatesRemoved)
wordCounter = 1
DocCounter = 1
for textToken in FinalSortedList:
    word_dict[textToken] = wordCounter
    wordCounter = wordCounter + 1
for DocNumString in extractedDocNumList:
    docNum_dict[DocNumString] = DocCounter
    DocCounter = DocCounter + 1
forward_file = open("files\\forward_index.txt", "w")
currentDirectory = pathlib.Path('.')
for i in range(15):
    filepath = str(currentDirectory) + '/ft911/ft911_' + str(i + 1)
    forwardIndex = indexingEachTerm(filepath,stopWordList,word_dict)
inv_indx = defaultdict(int)
for key, value in forwardIndex.items():
    print(key)
    for innerkey, innervalue in value.items():
        intermediate_dict = {}
        if (inv_indx[innerkey] == 0) :
            inv_indx[innerkey] = {key:innervalue}
        elif(inv_indx[innerkey] != 0) :
            intermediate_dict = inv_indx[innerkey]
            intermediate_dict.update({key: innervalue})
            inv_indx[innerkey] = intermediate_dict
for key, value in forwardIndex.items():
    intermediate_forward_dict = {}
    for innerkey in sorted(value.items()):
        intermediate_forward_dict.update({innerkey[0]: value[innerkey[0]]})
    sortedForwardIndex.update({key : intermediate_forward_dict})
for key in sorted(inv_indx.items()):
    intermediate_inverted_dict = {}
    wordIdFreq = inv_indx[key[0]]
    for innerkey in sorted(inv_indx[key[0]].items()):
        intermediate_inverted_dict.update({innerkey[0] : wordIdFreq[innerkey[0]]})
    sortedInvertedIndex.update({key[0] : intermediate_inverted_dict})
text_file = open("files\\parser_output.txt", "w")
for key, value in word_dict.items():
    text_file.write(str(value) + "         " + str(key) + '\n')
for key, value in docNum_dict.items():
    text_file.write(str(value) + "         " + str(key) + '\n')
for key, value in sortedForwardIndex.items():
    forward_file.write(str(key) + "         " + str(value) + '\n')
inverted_file = open("files\\inverted_index.txt", "w")
for key, value in sortedInvertedIndex.items():
    inverted_file.write(str(key) + "         " + str(value) + '\n')
N = len(sortedForwardIndex)
for key, value in sortedForwardIndex.items():
    sumofsquares = 0
    for innerkey, innervalue in value.items():
        df = len(sortedInvertedIndex[innerkey])
        idf = math.log(N / df, 10)
        sumofsquares = sumofsquares + pow(innervalue*idf, 2);
    sqrsum = math.sqrt(sumofsquares)
    normalizedDoc[key] = sqrsum
totalDoc = ""
queryNumber = []
with open(str(currentDirectory) + '/files/topics.txt', "r+") as fp:
    line = fp.readline()
    counter = 1
    while line:
        stripedString = line.strip() + " "
        totalDoc = totalDoc + stripedString
        if "<num>" in stripedString:
            querynum = re.sub('[^0-9]', '', stripedString)
            queryNumber.append(querynum)
            counter = counter + 1
        line = fp.readline()
Title = re.findall(r'<title>(.*?)<desc>', totalDoc)
Description = re.findall(r'<desc> Description:(.*?)<narr>', totalDoc)
Narrative = re.findall(r'<narr> Narrative:(.*?)</top>', totalDoc)
filepath = str(currentDirectory) + '/files/main.qrels'
referenceQueryDoc = []
with open(filepath) as fp:
    line = fp.readline()
    while line:
        stripedString = line.strip().split(" ")
        querydocindicated = stripedString[2].split("-")
        if "FT911" in querydocindicated[0]:
            referenceQueryDoc.append(stripedString)
        line = fp.readline()
def calPrecisionRecal(scorecalculated,queryNumberToEvaluateOn):
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
QueryWithTitle = extractDifferentQuery(Title,stopWordList)
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
        counterRank = counterRank + 1
    prec, recal = calPrecisionRecal(score,queryNumber[querycount])
    queryResults.write("
    queryResults.write("  Precision ==>  " + str(prec) + "  Recall ==>  " + str(recal)+"\n")
    score.clear()
    querycount = querycount + 1
queryResultWithDescription = open("files/titleWithDescriptionResults.txt", "w")
queryDesc = []
for x in range(len(Title)):
    stringconc1 = str(Title[x] + " " + Description[x])
    queryDesc.append(stringconc1)
querycount = 0
score.clear()
QueryWithTitleDescription = extractDifferentQuery(queryDesc,stopWordList)
for queryNum in QueryWithTitleDescription.keys():
    for queryTerm, tfQ in QueryWithTitleDescription[queryNum].items():
        queryId = word_dict[queryTerm]
        if queryId != 0:
            df = len(sortedInvertedIndex[queryId])
            for inverKey, tfD in sortedInvertedIndex[queryId].items():
                idf = math.log(N / df, 10)
                tfidf = ((tfD * idf) * (tfQ * idf))
                score[inverKey] += (tfidf / normalizedDoc[inverKey])
    counterRank = 1
    for key, value in sorted(score.items(), key=lambda kv: kv[1], reverse=True):
        queryResultWithDescription.write(queryNumber[querycount] + "        " + "FT911-" + str(key) + "        " + str(counterRank) + "        " + str('{:.15f}'.format(value)) + '\n')
        counterRank = counterRank + 1
    prec, recal = calPrecisionRecal(score, queryNumber[querycount])
    queryResultWithDescription.write("
    queryResultWithDescription.write("  Precision ==>  " + str(prec) + "  Recall ==>  " + str(recal) + "\n")
    score.clear()
    querycount = querycount + 1
queryResultWithNarrative = open("files/titleWithNarrativeResults.txt", "w")
titleNar = []
for x in range(len(Title)):
    stringconc2 = str(Title[x] + " " + Narrative[x])
    titleNar.append(stringconc2)
querycount = 0
score.clear()
QueryWithTitleNarrative = extractDifferentQuery(titleNar,stopWordList)
for queryNum in QueryWithTitleNarrative.keys():
    for queryTerm, tfQ in QueryWithTitleNarrative[queryNum].items():
        queryId = word_dict[queryTerm]
        if queryId != 0:
            df = len(sortedInvertedIndex[queryId])
            for inverKey, tfD in sortedInvertedIndex[queryId].items():
                idf = math.log(N / df, 10)
                tfidf = ((tfD * idf) * (tfQ * idf))
                score[inverKey] += (tfidf / normalizedDoc[inverKey])
    counterRank = 1
    for key, value in sorted(score.items(), key=lambda kv: kv[1], reverse=True):
        queryResultWithNarrative.write(queryNumber[querycount] + "        " + "FT911-" + str(key) + "        " + str(counterRank) + "        " + str('{:.15f}'.format(value)) + '\n')
        counterRank = counterRank + 1
    prec, recal = calPrecisionRecal(score, queryNumber[querycount])
    queryResultWithNarrative.write("
    queryResultWithNarrative.write("  Precision ==>  " + str(prec) + "  Recall ==>  " + str(recal) + "\n")
    score.clear()
    querycount = querycount + 1
def scoreCalculation(queryForwardIndexExtracted):
    N = len(sortedForwardIndex)
    querycount = 0
    score.clear()
    for queryNum in queryForwardIndexExtracted.keys():
        for queryTerm, tfQ in queryForwardIndexExtracted[queryNum].items():
            queryId = word_dict[queryTerm]
            if queryId != 0:
                df = len(sortedInvertedIndex[queryId])
                for inverKey, tfD in sortedInvertedIndex[queryId].items():
                    idf = math.log(N / df, 10)
                    tfidf = ((tfD * idf) * (tfQ * idf))
                    score[inverKey] += (tfidf / normalizedDoc[inverKey])
        counterRank = 1
        for key, value in sorted(score.items(), key=lambda kv: kv[1], reverse=True):
            queryResultFunc.write(queryNumber[querycount] + "        " + "FT911-" + str(key) + "        " + str(counterRank) + "        " + str('{:.15f}'.format(value)) + '\n')
            counterRank = counterRank + 1
        score.clear()
        querycount = querycount + 1
    return None
queryResultWithNarrative.close()
queryResultWithDescription.close()
queryResults.close()
forward_file.close()
inverted_file.close()
text_file.close()
print("--- %s Secs ---" % (time.time() - start_time))
print("User interface to check results for particular query and combinations")
exit = True;
while(exit):
    queryNumberToEvaluate = input(" Please select a query number 352 353 354 359  or 0 to exit\n")
    if queryNumberToEvaluate == "0":
        break
    else:
        print("Please select what all should be included in query")
        options = int(input("\n 1==> Title only,  2==> Narrative + Title , 3==> Desc + Title, 4==> All"))
        if options == 1:
            queryGiven = Title
        elif options == 2:
            queryGiven = []
            for x in range(len(Title)):
                stringconc = str(Title[x] + " " + Narrative[x])
                queryGiven.append(stringconc)
        elif options == 3:
            queryGiven = []
            for x in range(len(Title)):
                stringconc = str(Title[x] + " " + Description[x])
                queryGiven.append(stringconc)
        else:
            queryGiven = []
            for x in range(len(Title)):
                stringconc = str(Title[x] + " " + Description[x] + " " + Narrative[x])
                queryGiven.append(stringconc)
        indexOfQuery = queryNumber.index(queryNumberToEvaluate) + 1
        QueryIndex = extractDifferentQuery(queryGiven,stopWordList)
        N = len(sortedForwardIndex)
        for queryTerm, tfQ in QueryIndex[indexOfQuery].items():
            queryId = word_dict[queryTerm]
            if queryId != 0:
                df = len(sortedInvertedIndex[queryId])
                for inverKey, tfD in sortedInvertedIndex[queryId].items():
                    idf = math.log(N / df, 10)
                    tfidf = ((tfD * idf) * (tfQ * idf))
                    score[inverKey] += tfidf / normalizedDoc[inverKey]
        print("Scores")
        counterRank = 1
        for key, value in sorted(score.items(), key=lambda kv: kv[1], reverse=True):
            print(str(key) + " key value" + " " + str(counterRank) + " " + str(value) + " " + queryNumberToEvaluate)
            counterRank = counterRank + 1
        for key, value in score.items():
            print(str(key) + " key value" + str(value))
        print("NumberOfFilesRetrived " + str(len(score)))
        numberofDocGiven = 0
        numberofRelaventDocsGiven = 0
        truePositive = 0
        for x in range(len(referenceQueryDoc)):
            if queryNumberToEvaluate == referenceQueryDoc[x][0]:
                numberofDocGiven += 1
                if referenceQueryDoc[x][3] == '1':
                    docnumInref = referenceQueryDoc[x][2].split("-")
                    if int(docnumInref[1]) in score.keys():
                        truePositive += 1
                    numberofRelaventDocsGiven += 1
        print(numberofDocGiven)
        print(numberofRelaventDocsGiven)
        print(truePositive)
        print("Precision")
        print(truePositive / len(score))
        print("Recall")
        print(truePositive / numberofRelaventDocsGiven)
        numberofRelaventDocsGiven = 0
        truePositive = 0
        score.clear()
        continue