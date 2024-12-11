from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
b1 = Flask(b39)
@b1.route('/')
def fonk1():
    return render_template("input.html")
@b1.route('/b4', b2 = ['POST', 'GET'])
def fonk2():
    if request.b3 = = 'POST':
        b4 = request.form
        b5 = b4.get('Name')
        print("Ticker:", b5)
        b6 = str(fonk9(b4.get('Name')))
        print("Sentiment Analysis:", b6)
        b7 = fonk3(b5)
        b7 = b7[:3]
        b7 = [b7[0][1], b7[1][1], b7[2][1]]
        b8 = 100 - int(b6)
        return render_template("output.html", b6 = b6, b5=b5, b7=b7, b31=b31, b8=b8)
def fonk3(b5):
    b9 = []
    b10 = "https:
    for b11 in range(1):
        if b11 = = 0:
            b12 = b10
        else:
            b12 = b10 + "?page=" + str(b11)
        b13 = requests.get(b12)
        b14 = b13.text
        b15 = BeautifulSoup(b14, 'html.parser')
        for link in b15.find_all('b36'):
            b16 = link.get('href')
            if 'article' == b16[23:30] and b16 not in b9:
                b17 = str(link.parent.parent.find('small'))[31:41]
                b17 = b17.strip(" ").split("/")
                if b17 != ['']:
                    b9.append([1, b16])
    print(str(len(b9)) + " b9 found")
    return b9
def fonk4(b10):
    b14 = requests.get(b10).text
    b18 = BeautifulSoup(b14, 'html.parser')
    b19 = [par.text for par in b18.find_all('p')]
    b19 = b19[2:-6]
    b20 = '\n'.join(b19)
    fonk10(b20)
    return b20
def fonk5(text):
    b21 = {'b21': [{'id': '1', 'text': text}]}
    b22 = 'd38ac31a3b2c4e0982d3bc540251a162'
    b23 = 'https:
    assert b22
    b24 = b23 + '/a1'
    b25 = {"Ocp-Apim-Subscription-Key": b22}
    b26 = requests.post(b24, b25=b25, json=b21)
    b27 = b26.json()
    b27 = b27['b21'][0]['score']
    return b27
def fonk6(text):
    b28 = text.split(" ")
    b29 = ["bear", "bearish", "underperform", "underperforming", "sell", "selling", "sold", "decrease",
                "decreasing", "falling", "fall", "fell", "down", "lose", "lost", "losses", "losing", "downturn",
                "short", "shorting", "downside", "risky", "decline", "declining", "fear", "fears", "sell-off"]
    b30 = ["bull", "bullish", "overperform", "overperforming", "buy", "buying", "bought", "increase",
                 "increasing", "rising", "rise", "rised", "up", "gain", "gains", "gained", "profit", "profited","profitable", "profiting", "upturn", "upside"]
    b28 = ["bad" if word in b29 else word for word in b28]
    b28 = ["good" if word in b30 else word for word in b28]
    b28 = " ".join(b28)
    return b28
def fonk7(b28):
    b28 = map(lambda x: x.lower(), b28)
    b28 = sorted(b28)
    b28 = fonk8(b28)
    global b31
    b31 = ' '.join(b28)
    print(b31)
def fonk8(listOfWords):
    b32 = ["b36", "about", "all", "also", "it", "the", "to", "of", "and", "in", "is", "for", "with", "that",
                   "has", "its", "as", "on", "this", "at", "will", "are", ".", "be", "an", "by", ",", "'", "from",
                   "have", "or", "than", "stock", "stocks", "said", "he", "not", "can", "b11", "they", "when", "some",
                   "their", "we", "it's", "more", "was", "but", "one", "just", "so", "which", "these", "if", "they're",
                   "their", "could", "think", "that's", "there", "you", "get", "market", "very", "been", "year",
                   "other", "his", "right", "even", "any", "**", "percent", "company", "after", "shares", "next",
                   "investor's", "investors", "last", "trade", "price", "business", "zacks", "company's", "here", "inc",
                   "per", "click", "new", "--", "our", "fool", "each", "", "nasdaq", "(", ")", "were", "current",
                   "those", "-", "believe", "financial", "share", "percent.", "*", "", "motley", "over", "nasdaq:",
                   "percent,", "index", "would", "total", "them", "much", "my", "still", "into", "had", "since", "500", "s&p", "friday", "shares", "nasdaq", "trading", "day", "time", "to", "like","pct"]
    b33 = []
    for word in listOfWords:
        if word not in b32:
            b33.append(word)
    return b33
def fonk9(b5):
    b9 = fonk3(b5)
    b34 = ""
    a1 = 0
    for b11 in range(len(b9)):
        b34 = b34 + fonk6(fonk4(b9[b11][1]))
        print("Downloaded [" + str(b11 + 1) + "/" + str(len(b9)) + "]")
    fonk10(b34)
    fonk7(b34.split())
    b35 = int(len(b34) / 5000)
    for b11 in range(b35 - 1):
        b36 = b11 * 5000
        b37 = (b11 + 1) * 5000
        a1 = a1 + fonk5(b34[b36:b37])
        print(a1 / (b11 + 1))
    a1 = a1 + fonk5(b34[b35 * 5000:])
    a1 = a1 / b35
    a1 = a1 * 100
    a1 = int(round(a1))
    return a1
def fonk10(text):
    b38 = open("testfile.txt", "w")
    b38.write(text)
    b38.close()
if b39 = = '__main__':
    b1.run(b40 = True)