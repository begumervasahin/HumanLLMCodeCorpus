from flask import Flask, render_template, request
import util
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/results", methods=["GET", "POST"])
def results():
    if request.method == "GET":
        query = request.args.get('question', '').strip()
        mode = request.args.get('type', '').strip()
        if not query or not mode:
            return render_template('index.html', error="Both 'question' and 'type' must be provided.")
        urls = util.get_list_of_urls(query, 10)
        results = {}
        for url in urls:
            text = util.get_text_from_url(url)
            if mode == 'Who':
                results = util.find_name(text, results)
            elif mode == 'When':
                results = util.find_date(text, results)
            else:
                return render_template('index.html', error="Invalid 'type' provided. Use 'Who' or 'When'.")
        sorted_results = util.sort_dict_by_value(results, 10)
        return render_template('results.html', question=query, results=sorted_results)
    return render_template('index.html')
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)