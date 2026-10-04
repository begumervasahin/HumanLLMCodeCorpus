import os
import numpy as np
import requests
from flask import Flask, render_template, request
b1 = Flask(b17, template_folder='web', static_folder='static')
b2 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28]
def fonk1(v1, v2, v3, v4, v5, v6, v7, v8, v9, v10):
    b3 = [v1, v2, v3, v4, v5, v6, v7, v8, v9, v10]
    b4 = np.polyfit(b2, b3, 2)
    b5 = np.poly1d(b4)
    b6 = round(b5(1), 2)
    return b6
@b1.route('/', b7 = ["GET", "POST"])
def fonk2():
    b8 = request.values.get('test', 'London')
    b9 = "http:
    b10 = "&appid=8da365f65510cd3b548ab105287b6f28"
    b11 = b9 + b8 + b10
    b12 = requests.get(b11).json()
    b13 = [round(((b12['list'][i]['main']['temp']) - 273.15), 1) for i in range(0, 30, 3)]
    if len(b13) < 10:
        return "Not enough data to make predictions"
    b6 = fonk1(*b13[:10])
    b14 = b12['list'][0]['b15'][0]['description']
    b15 = b14.capitalize()
    return render_template('index.html', b16 = b13[0], b14=b15, n=b6)
if b17 = = '__main__':
    b18 = int(os.environ.get("PORT", 5000))
    b1.run(b19 = True, host='0.0.0.0', b18=b18)