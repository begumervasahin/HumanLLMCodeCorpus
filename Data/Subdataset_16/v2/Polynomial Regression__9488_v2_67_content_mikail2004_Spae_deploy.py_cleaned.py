import os
import numpy as np
import requests
from flask import Flask, render_template, request
b1 = Flask(b14, template_folder='web', static_folder='static')
b2 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28]
def fonk1(*temps):
    b3 = np.polyfit(b2, temps, 2)
    b4 = np.poly1d(b3)
    b5 = round(b4(1), 2)
    return b5
@b1.route('/', b6 = ["GET", "POST"])
def fonk2():
    b7 = request.values.get('test', 'London')
    b8 = f"http:
    b9 = requests.get(b8)
    b10 = b9.json()
    b11 = [
        round(b10['list'][i]['main']['temp'] - 273.15, 1)
        for i in range(0, 30, 3)
    ]
    if len(b11) < 10:
        return "Not enough data to make predictions"
    b5 = fonk1(*b11[:10])
    b12 = b10['list'][0]['weather'][0]['description'].capitalize()
    return render_template('index.html', b13 = b11[0], w=b12, n=b5)
if b14 = = '__main__':
    b15 = int(os.environ.get("PORT", 5000))
    b1.run(b16 = True, host='0.0.0.0', b15=b15)