from flask import Flask, render_template, request
def get_list_of_urls(query, num_results):
    return [f"https:
def get_text_from_url(url):
    return f"Text from {url}"
def find_name(text, results):
    return {"Name1": 5, "Name2": 3}
def find_date(text, results):
    return {"2023-01-01": 10, "2023-02-01": 7}
def sort_dict_by_value(dictionary, limit):
    return {k: v for k, v in sorted(dictionary.items(), key=lambda item: item[1], reverse=True)[:limit]}
app = Flask(__name__)
@app.route("/")
def root():
    return render_template("index.html")
@app.route("/results", methods=["GET", "POST"])
def results():
    if request.method == "GET":
        query = request.args.get('question', '')
        mode = request.args.get('type', '')
        urls = get_list_of_urls(query, 10)
        current_results = {}
        for url in urls:
            text = get_text_from_url(url)
            if mode == 'Who':
                current_results = find_name(text, current_results)
            else:
                current_results = find_date(text, current_results)
        sorted_results = sort_dict_by_value(current_results, 10)
        return render_template('results.html', question=query, results=sorted_results)
    else:
        return render_template('index.html')
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)