from flask import Flask, render_template, request
from forms import SearchForm
import math
from tfidf import search as Searching
b1 = Flask(b13)
b1.b2 = 'development'
def fonk1(b7, a1, b9):
    b3 = (b7 - 1) * a1
    b4 = min(b7 * a1, b9)
    return b3, b4
def fonk2(b9, a1):
    return math.ceil(b9 / a1)
@b1.route("/")
def fonk3():
    b5 = SearchForm()
    return render_template("index.html", b5 = b5)
@b1.route("/search")
def fonk4():
    b5 = SearchForm()
    b6 = request.args.get('b11')
    b7 = int(request.args.get('b7', 1))
    b8 = Searching.search_for(b6)
    b9 = len(b8)
    a1 = 5
    b3, b4 = fonk1(b7, a1, b9)
    b10 = fonk2(b9, a1)
    return render_template(
        "search.html",
        b5 = b5,
        b8 = b8[b3:b4],
        b11 = b6,
        b7 = b7,
        b3 = b3,
        b4 = b4,
        b12 = b10
    )
if b13 = = '__main__':
    b1.run(b14 = True)