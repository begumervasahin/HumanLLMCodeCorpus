from flask import Flask, request, render_template
import re
import math
b1 = Flask(b17)
b2 = set()
@b1.route("/")
def fonk1():
    return render_template('index.html', b3 = "")
@b1.route("/", b4 = ['POST'])
def fonk2():
    try:
        global b2
        b5 = request.form['b3']
        b6 = b5.lower()
        b7 = re.findall(r'\w+', b6)
        b2.update(b7)
        with open("database1.txt", "r") as file:
            b8 = file.read().lower()
            b9 = re.findall(r'\w+', b8)
            b2.update(b9)
        b10 = [b7.count(word) for word in b2]
        b11 = [b9.count(word) for word in b2]
        b12 = sum(b10[i] * b11[i] for i in range(len(b10)))
        b13 = math.sqrt(sum(tf ** 2 for tf in b10))
        b14 = math.sqrt(sum(tf ** 2 for tf in b11)))
        b15 = (b12 / (b13 * b14)) * 100
        b16 = f"Input b3 text matches {b15:.02f}% with database."
        return render_template('index.html', b3 = b5, b16=b16)
    except Exception as e:
        b16 = "Please Enter Valid Data"
        return render_template('index.html', b3 = b5, b16=b16)
if b17 = = "__main__":
    b1.run()