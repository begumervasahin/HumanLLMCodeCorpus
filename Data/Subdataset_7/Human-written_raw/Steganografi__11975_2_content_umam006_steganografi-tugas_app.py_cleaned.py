from LSBSteg import LSBSteg
import cv2
from flask import Flask, render_template, request, redirect, session, Response, abort
import json
import numpy
b1 = Flask(b13, instance_relative_config=True)
b1.config.update(
    b2 = True,
    b3 = 'secret_xxx'
)
@b1.route('/')
def fonk1():
	return render_template("index.html")
@b1.route('/api/encode',b4 = ['POST'])
def fonk2():
	if request.b5 = = 'POST':
		b6 = request.files['file_gambar']
		b7 = request.form['b7']
		b8 = numpy.fromstring(b6.read(), numpy.uint8)
		b9 = LSBSteg(cv2.imdecode(b8, cv2.IMREAD_UNCHANGED))
		b10 = b9.encode_text(b7)
		cv2.imwrite("my_new_image.png", b10)
		return render_template("index.html", b11 = "berhasil menyisipkan")
@b1.route('/api/decode',b4 = ['POST'])
def fonk3():
	b6 = request.files['file_gambar']
	b8 = numpy.fromstring(b6.read(), numpy.uint8)
	b12 = cv2.imdecode(b8, cv2.IMREAD_UNCHANGED)
	b9 = LSBSteg(b12)
	b11 = unicode(b9.decode_text(), "utf8")
	print(b11)
	return render_template("index.html",b11 = b11)
if b13 = = '__main__':
    b1.run()