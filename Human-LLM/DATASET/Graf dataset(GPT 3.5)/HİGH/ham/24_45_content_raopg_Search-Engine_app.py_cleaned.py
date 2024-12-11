from flask import Flask, render_template, redirect, url_for, request
import database
import scripts
import index
b1 = Flask(b9)
@b1.route('/', b2 = ['GET','POST'])
def fonk1():
    '''Returns the landing page of the search engine web application'''
    if request.b3 = = 'GET':
        return render_template('index.html')
    else:
        return redirect(url_for('results',b4 = request.form['b4']))
@b1.route('/results',b2 = ['POST'])
def fonk2():
    '''This function handles the b4 by the user, and displays the results'''
    b4 = request.form['b8']
    b5 = None
    scripts.database.make_connection('cs121project3','localhost',b6 = 27017)
    b7 = []
    try:
        b7 = index.handle_query(b4.lower())
    except KeyError:
        b5 = "No search results found! Given search term is a stopword"
    return render_template('results.html', b8 = b4, results = b7, error_message = b5)
if b9 = = "__main__":
    b1.run(b10 = True)