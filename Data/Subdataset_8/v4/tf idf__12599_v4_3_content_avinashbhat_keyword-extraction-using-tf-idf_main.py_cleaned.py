
from scraper import linkify, getLinks, getWords
from algorithms import tf, getDocLinkStrength, idf, tfidf
name = input("Enter the Name of Personality\n")
pageLink = linkify(name)
wordList = getWords(pageLink)
linkList = getLinks(pageLink)
tfDict = tf(wordList)
docLinks = getDocLinkStrength(linkList, tfDict)
links_for_tf_idf = []
for link, _ in docLinks:
    if link not in links_for_tf_idf:
        links_for_tf_idf.append(link)
dump = []
for link in links_for_tf_idf[:10]:
    tempLink = linkify(link)
    dump.append(getWords(tempLink))
idfDict = idf(tfDict, dump)
tfidfDict = tfidf(tfDict, idfDict)
tfidfList = sorted(tfidfDict.items(), key=lambda x: x[1], reverse=True)
keywords = getDocLinkStrength(linkList, tfidfDict)
finalKeywordList = []
for link, _ in keywords:
    if link not in finalKeywordList:
        finalKeywordList.append(link)
for keyword in finalKeywordList:
    print(keyword)