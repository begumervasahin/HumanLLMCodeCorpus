from flask import Flask
from flask import render_template, request
from forms import SearchForm
import math
from tfidf import search as Searching
b1 = Flask(b10)
b1.b2 = 'development'
@b1.route("/")
def fonk1():
    b3 = SearchForm()
    return render_template("index.html", b3 = b3)
@b1.route("/search")
def fonk2():
    b3 = SearchForm()
    b4 = request.args.get('keyword')
    if not request.args.get('a1'):
        a1 = 1
    else:
        a1 = int(request.args.get('a1'))
    b5 = Searching.search_for(b4)
    b6 = len(b5)
    a2 = 5
    b7 = (a1 - 1) * a2
    if (a1 * a2) > b6:
        b8 = b6
    else:
        b8 = a1 * a2
    b9 = math.ceil(b6 / a2)
    return render_template("search.html", b3 = b3, b5=b5, keyword=b4, a1=a1, b7=b7, b8=b8, b9=b9)
if b10 = = '__main__':
   b1.run(b11 = True)