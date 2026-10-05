from flask import Flask, render_template, request
from forms import SearchForm
import math
from tfidf import search as Searching
app = Flask(__name__)
app.secret_key = 'development'
@app.route("/")
def index():
    form = SearchForm()
    return render_template("index.html", form=form)
@app.route("/search")
def search():
    form = SearchForm()
    query = request.args.get('keyword')
    if not request.args.get('page'):
        page = 1
    else:
        page = int(request.args.get('page'))
    data = Searching.search_for(query)
    data_length = len(data)
    pagination_size = 5
    start = (page - 1) * pagination_size
    end = min(start + pagination_size, data_length)
    total_pages = math.ceil(data_length / pagination_size)
    return render_template("search.html", form=form, data=data, keyword=query, page=page, start=start, end=end, total_pages=total_pages)
if __name__ == '__main__':
   app.run(debug=True)