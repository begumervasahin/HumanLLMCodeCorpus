
docA = "I am going to Bangalore"
docB = "I am coming from Delhi"
bowA = docA.split(" ")
bowB = docB.split(" ")
wordSet = set(bowA).union(set(bowB))
wordDictA = dict.fromkeys(wordSet, 0)
wordDictB = dict.fromkeys(wordSet, 0)
for word in bowA:
    wordDictA[word] += 1
for word in bowB:
    wordDictB[word] += 1
print("Word frequencies in docA:", wordDictA)
print("Word frequencies in docB:", wordDictB)
import pandas as pd
def computeTF(wordDict, bow):
    tfDict = {}
    bowCount = len(bow)
    for word, count in wordDict.items():
        tfDict[word] = count / float(bowCount)
    return tfDict
tfBowA = computeTF(wordDictA, bowA)
tfBowB = computeTF(wordDictB, bowB)
print("TF for docA:", tfBowA)
print("TF for docB:", tfBowB)
def computeIDF(docList):
    import math
    idfDict = {}
    N = len(docList)
    idfDict = dict.fromkeys(docList[0].keys(), 0)
    for doc in docList:
        for word, val in doc.items():
            if val > 0:
                idfDict[word] += 1
    for word, val in idfDict.items():
        idfDict[word] = math.log(N / float(val))
    return idfDict
idfs = computeIDF([wordDictA, wordDictB])
print("IDF values:", idfs)
def computeTFIDF(tfBow, idfs):
    tfidf = {}
    for word, val in tfBow.items():
        tfidf[word] = val * idfs[word]
    return tfidf
tfidfBowA = computeTFIDF(tfBowA, idfs)
tfidfBowB = computeTFIDF(tfBowB, idfs)
tfidf_df = pd.DataFrame([tfidfBowA, tfidfBowB])
print("TF-IDF values:")
print(tfidf_df)