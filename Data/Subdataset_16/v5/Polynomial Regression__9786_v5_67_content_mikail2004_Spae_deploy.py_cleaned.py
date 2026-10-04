import os
import numpy as np
import requests
from flask import Flask, render_template, request
b1 = Flask(b17, template_folder='web', static_folder='static')
b2 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28]
def fonk1(temperature_values):
    b3 = np.polyfit(b2, temperature_values, 2)
    b4 = np.poly1d(b3)
    b5 = round(b4(1), 2)
    return b5
@b1.route('/', b6 = ["GET", "POST"])
def fonk2():
    b7 = request.values.get('test', type=str)
    b8 = "8da365f65510cd3b548ab105287b6f28"
    b9 = f"http:
    b10 = requests.get(b9)
    b11 = b10.json()
    b12 = [
        round(b11['list'][i]['main']['temp'] - 273.15, 1)
        for i in [0, 1, 4, 7, 10, 13, 16, 19, 22, 25, 28]
    ]
    b13 = b12[0]
    b14 = b12[1:]
    b5 = fonk1(b14)
    b15 = b11['list'][0]['weather'][0]['description'].capitalize()
    return render_template('index.html', b16 = b13, w=b15, n=b5)
if b17 = = '__main__':
    b18 = int(os.environ.get("PORT", 5000))
    b1.run(b19 = True, host='0.0.0.0', b18=b18)