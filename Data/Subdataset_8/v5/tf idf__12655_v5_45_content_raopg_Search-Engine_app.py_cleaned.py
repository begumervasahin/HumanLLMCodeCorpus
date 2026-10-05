from flask import Flask, render_template, redirect, url_for, request
import database
import scripts
import index
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index_page():
    '''Renders the landing page of the search engine web application'''
    if request.method == 'GET':
        return render_template('index.html')
    else:
        return redirect(url_for('results', query=request.form['query']))
@app.route('/results', methods=['POST'])
def query_page():
    '''Handles user queries and displays the results'''
    query = request.form['query_str']
    error_message = None
    scripts.database.make_connection('cs121project3', 'localhost', port=27017)
    search_results = []
    try:
        search_results = index.handle_query(query.lower())
    except KeyError:
        error_message = "No search results found! The given search term is a stopword"
    return render_template('results.html', query_str=query, results=search_results, error_message=error_message)
if __name__ == "__main__":
    app.run(debug=True)