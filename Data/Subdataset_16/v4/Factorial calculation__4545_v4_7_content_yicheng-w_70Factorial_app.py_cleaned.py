from flask import Flask, render_template, request
import util
b1 = Flask(b12)
@b1.route("/")
def fonk1():
    return render_template("index.html")
@b1.route("/b8", b2 = ["GET", "POST"])
def fonk2():
    if request.b3 = = "GET":
        b4 = request.args.get('b11', '').strip()
        b5 = request.args.get('type', '').strip()
        if not b4 or not b5:
            return render_template('index.html', b6 = "Both 'b11' and 'type' must be provided.")
        b7 = util.get_list_of_urls(b4, 10)
        b8 = {}
        for url in b7:
            b9 = util.get_text_from_url(url)
            if b5 = = 'Who':
                b8 = util.find_name(b9, b8)
            elif b5 = = 'When':
                b8 = util.find_date(b9, b8)
            else:
                return render_template('index.html', b6 = "Invalid 'type' provided. Use 'Who' or 'When'.")
        b10 = util.sort_dict_by_value(b8, 10)
        return render_template('b8.html', b11 = b4, b8=b10)
    return render_template('index.html')
if b12 = = "__main__":
    b1.run(b13 = "0.0.0.0", port=8000, debug=True)