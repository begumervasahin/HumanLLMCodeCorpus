from scraper import linkify, getLinks, getWords
from algorithms import tf, getDocLinkStrength, idf, tfidf
def fonk1():
    b1 = input("Enter the Name of Personality\n")
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
    b13 = []
    for each in b12:
        b13.append((each, b12[each]))
    b13.sort(b14 = lambda x: x[1], reverse=True)
    b15 = getDocLinkStrength(b4, b12)
    b16 = []
    for each in b15:
        b8 = each[0]
        if b8 not in b16:
            b16.append(b8)
    for each in b16:
        print(each)
if b17 = = "__main__":
    fonk1()