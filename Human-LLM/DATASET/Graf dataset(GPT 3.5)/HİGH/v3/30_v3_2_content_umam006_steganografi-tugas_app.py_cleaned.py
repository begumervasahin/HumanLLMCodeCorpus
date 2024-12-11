
from LSBSteg import LSBSteg
import cv2
from flask import Flask, render_template, request
import numpy as np
b1 = Flask(b14, instance_relative_config=True)
b1.config['DEBUG'] = True
b1.config['SECRET_KEY'] = 'secret_xxx'
@b1.route('/')
def fonk1():
    return render_template("index.html")
def fonk2(b8, b9):
    b2 = np.fromstring(b8.read(), np.uint8)
    b3 = cv2.imdecode(b2, cv2.IMREAD_UNCHANGED)
    b4 = LSBSteg(b3)
    b5 = b4.encode_text(b9)
    cv2.imwrite("my_new_image.png", b5)
    return "berhasil menyisipkan"
@b1.route('/api/encode', b6 = ['POST'])
def fonk3():
    if request.b7 = = 'POST':
        b8 = request.files['file_gambar']
        b9 = request.form['b9']
        b10 = fonk2(b8, b9)
        return render_template("index.html", b11 = b10)
def fonk4(b8):
    b2 = np.fromstring(b8.read(), np.uint8)
    b3 = cv2.imdecode(b2, cv2.IMREAD_UNCHANGED)
    b4 = LSBSteg(b3)
    b12 = b4.decode_text().fonk5("utf-8")
    return b12
@b1.route('/api/decode', b6 = ['POST'])
def fonk5():
    b8 = request.files['file_gambar']
    b13 = fonk4(b8)
    print(b13)
    return render_template("index.html", b11 = b13)
if b14 = = '__main__':
    b1.run()
