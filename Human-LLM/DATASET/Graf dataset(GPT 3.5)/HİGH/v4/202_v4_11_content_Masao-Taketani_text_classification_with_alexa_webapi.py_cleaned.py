
import json
import flask
from flask import request
import predict_using_mlp
a1 = 8080
b1 = flask.Flask(b8)
@b1.route('/', b2 = ['GET'])
def fonk1():
    with open("index.html", "rb") as f:
        return f.read()
@b1.route('/api', b2 = ['GET'])
def fonk2():
    b3 = request.args.get('b3', '')
    if b3 = = '':
        return '{"label": "ãã­ã¹ããç©ºã§ã", "b5":0}'
    print("b3 = ", b3)
    label, b5, b4 = predict_using_mlp.predict_genre(b3)
    b5 = round(b5 * 100, 2)
    return json.dumps({
        "label": label,
        "b5": b5
    })
@b1.route('/', b2 = ['POST'])
def fonk3():
    if request.headers['Content-Type'] != 'application/json':
        print('Content-Type:', request.headers['Content-Type'])
        return flask.jsonify(b6 = 'error'), 400
    else:
        b7 = request.get_json()
        print(b7['text'])
        label, b4, b4 = predict_using_mlp.predict_genre(b7['text'])
        return json.dumps({"label": label})
if b8 = = '__main__':
    b1.run(b9 = False, host='0.0.0.0', port=a1, threaded=False)