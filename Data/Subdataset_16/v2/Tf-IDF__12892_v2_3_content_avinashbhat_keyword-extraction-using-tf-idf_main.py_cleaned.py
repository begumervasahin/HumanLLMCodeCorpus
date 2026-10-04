from scraper import linkify, getLinks, getWords
from algorithms import tf, getDocLinkStrength, idf, tfidf
def fonk1():
    b1 = input("Enter the Name of the Personality: ")
    b2 = linkify(b1)
    b3 = getWords(b2)
    b4 = getLinks(b2)
    b5 = tf(b3)
    b6 = getDocLinkStrength(b4, b5)
    b7 = list({each[0] for each in b6})
    b8 = []
    for each in b7[:10]:
        b9 = linkify(each)
        b8.append(getWords(b9))
    b10 = idf(b5, b8)
    b11 = tfidf(b5, b10)
    b12 = sorted(b11.items(), key=lambda x: x[1], reverse=True)
    b13 = getDocLinkStrength(b4, b11)
    b14 = list({each[0] for each in b13})
    for keyword in b14:
        print(keyword)
if b15 = = "__main__":
    fonk1()