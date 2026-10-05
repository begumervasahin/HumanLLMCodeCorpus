import json
from flask import Flask, request
import predict_using_mlp
PORT_NO = 8080
DEBUG_MODE = False
HOST = '0.0.0.0'
app = Flask(__name__)
@app.route('/', methods=['GET'])
def index():
    with open("index.html", "rb") as f:
        return f.read()
@app.route('/api', methods=['GET'])
def api():
    q = request.args.get('q', '')
    if not q:
        return json.dumps({"label": "ãã­ã¹ããç©ºã§ã", "percent": 0})
    print("Received query:", q)
    label, percent, _ = predict_using_mlp.predict_genre(q)
    percent = round(percent * 100, 2)
    return json.dumps({"label": label, "percent": percent})
@app.route('/', methods=['POST'])
def api_2():
    if request.headers['Content-Type'] != 'application/json':
        print('Invalid Content-Type:', request.headers['Content-Type'])
        return json.dumps({"res": "error"}), 400
    else:
        data = request.get_json()
        print("Received text:", data['text'])
        label, _, _ = predict_using_mlp.predict_genre(data['text'])
        return json.dumps({"label": label})
if __name__ == '__main__':
    app.run(debug=DEBUG_MODE, host=HOST, port=PORT_NO, threaded=False)