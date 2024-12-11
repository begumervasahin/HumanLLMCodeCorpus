from scraper import linkify, getLinks, getWords
from algorithms import tf, getDocLinkStrength, idf, tfidf
def fonk1():
    return input("Enter the Name of Personality\n")
def fonk2(b6):
    return getWords(b6)
def fonk3(b6):
    return getLinks(b6)
def fonk4(b7):
    return tf(b7)
def fonk5(b8, b9):
    return getDocLinkStrength(b8, b9)
def fonk6(b10):
    return list(set(link for link, _ in b10))
def fonk7(word_links, b1 = 10):
    b2 = []
    for link in word_links[:b1]:
        b3 = linkify(link)
        b2.append(getWords(b3))
    return b2
def fonk8(b9, documents):
    return idf(b9, documents)
def fonk9(b9, b12):
    return tfidf(b9, b12)
def fonk10(b13):
    return sorted(b13.items(), b4 = lambda x: x[1], reverse=True)
def fonk11(b8, b13):
    return [link for link, _ in getDocLinkStrength(b8, b13)]
def fonk12(b15):
    for keyword in b15:
        print(keyword)
def fonk13():
    b5 = fonk1()
    b6 = linkify(b5)
    b7 = fonk2(b6)
    b8 = fonk3(b6)
    b9 = fonk4(b7)
    b10 = fonk5(b8, b9)
    b11 = fonk6(b10)
    b2 = fonk7(b11)
    b12 = fonk8(b9, b2)
    b13 = fonk9(b9, b12)
    b14 = fonk10(b13)
    b15 = fonk11(b8, b13)
    fonk12(b15)
if b16 = = "__main__":
    fonk13()