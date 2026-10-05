import json
from flask import Flask, request
import predict_using_mlp
PORT_NO = 8080
app = Flask(__name__)
@app.route('/', methods=['GET'])
def home():
    with open("index.html", "rb") as f:
        return f.read()
@app.route('/api', methods=['GET'])
def predict_genre_api():
    q = request.args.get('q', '')
    if not q:
        return json.dumps({"label": "ãã­ã¹ããç©ºã§ã", "percent": 0})
    print("Received text:", q)
    label, percent, _ = predict_using_mlp.predict_genre(q)
    percent = round(percent * 100, 2)
    return json.dumps({"label": label, "percent": percent})
@app.route('/', methods=['POST'])
def predict_genre_post():
    if request.headers['Content-Type'] != 'application/json':
        print('Error: Content-Type is not application/json')
        return json.dumps({"error": "Content-Type must be application/json"}), 400
    data = request.get_json()
    print("Received text:", data.get('text', ''))
    label, _, _ = predict_using_mlp.predict_genre(data.get('text', ''))
    return json.dumps({"label": label})
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=PORT_NO, threaded=False)