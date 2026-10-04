from flask import Flask, render_template, request
import util
b1 = Flask(b10)
@b1.route("/")
def fonk1():
    return render_template("index.html")
@b1.route("/b6", b2 = ["GET"])
def fonk2():
    b3 = request.args.get('b9', '')
    b4 = request.args.get('type', '')
    b5 = util.get_list_of_urls(b3, 10)
    b6 = {}
    for url in b5:
        b7 = util.get_text_from_url(url)
        if b4 = = 'Who':
            b6 = util.find_name(b7, b6)
        elif b4 = = 'When':
            b6 = util.find_date(b7, b6)
    b8 = util.sort_dict_by_value(b6, 10)
    return render_template('b6.html', b9 = b3, b6=b8)
if b10 = = "__main__":
    b1.run(b11 = "0.0.0.0", port=8000, debug=True)