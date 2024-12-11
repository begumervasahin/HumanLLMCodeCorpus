from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
b1 = Flask(b32)
@b1.route('/')
def fonk1():
    return render_template("input.html")
@b1.route('/result', b2 = ['POST', 'GET'])
def fonk2():
    if request.b3 = = 'POST':
        b4 = request.form.get('Name')
        b5 = str(fonk5(b4))
        b6 = fonk3(b4)
        b6 = [link[1] for link in b6[:3]]
        b7 = 100 - int(b5)
        return render_template("output.html", b5 = b5, b4=b4, b6=b6, otherHalf=b7)
def fonk3(b4):
    b8 = []
    b9 = f"https:
    b10 = requests.get(b9)
    b11 = b10.text
    b12 = BeautifulSoup(b11, 'html.parser')
    for link in b12.find_all('a'):
        b13 = link.get('href')
        if 'article' == b13[23:30] and b13 not in b8:
            b14 = str(link.parent.parent.find('small'))[31:41]
            b14 = b14.strip(" ").split("/")
            if b14 != ['']:
                b8.append([1, b13])
    print(f"{len(b8)} b8 found")
    return b8
def fonk4(source):
    b11 = requests.get(source).text
    b15 = BeautifulSoup(b11, 'html.parser')
    b16 = [par.text for par in b15.find_all('p')]
    b16 = b16[2:-6]
    b17 = '\n'.join(b16)
    return b17
def fonk5(b4):
    b8 = fonk3(b4)
    b18 = ""
    a1 = 0
    for article in b8:
        b18 += fonk7(fonk4(article[1]))
    b19 = len(b18)
    for i in range(b19):
        b20 = i * 5000
        b21 = (i + 1) * 5000
        a1 += fonk6(b18[b20:b21])
    a1 += fonk6(b18[b19 * 5000:])
    a1 /= b19
    a1 *= 100
    a1 = int(round(a1))
    return a1
def fonk6(text):
    b22 = {'b22': [{'id': '1', 'text': text}]}
    b23 = 'YOUR_AZURE_KEY'
    b24 = 'YOUR_AZURE_ENDPOINT'
    b25 = f"{b24}/a1"
    b26 = {"Ocp-Apim-Subscription-Key": b23}
    b27 = requests.post(b25, b26=b26, json=b22)
    b28 = b27.json()
    b28 = b28['b22'][0]['score']
    return b28
def fonk7(text):
    b29 = ["bear", "bearish", "underperform", "underperforming", "sell", "selling", "sold", "decrease",
                "decreasing", "falling", "fall", "fell", "down", "lose", "lost", "losses", "losing", "downturn",
                "short", "shorting", "downside", "risky", "decline", "declining", "fear", "fears", "sell-off"]
    b30 = ["bull", "bullish", "overperform", "overperforming", "buy", "buying", "bought", "increase",
                 "increasing", "rising", "rise", "rised", "up", "gain", "gains", "gained", "profit", "profited","profitable", "profiting", "upturn", "upside"]
    b31 = text.split(" ")
    b31 = ["bad" if word in b29 else word for word in b31]
    b31 = ["good" if word in b30 else word for word in b31]
    return " ".join(b31)
if b32 = = '__main__':
    b1.run(b33 = True)