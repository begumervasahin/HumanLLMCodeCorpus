from flask import Flask
from flask import jsonify
app = Flask(__name__)
@app.route('/fibonacci/<int:endNumber>', methods=['GET'])
def index(endNumber):
    if endNumber == 0:
        return ""
    elif int(endNumber) > 0:
        return str(fib(endNumber)) +'\n'
    else:
        return handle_invalid_usage
def fib(n):
    result = []
    a, b = 0, 1
    for i in range(n):
       result.append(a)
       a, b = b, a+b
    return result
@app.errorhandler(404)
def handle_invalid_usage(error):
    response = jsonify("Please enter a positive number only")
    response.status_code = 400
    return response
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)