from flask import Flask, request, render_template
import re
import math
b1 = Flask("__name__")
b2 = ""
@b1.route("/")
def fonk1():
	return render_template('index.html', b3 = "")
@b1.route("/", b4 = ['POST'])
def fonk2():
	try:
		b5 = []
		a1 = 0
		b6 = request.form['b3']
		b7 = b6.lower()
		b8 = re.sub("[^\w]", " ",b7).split()
		for b14 in b8:
			if b14 not in b5:
				b5.append(b14)
		b9 = open("b10.txt", "r")
		b10 = b9.read().lower()
		b11 = re.sub("[^\w]", " ",b10).split()
		for b14 in b11:
			if b14 not in b5:
				b5.append(b14)
		b12 = []
		b13 = []
		for b14 in b5:
			a2 = 0
			a3 = 0
			for word2 in b8:
				if b14 = = word2:
					a2 += 1
			b12.append(a2)
			for word2 in b11:
				if b14 = = word2:
					a3 += 1
			b13.append(a3)
		a4 = 0
		for i in range (len(b12)):
			a4 += b12[i]*b13[i]
		a5 = 0
		for i in range (len(b12)):
			a5 += b12[i]**2
		a5 = math.sqrt(a5)
		a6 = 0
		for i in range (len(b13)):
			a6 += b13[i]**2
		a6 = math.sqrt(a6)
		a1 = (float)(a4 / (a5 * a6))*100
		'''
		print b8
		print
		print b11
		print b12
		print
		print b13
		'''
		b15 = "Input b3 text matches %0.02f%% with database."%a1
		return render_template('index.html', b3 = b6, b15=b15)
	except Exception as e:
		b15 = "Please Enter Valid Data"
		return render_template('index.html', b3 = b6, b15=b15)
b1.run()