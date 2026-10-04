from scraper import linkify, getLinks, getWords
from algorithms import tf, getDocLinkStrength, sublinear_tf, augmented_tf, idf, tfidf
def get_personality_keywords(name):
    pageLink = linkify(name)
    wordList = getWords(pageLink)
    linkList = getLinks(pageLink)
    tfDict = tf(wordList)
    docLinks = getDocLinkStrength(linkList, tfDict)
    links_for_tf_idf = list(set(each[0] for each in docLinks))
    dump = [getWords(linkify(each)) for each in links_for_tf_idf[:10]]
    idfDict = idf(tfDict, dump)
    tfidfDict = tfidf(tfDict, idfDict)
    tfidfList = sorted(tfidfDict.items(), key=lambda x: x[1], reverse=True)
    keywords = getDocLinkStrength(linkList, tfidfDict)
    finalKeywordList = list(set(each[0] for each in keywords))
    return finalKeywordList
name = input("Enter the Name of Personality\n")
finalKeywordList = get_personality_keywords(name)
for keyword in finalKeywordList:
    print(keyword)