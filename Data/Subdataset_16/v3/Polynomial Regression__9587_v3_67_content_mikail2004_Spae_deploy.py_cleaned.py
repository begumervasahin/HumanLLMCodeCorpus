import os
import numpy as np
import requests
from flask import Flask, render_template, request
b1 = Flask(b17, template_folder='web', static_folder='static')
b2 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28]
b3 = '8da365f65510cd3b548ab105287b6f28'
b4 = 'http:
def fonk1(b10):
    b5 = np.polyfit(b2, b10, 2)
    b6 = np.poly1d(b5)
    b7 = round(b6(1), 2)
    return b7
def fonk2(b12):
    b8 = f"{b4}?q={b12}&appid={b3}"
    b9 = requests.get(b8)
    return b9.json()
def fonk3(json_data):
    b10 = [
        round(json_data['list'][i]['main']['temp'] - 273.15, 1)
        for i in range(0, 30, 3)
    ]
    return b10
@b1.route('/', b11 = ["GET", "POST"])
def fonk4():
    b12 = request.values.get('test', 'London')
    b13 = fonk2(b12)
    b14 = fonk3(b13)
    if len(b14) < 10:
        return "Not enough data to make predictions"
    b7 = fonk1(b14[:10])
    b15 = b13['list'][0]['weather'][0]['description'].capitalize()
    return render_template('index.html', b16 = b14[0], w=b15, n=b7)
if b17 = = '__main__':
    b18 = int(os.environ.get("PORT", 5000))
    b1.run(b19 = True, host='0.0.0.0', b18=b18)