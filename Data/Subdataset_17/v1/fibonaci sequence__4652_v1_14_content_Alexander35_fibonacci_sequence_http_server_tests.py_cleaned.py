from flask import Flask, request, jsonify
app = Flask(__name__)
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
@app.route('/fibonacci')
def fibonacci_route():
    start = int(request.args.get('from'))
    end = int(request.args.get('to'))
    result = {i: fibonacci(i) for i in range(start, end)}
    return jsonify(result)
@app.route('/get-sequence')
def get_sequence_route():
    start = int(request.args.get('from'))
    end = int(request.args.get('to'))
    result = {i: fibonacci(i) for i in range(start, end)}
    return jsonify(result)
if __name__ == '__main__':
    app.run(port=5000)