from scraper import linkify, getLinks, getWords
from algorithms import tf, getDocLinkStrength, sublinear_tf, augmented_tf, idf, tfidf
name = input("Enter the Name of Personality\n")
pageLink = linkify(name)
wordList = getWords(pageLink)
linkList = getLinks(pageLink)
tfDict = tf(wordList)
docLinks = getDocLinkStrength(linkList, tfDict)
links_for_tf_idf = []
for each in docLinks:
    temp = each[0]
    if temp not in links_for_tf_idf:
        links_for_tf_idf.append(temp)
dump = []
for each in links_for_tf_idf[:10]:
    tempLink = linkify(each)
    dump.append(getWords(tempLink))
idfDict = idf(tfDict, dump)
tfidfDict = tfidf(tfDict, idfDict)
tfidfList = [(each, tfidfDict[each]) for each in tfidfDict]
tfidfList.sort(key=lambda x: x[1], reverse=True)
keywords = getDocLinkStrength(linkList, tfidfDict)
finalKeywordList = []
for each in keywords:
    temp = each[0]
    if temp not in finalKeywordList:
        finalKeywordList.append(temp)
for keyword in finalKeywordList:
    print(keyword)