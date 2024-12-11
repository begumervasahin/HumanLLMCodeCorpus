from scraper import linkify, getLinks, getWords
from algorithms import tf, getDocLinkStrength, idf, tfidf
def fonk1():
    b1 = input("Enter the Name of Personality: ")
    b2 = linkify(b1)
    b3 = getWords(b2)
    b4 = getLinks(b2)
    b5 = tf(b3)
    b6 = getDocLinkStrength(b4, b5)
    b7 = []
    for each in b6:
        b8 = each[0]
        if b8 not in b7:
            b7.append(b8)
    b9 = []
    for each in b7[:10]:
        b10 = linkify(each)
        b9.append(getWords(b10))
    b11 = idf(b5, b9)
    b12 = tfidf(b5, b11)
    b13 = sorted(b12.items(), key=lambda x: x[1], reverse=True)
    b14 = getDocLinkStrength(b4, b12)
    b15 = []
    for each in b14:
        b8 = each[0]
        if b8 not in b15:
            b15.append(b8)
    for each in b15:
        print(each)
if b16 = = "__main__":
    fonk1()