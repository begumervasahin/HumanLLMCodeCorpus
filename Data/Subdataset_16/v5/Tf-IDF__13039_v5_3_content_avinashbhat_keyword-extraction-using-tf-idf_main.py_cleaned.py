from scraper import linkify, getLinks, getWords
from algorithms import tf, getDocLinkStrength, sublinear_tf, augmented_tf, idf, tfidf
def fonk1(b13):
    b1 = linkify(b13)
    b2 = getWords(b1)
    b3 = getLinks(b1)
    b4 = tf(b2)
    b5 = getDocLinkStrength(b3, b4)
    b6 = list(set(each[0] for each in b5))
    b7 = [getWords(linkify(each)) for each in b6[:10]]
    b8 = idf(b4, b7)
    b9 = tfidf(b4, b8)
    b10 = sorted(b9.items(), key=lambda x: x[1], reverse=True)
    b11 = getDocLinkStrength(b3, b9)
    b12 = list(set(each[0] for each in b11))
    return b12
b13 = input("Enter the Name of Personality\n")
b12 = fonk1(b13)
for keyword in b12:
    print(keyword)