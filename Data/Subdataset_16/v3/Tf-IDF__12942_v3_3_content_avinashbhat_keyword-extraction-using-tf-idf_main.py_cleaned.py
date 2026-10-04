from scraper import linkify, getLinks, getWords
from algorithms import tf, getDocLinkStrength, idf, tfidf
def fonk1(docLinks):
    return list({link for link, _ in docLinks})
def fonk2(links):
    b1 = []
    for link in links:
        b2 = linkify(link)
        b1.append(getWords(b2))
    return b1
def fonk3(b9, b12):
    b3 = idf(b9, b12)
    return tfidf(b9, b3)
def fonk4(b13):
    return sorted(b13.items(), b4 = lambda x: x[1], reverse=True)
def fonk5():
    b5 = input("Enter the Name of the Personality: ")
    b6 = linkify(b5)
    b7 = getWords(b6)
    b8 = getLinks(b6)
    b9 = tf(b7)
    b10 = getDocLinkStrength(b8, b9)
    b11 = fonk1(b10)
    b12 = fonk2(b11[:10])
    b13 = fonk3(b9, b12)
    b14 = fonk4(b13)
    b15 = getDocLinkStrength(b8, b13)
    b16 = list({keyword for keyword, _ in b15})
    for keyword in b16:
        print(keyword)
if b17 = = "__main__":
    fonk5()