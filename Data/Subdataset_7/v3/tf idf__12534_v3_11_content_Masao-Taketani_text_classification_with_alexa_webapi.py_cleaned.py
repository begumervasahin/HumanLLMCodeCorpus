import json
from flask import Flask, request
import predict_using_mlp
a1 = 8080
b1 = False
b2 = '0.0.0.0'
b3 = Flask(b9)
@b3.route('/', b4 = ['GET'])
def fonk1():
    with open("index.html", "rb") as f:
        return f.read()
@b3.route('/api', b4 = ['GET'])
def fonk2():
    b5 = request.args.get('b5', '')
    if not b5:
        return json.dumps({"label": "ãã­ã¹ããç©ºã§ã", "b7": 0})
    print("Received query:", b5)
    label, b7, b6 = predict_using_mlp.predict_genre(b5)
    b7 = round(b7 * 100, 2)
    return json.dumps({"label": label, "b7": b7})
@b3.route('/', b4 = ['POST'])
def fonk3():
    if request.headers['Content-Type'] != 'application/json':
        print('Invalid Content-Type:', request.headers['Content-Type'])
        return json.dumps({"res": "error"}), 400
    else:
        b8 = request.get_json()
        print("Received text:", b8['text'])
        label, b6, b6 = predict_using_mlp.predict_genre(b8['text'])
        return json.dumps({"label": label})
if b9 = = '__main__':
    b3.run(b10 = b1, host=b2, port=a1, threaded=False)