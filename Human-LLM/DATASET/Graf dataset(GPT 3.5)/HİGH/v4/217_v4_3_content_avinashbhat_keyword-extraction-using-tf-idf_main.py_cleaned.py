
from scraper import linkify, getLinks, getWords
from algorithms import tf, getDocLinkStrength, idf, tfidf
b1 = input("Enter the Name of Personality\n")
b2 = linkify(b1)
b3 = getWords(b2)
b4 = getLinks(b2)
b5 = tf(b3)
b6 = getDocLinkStrength(b4, b5)
b7 = []
for link, _ in b6:
    if link not in b7:
        b7.append(link)
b8 = []
for link in b7[:10]:
    b9 = linkify(link)
    b8.append(getWords(b9))
b10 = idf(b5, b8)
b11 = tfidf(b5, b10)
b12 = sorted(b11.items(), key=lambda x: x[1], reverse=True)
b13 = getDocLinkStrength(b4, b11)
b14 = []
for link, _ in b13:
    if link not in b14:
        b14.append(link)
for keyword in b14:
    print(keyword)