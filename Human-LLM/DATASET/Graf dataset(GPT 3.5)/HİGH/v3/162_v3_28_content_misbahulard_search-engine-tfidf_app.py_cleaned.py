from flask import Flask, render_template, request
from forms import SearchForm
import math
from tfidf import search as Searching
b1 = Flask(b11)
b1.b2 = 'development'
@b1.route("/")
def fonk1():
    b3 = SearchForm()
    return render_template("index.html", b3 = b3)
@b1.route("/search")
def fonk2():
    b3 = SearchForm()
    b4 = request.args.get('keyword')
    b5 = int(request.args.get('b5', 1))
    b6 = Searching.search_for(b4)
    b7 = len(b6)
    a1 = 5
    b8 = (b5 - 1) * a1
    b9 = min(b8 + a1, b7)
    b10 = math.ceil(b7 / a1)
    return render_template("search.html", b3 = b3, b6=b6, keyword=b4, b5=b5, b8=b8, b9=b9, b10=b10)
if b11 = = '__main__':
   b1.run(b12 = True)