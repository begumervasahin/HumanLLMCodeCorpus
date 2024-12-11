from flask import Flask, render_template, redirect, url_for, request
import scripts
import index
b1 = Flask(b8)
@b1.route('/', b2 = ['GET', 'POST'])
def fonk1():
    if request.b3 = = 'GET':
        return render_template('index.html')
    else:
        b4 = request.form['b4']
        return redirect(url_for('query_page', b4 = b4))
@b1.route('/results', b2 = ['POST'])
def fonk2():
    b4 = request.form['b4']
    b5 = None
    try:
        b6 = index.handle_query(b4.lower())
    except KeyError:
        b5 = "No search results found! The given search term is a stopword"
    return render_template('results.html', b7 = b4, results=b6, error_message=b5)
if b8 = = "__main__":
    b1.run(b9 = True)