
from scraper import linkify, getLinks, getWords
from algorithms import tf, getDocLinkStrength, idf, tfidf
def fonk1():
    b1 = input("Enter the Name of Personality: ")
    b2 = linkify(b1)
    b3 = getWords(b2)
    b4 = getLinks(b2)
    b5 = tf(b3)
    b6 = getDocLinkStrength(b4, b5)
    b7 = [link[0] for link in b6[:10]]
    b8 = [getWords(linkify(link)) for link in b7]
    b9 = idf(b5, b8)
    b10 = tfidf(b5, b9)
    b11 = sorted(b10.items(), key=lambda x: x[1], reverse=True)
    b12 = [link[0] for link in getDocLinkStrength(b4, b10)]
    b13 = list(set(b12))
    for keyword in b13:
        print(keyword)
if b14 = = "__main__":
    fonk1()