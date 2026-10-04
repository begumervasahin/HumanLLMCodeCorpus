from flask import Flask, render_template, request
import util
app = Flask(__name__)
@app.route("/")
def root():
    return render_template("index.html")
@app.route("/results", methods=["GET", "POST"])
def results():
    if request.method == "GET":
        query = request.args.get('question', '')
        mode = request.args.get('type', '')
        urls = util.get_list_of_urls(query, 10)
        current_results = {}
        for url in urls:
            text = util.get_text_from_url(url)
            if mode == 'Who':
                current_results = util.find_name(text, current_results)
            else:
                current_results = util.find_date(text, current_results)
        sorted_results = util.sort_dict_by_value(current_results, 10)
        return render_template('results.html', question=query, results=sorted_results)
    else:
        return render_template('index.html')
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)