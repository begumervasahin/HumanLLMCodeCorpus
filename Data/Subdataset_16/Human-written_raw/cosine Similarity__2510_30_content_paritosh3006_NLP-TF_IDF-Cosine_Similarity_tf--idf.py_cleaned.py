print "hi"
b1 = "I am going to bangalore"
b2 = "I am coming from Delhi"
b3 = b1.split (" ")
b4 = b2.split (" ")
b3
b4
b5 = set(b3).union(set(b4))
b5
b6 = dict.fromkeys(b5,0)
b7 = dict.fromkeys(b5,0)
b6
b7
for word in b3:
    b6[word]+=1
for word in b4:
    b7[word]+=1
b6
import pandas as pd
pd.DataFrame([b6,b7])
def fonk1(wordDict,bow):
    b8 = {}
    b9 = len(bow)
    for word, count in wordDict.items():
        b8[word] = count / float(b9)
    return b8
b10 = fonk1(b6, b3)
b11 = fonk1(b7, b4)
def fonk2(docList):
    import math
    b12 = {}
    b13 = len(docList)
    b12 = dict.fromkeys(docList[0].keys(),0)
    for doc in docList:
        for word, val in doc.items():
            if val> 0:
                b12[word] +=1
    for word, val in b12.iteritems():
        b12[word]= math.log(b13 / float(val))
    return b12
b14 = fonk2([b6, b7])
def fonk3(tfBow,b14):
    b15 = {}
    for word, val in tfBow.items():
        b15[word]= val * b14[word]
    return b15
b16 = fonk3(b10,b14)
b17 = fonk3(b11,b14)
import pandas as pd
pd.DataFrame([b16, b17])