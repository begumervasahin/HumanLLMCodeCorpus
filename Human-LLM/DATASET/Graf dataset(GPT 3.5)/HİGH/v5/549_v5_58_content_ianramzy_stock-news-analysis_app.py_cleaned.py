from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
b1 = Flask(b25)
@b1.route('/')
def fonk1():
    return render_template("input.html")
@b1.route('/result', b2 = ['POST'])
def fonk2():
    if request.b3 = = 'POST':
        b4 = request.form.get('Name')
        print("Ticker:", b4)
        b5 = str(fonk4(b4))
        print("Sentiment Analysis:", b5)
        b6 = fonk3(b4)[:3]
        b6 = [link[1] for link in b6]
        b7 = 100 - int(b5)
        return render_template("output.html", b5 = b5, b4=b4, b6=b6, b7=b7)
def fonk3(b4):
    b8 = []
    b9 = f"https:
    b10 = requests.get(b9)
    b11 = BeautifulSoup(b10.text, 'html.parser')
    for link in b11.find_all('a'):
        b12 = link.get('href')
        if 'article' in b12 and b12 not in b8:
            b8.append([1, b12])
    print(f"{len(b8)} b8 found")
    return b8
def fonk4(b4):
    b8 = fonk3(b4)
    b13 = ""
    a1 = 0
    for article in b8:
        b13 += fonk5(article[1])
        print(f"Downloaded [{len(b13)} / {len(b8)}]")
    a1 = fonk6(b13)
    return a1
def fonk5(source):
    b14 = requests.get(source).text
    b15 = BeautifulSoup(b14, 'html.parser')
    b16 = [par.text for par in b15.find_all('p')]
    b16 = b16[2:-6]
    return '\n'.join(b16)
def fonk6(text):
    b17 = {'b17': [{'id': '1', 'text': text}]}
    b18 = 'd38ac31a3b2c4e0982d3bc540251a162'
    b19 = 'https:
    b20 = f'{b19}/a1'
    b21 = {"Ocp-Apim-Subscription-Key": b18}
    b22 = requests.post(b20, b21=b21, json=b17)
    b23 = b22.json()
    b24 = b23['b17'][0]['b24']
    return int(round(b24 * 100))
if b25 = = '__main__':
    b1.run(b26 = True)