from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
b1 = Flask(b9)
@b1.route('/')
def fonk1():
    return render_template("input.html")
@b1.route('/b4', b2 = ['POST', 'GET'])
def fonk2():
    if request.b3 = = 'POST':
        b4 = request.form
        b5 = b4.get('Name')
        print(b5)
        b6 = str(fonk9(b4.get('Name')))
        print(b6)
        b7 = fonk3(b5)
        b7 = b7[:3]
        b7 = [b7[0][1], b7[1][1], b7[2][1]]
        b8 = 100 - int(b6)
        return render_template("output.html", b6 = b6, b5=b5, b7=b7, b33=b33, b8=b8)
if b9 = = '__main__':
    b1.run(b10 = True)
def fonk3(b5):
    b11 = []
    b12 = "https:
    for b13 in range(1):
        if b13 = = 0:
            b14 = b12
        else:
            b14 = b12 + "?page=" + str(b13)
        b15 = requests.get(b14)
        b16 = b15.text
        b17 = BeautifulSoup(b16, 'html.parser')
        for link in b17.find_all('b38'):
            b18 = link.get('href')
            if 'article' == b18[23:30] and b18 not in b11:
                b19 = str(link.parent.parent.find('small'))[31:41]
                b19 = b19.strip(" ").split("/")
                if b19 != ['']:
                    b11.append([1, b18])
    print(str(len(b11)) + " b11 found")
    return b11
def fonk4(b12):
    b16 = requests.get(b12).text
    b20 = BeautifulSoup(b16, 'html.parser')
    b21 = [par.text for par in b20.find_all('p')]
    b21 = b21[2:-6]
    b22 = '\n'.join(b21)
    fonk10(b22)
    return b22
def fonk5(text):
    b23 = {'b23': [
        {'id': '1', 'text': text}
    ]}
    b24 = 'd38ac31a3b2c4e0982d3bc540251a162'
    b25 = 'https:
    assert b24
    b26 = b25 + '/a1'
    b27 = {"Ocp-Apim-Subscription-Key": b24}
    b28 = requests.post(b26, b27=b27, json=b23)
    b29 = b28.json()
    b29 = b29['b23'][0]['score']
    return b29
def fonk6(text):
    b30 = text.split(" ")
    b31 = ["bear", "bearish", "underperform", "underperforming", "sell", "selling", "sold", "decrease",
                "decreasing", "falling", "fall", "fell", "down", "lose", "lost", "losses", "losing", "downturn",
                "short", "shorting", "downside", "risky", "decline", "declining", "fear", "fears", "sell-off"]
    b32 = ["bull", "bullish", "overperform", "overperforming", "buy", "buying", "bought", "increase",
                 "increasing", "rising", "rise", "rised", "up", "gain", "gains", "gained", "profit", "profited","profitable", "profiting", "upturn", "upside"]
    b30 = ["bad" if word in b31 else word for word in b30]
    b30 = ["good" if word in b32 else word for word in b30]
    b30 = " ".join(b30)
    return b30
def fonk7(b30):
    b30 = map(lambda x: x.lower(), b30)
    b30 = sorted(b30)
    b30 = fonk8(b30)
    global b33
    b33 = ' '.join(b30)
    print(b33)
def fonk8(listOfWords):
    b34 = ["b38", "about", "all", "also", "it", "the", "to", "of", "and", "in", "is", "for", "with", "that",
                   "has", "its", "as", "on", "this", "at", "will", "are", ".", "be", "an", "by", ",", "'", "from",
                   "have", "or", "than", "stock", "stocks", "said", "he", "not", "can", "b13", "they", "when", "some",
                   "their", "we", "it's", "more", "was", "but", "one", "just", "so", "which", "these", "if", "they're",
                   "their", "could", "think", "that's", "there", "you", "get", "market", "very", "been", "year",
                   "other", "his", "right", "even", "any", "**", "percent", "company", "after", "shares", "next",
                   "investor's", "investors", "last", "trade", "price", "business", "zacks", "company's", "here", "inc",
                   "per", "click", "new", "--", "our", "fool", "each", "", "nasdaq", "(", ")", "were", "current",
                   "those", "-", "believe", "financial", "share", "percent.", "*", "", "motley", "over", "nasdaq:",
                   "percent,", "index", "would", "total", "them", "much", "my", "still", "into", "had", "since", "500", "s&p", "friday", "shares", "nasdaq", "trading", "day", "time", "to", "like","pct"]
    b35 = []
    for word in listOfWords:
        if word not in b34:
            b35.append(word)
    return b35
def fonk9(b5):
    b11 = fonk3(b5)
    b36 = ""
    a1 = 0
    for b13 in range(len(b11)):
        b36 = b36 + fonk6(fonk4(b11[b13][1]))
        print("Downloaded [" + str(b13 + 1) + "/" + str(len(b11)) + "]")
    fonk10(b36)
    fonk7(b36.split())
    b37 = int(len(b36) / 5000)
    for b13 in range(b37 - 1):
        b38 = b13 * 5000
        b39 = (b13 + 1) * 5000
        a1 = a1 + fonk5(b36[b38:b39])
        print(a1 / (b13 + 1))
    a1 = a1 + fonk5(b36[b37 * 5000:])
    a1 = a1 / b37
    a1 = a1 * 100
    a1 = int(round(a1))
    return a1
def fonk10(text):
    b40 = open("testfile.txt", "w")
    b40.write(text)
    b40.close()