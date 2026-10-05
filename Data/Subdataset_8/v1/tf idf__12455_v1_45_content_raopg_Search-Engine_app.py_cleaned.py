from flask import Flask, render_template, redirect, url_for, request
import scripts
import index
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def indexpage():
    '''Returns the landing page of the search engine web application'''
    if request.method == 'GET':
        return render_template('index.html')
    else:
        return redirect(url_for('querypage', query=request.form['query']))
@app.route('/results', methods=['POST'])
def querypage():
    '''This function handles the query by the user, and displays the results'''
    query = request.form['query']
    message = None
    search_results = []
    try:
        search_results = index.handle_query(query.lower())
    except KeyError:
        message = "No search results found! Given search term is a stopword"
    return render_template('results.html', query_str=query, results=search_results, error_message=message)
if __name__ == "__main__":
    app.run(debug=True)