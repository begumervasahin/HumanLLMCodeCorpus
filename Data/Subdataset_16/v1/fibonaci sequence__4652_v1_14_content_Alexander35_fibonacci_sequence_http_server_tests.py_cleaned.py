from flask import Flask, request, jsonify
b1 = Flask(b6)
def fonk1(n):
    a, b2 = 0, 1
    for _ in range(n):
        a, b2 = b2, a + b2
    return a
@b1.route('/fibonacci')
def fonk2():
    b3 = int(request.args.get('from'))
    b4 = int(request.args.get('to'))
    b5 = {i: fonk1(i) for i in range(b3, b4)}
    return jsonify(b5)
@b1.route('/get-sequence')
def fonk3():
    b3 = int(request.args.get('from'))
    b4 = int(request.args.get('to'))
    b5 = {i: fonk1(i) for i in range(b3, b4)}
    return jsonify(b5)
if b6 = = '__main__':
    b1.run(b7 = 5000)