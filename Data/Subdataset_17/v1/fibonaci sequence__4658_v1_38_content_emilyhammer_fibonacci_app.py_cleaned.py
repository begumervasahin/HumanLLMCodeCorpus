from flask import Flask, jsonify
app = Flask(__name__)
@app.route('/fibonacci/<int:end_number>', methods=['GET'])
def get_fibonacci_sequence(end_number):
    if end_number == 0:
        return jsonify([])
    elif end_number > 0:
        return jsonify(fib(end_number))
    else:
        return handle_invalid_usage(400)
def fib(n):
    result = []
    a, b = 0, 1
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result
@app.errorhandler(404)
def handle_invalid_usage(error):
    response = jsonify(message="Please enter a positive number only")
    response.status_code = 400
    return response
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)