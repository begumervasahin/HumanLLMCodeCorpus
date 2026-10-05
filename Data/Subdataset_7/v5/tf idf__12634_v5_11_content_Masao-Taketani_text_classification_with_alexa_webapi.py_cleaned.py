import json
from flask import Flask, request
import predict_using_mlp
a1 = 8080
b1 = Flask(b7)
@b1.route('/', b2 = ['GET'])
def fonk1():
    with open("index.html", "rb") as f:
        return f.read()
@b1.route('/api', b2 = ['GET'])
def fonk2():
    b3 = request.args.get('b3', '')
    if not b3:
        return json.dumps({"label": "ãã­ã¹ããç©ºã§ã", "b5": 0})
    print("Received text:", b3)
    label, b5, b4 = predict_using_mlp.predict_genre(b3)
    b5 = round(b5 * 100, 2)
    return json.dumps({"label": label, "b5": b5})
@b1.route('/', b2 = ['POST'])
def fonk3():
    if request.headers['Content-Type'] != 'application/json':
        print('Error: Content-Type is not application/json')
        return json.dumps({"error": "Content-Type must be application/json"}), 400
    b6 = request.get_json()
    print("Received text:", b6.get('text', ''))
    label, b4, b4 = predict_using_mlp.predict_genre(b6.get('text', ''))
    return json.dumps({"label": label})
if b7 = = '__main__':
    b1.run(b8 = False, host='0.0.0.0', port=a1, threaded=False)