from flask import Flask, jsonify, Response
app = Flask(__name__)
@app.route('/fibonacci/<int:end_number>', methods=['GET'])
def get_fibonacci_sequence(end_number: int) -> Response:
    if end_number == 0:
        return jsonify([])
    elif end_number > 0:
        return jsonify(generate_fibonacci_sequence(end_number))
    else:
        return handle_invalid_usage()
def generate_fibonacci_sequence(n: int) -> list:
    result = []
    a, b = 0, 1
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result
@app.errorhandler(400)
def handle_invalid_usage(error=None) -> Response:
    response = jsonify(message="Please enter a positive number only")
    response.status_code = 400
    return response
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)