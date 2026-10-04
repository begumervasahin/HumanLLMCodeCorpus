from flask import Flask, render_template, request
import util
b1 = Flask(b11)
@b1.route("/")
def fonk1():
    return render_template("index.html")
@b1.route("/b7", b2 = ["GET"])
def fonk2():
    b3 = request.args.get('b10', '').strip()
    b4 = request.args.get('type', '').strip()
    if not b3 or not b4:
        return render_template('index.html', b5 = "Both 'b10' and 'type' must be provided.")
    if b4 not in ['Who', 'When']:
        return render_template('index.html', b5 = "Invalid 'type' provided. Use 'Who' or 'When'.")
    b6 = util.get_list_of_urls(b3, 10)
    b7 = {}
    for url in b6:
        b8 = util.get_text_from_url(url)
        if b4 = = 'Who':
            b7 = util.find_name(b8, b7)
        elif b4 = = 'When':
            b7 = util.find_date(b8, b7)
    b9 = util.sort_dict_by_value(b7, 10)
    return render_template('b7.html', b10 = b3, b7=b9)
if b11 = = "__main__":
    b1.run(b12 = "0.0.0.0", port=8000, debug=True)