from LSBSteg import LSBSteg
import cv2
from flask import Flask, render_template, request
b1 = Flask(b14, instance_relative_config=True)
b1.config.update(
    b2 = True,
    b3 = 'secret_xxx'
)
@b1.route('/')
def fonk1():
    return render_template("index.html")
@b1.route('/api/encode', b4 = ['POST'])
def fonk2():
    if request.b5 = = 'POST':
        b6 = request.files['file_gambar']
        b7 = request.form['b7']
        b8 = b6.read()
        b9 = numpy.fromstring(b8, numpy.uint8)
        b10 = cv2.imdecode(b9, cv2.IMREAD_UNCHANGED)
        b11 = LSBSteg(b10)
        b12 = b11.encode_text(b7)
        cv2.imwrite("my_new_image.png", b12)
        return render_template("index.html", b13 = "berhasil menyisipkan")
@b1.route('/api/decode', b4 = ['POST'])
def fonk3():
    b6 = request.files['file_gambar']
    b8 = b6.read()
    b9 = numpy.fromstring(b8, numpy.uint8)
    b10 = cv2.imdecode(b9, cv2.IMREAD_UNCHANGED)
    b11 = LSBSteg(b10)
    b13 = unicode(b11.decode_text(), "utf8")
    print(b13)
    return render_template("index.html", b13 = b13)
if b14 = = '__main__':
    b1.run()