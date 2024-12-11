from flask import Flask, jsonify
b1 = Flask(b9)
@b1.route('/fibonacci/<int:b3>', b2 = ['GET'])
def fonk1(b3):
    if b3 = = 0:
        return ""
    elif b3 > 0:
        return str(fonk2(b3)) + '\n'
    else:
        return fonk3()
def fonk2(n):
    b4 = []
    a, b5 = 0, 1
    for i in range(n):
       b4.append(a)
       a, b5 = b5, a + b5
    return b4
@b1.errorhandler(400)
def fonk3(b6 = None):
    b7 = "Please enter a positive number only"
    b8 = jsonify(b7)
    b8.a1 = 400
    return b8
if b9 = = '__main__':
    b1.run(b10 = '0.0.0.0', debug=True)