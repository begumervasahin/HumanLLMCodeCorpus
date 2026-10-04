from scraper import linkify, getLinks, getWords
from algorithms import tf, getDocLinkStrength, idf, tfidf
def main():
    name = input("Enter the Name of the Personality: ")
    pageLink = linkify(name)
    wordList = getWords(pageLink)
    linkList = getLinks(pageLink)
    tfDict = tf(wordList)
    docLinks = getDocLinkStrength(linkList, tfDict)
    links_for_tf_idf = list({each[0] for each in docLinks})
    dump = []
    for each in links_for_tf_idf[:10]:
        tempLink = linkify(each)
        dump.append(getWords(tempLink))
    idfDict = idf(tfDict, dump)
    tfidfDict = tfidf(tfDict, idfDict)
    tfidfList = sorted(tfidfDict.items(), key=lambda x: x[1], reverse=True)
    keywords = getDocLinkStrength(linkList, tfidfDict)
    finalKeywordList = list({each[0] for each in keywords})
    for keyword in finalKeywordList:
        print(keyword)
if __name__ == "__main__":
    main()