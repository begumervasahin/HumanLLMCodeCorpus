from flask import Flask, render_template, redirect, url_for, request
import scripts
import index
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index_page():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        query = request.form['query']
        return redirect(url_for('query_page', query=query))
@app.route('/results', methods=['POST'])
def query_page():
    query = request.form['query']
    message = None
    try:
        search_results = index.handle_query(query.lower())
    except KeyError:
        message = "No search results found! The given search term is a stopword"
    return render_template('results.html', query_str=query, results=search_results, error_message=message)
if __name__ == "__main__":
    app.run(debug=True)