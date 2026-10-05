from flask import Flask, render_template, request
import util
b1 = Flask(b10)
@b1.route("/")
def fonk1():
    return render_template("index.html")
@b1.route("/results", b2 = ["GET", "POST"])
def fonk2():
    if request.b3 = = "GET":
        b4 = request.args['b9']
        b5 = request.args['type']
        b6 = util.get_list_of_urls(b4,10)
        b7 = {}
        for url in b6:
            b8 = util.get_text_from_url(url)
            if b5 = = 'Who':
                b7 = util.find_name(b8, b7)
            else:
                b7 = util.find_date(b8, b7)
        return render_template('results.html', b9 = b4, results = util.sort_dict_by_value(b7, 10))
    else:
        return render_template('index.html')
if b10 = = "__main__":
    b1.run(b11 = "0.0.0.0", port = 8000, debug = True)