from flask import Flask, jsonify, Response
b1 = Flask(b8)
@b1.route('/fibonacci/<int:b3>', b2 = ['GET'])
def fonk1(b3: int) -> Response:
    if b3 = = 0:
        return jsonify([])
    elif b3 > 0:
        return jsonify(fonk2(b3))
    else:
        return fonk3()
def fonk2(n: int) -> list:
    b4 = []
    a, b5 = 0, 1
    for _ in range(n):
        b4.append(a)
        a, b5 = b5, a + b5
    return b4
@b1.errorhandler(400)
def fonk3(b6 = None) -> Response:
    b7 = jsonify(message="Please enter a positive number only")
    b7.a1 = 400
    return b7
if b8 = = '__main__':
    b1.run(b9 = '0.0.0.0', debug=True)