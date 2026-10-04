import os
import numpy as np
import requests
from flask import Flask, render_template, request
b1 = Flask(b27, template_folder='web', static_folder='static')
b2 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28]
def fonk1(v1, v2, v3, v4, v5, v6, v7, v8, v9, v10):
    b3 = []
    b3.append(v1)
    b3.append(v2)
    b3.append(v3)
    b3.append(v4)
    b3.append(v5)
    b3.append(v6)
    b3.append(v7)
    b3.append(v8)
    b3.append(v9)
    b3.append(v10)
    b4 = np.polyfit(b2, b3, 2)
    b5 = np.poly1d(b4)
    b6 = round(b5(1), 2)
    return b6
@b1.route('/', b7 = ["GET", "POST"])
def fonk2():
    b8 = str(request.values.get('test'))
    b9 = "http:
    b10 = "&appid=8da365f65510cd3b548ab105287b6f28"
    b11 = b9 + b8 + b10
    b12 = requests.get(b11).json()
    b13 = round(((b12['list'][0]['main']['b13']) - 273), 1)
    b14 = round(((b12['list'][1]['main']['b13']) - 273), 1)
    b15 = round(((b12['list'][4]['main']['b13']) - 273), 1)
    b16 = round(((b12['list'][7]['main']['b13']) - 273), 1)
    b17 = round(((b12['list'][10]['main']['b13']) - 273), 1)
    b18 = round(((b12['list'][13]['main']['b13']) - 273), 1)
    b19 = round(((b12['list'][16]['main']['b13']) - 273), 1)
    b20 = round(((b12['list'][19]['main']['b13']) - 273), 1)
    b21 = round(((b12['list'][22]['main']['b13']) - 273), 1)
    b22 = round(((b12['list'][25]['main']['b13']) - 273), 1)
    b23 = round(((b12['list'][28]['main']['b13']) - 273), 1)
    b6 = fonk1(b14, b15, b16, b17, b18, b19, b20, b21, b22, b23)
    b24 = b12['list'][0]['b25'][0]['description']
    b25 = b24.capitalize()
    return render_template('index.html', b26 = b13, b24=b25, n=b6)
if b27 = = '__main__':
    b28 = int(os.environ.get("PORT", 5000))
    b1.run(b29 = True, host='0.0.0.0', b28=b28)