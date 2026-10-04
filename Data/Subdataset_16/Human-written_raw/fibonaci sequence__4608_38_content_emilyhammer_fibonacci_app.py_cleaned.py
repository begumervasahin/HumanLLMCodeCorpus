from flask import Flask
from flask import jsonify
b1 = Flask(b7)
@b1.route('/fibonacci/<int:b3>', b2 = ['GET'])
def fonk1(b3):
    if b3 = = 0:
        return ""
    elif int(b3) > 0:
        return str(fonk2(b3)) +'\n'
    else:
        return handle_invalid_usage
def fonk2(n):
    b4 = []
    a, b5 = 0, 1
    for i in range(n):
       b4.append(a)
       a, b5 = b5, a+b5
    return b4
@b1.errorhandler(404)
def fonk3(error):
    b6 = jsonify("Please enter a positive number only")
    b6.a1 = 400
    return b6
if b7 = = '__main__':
    b1.run(b8 = '0.0.0.0', debug=True)