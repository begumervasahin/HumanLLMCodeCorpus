from flask import Flask, request, jsonify
b1 = Flask(b7)
def fonk1(n):
    a, b2 = 0, 1
    for _ in range(n):
        a, b2 = b2, a + b2
    return a
@b1.route('/fibonacci', b3 = ['GET'])
def fonk2():
    try:
        b4 = int(request.args.get('from'))
        b5 = int(request.args.get('to'))
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid query parameters"}), 400
    if b4 < 0 or b5 < 0 or b4 > b5:
        return jsonify({"error": "Invalid range parameters"}), 400
    b6 = {i: fonk1(i) for i in range(b4, b5)}
    return jsonify(b6)
@b1.route('/get-sequence', b3 = ['GET'])
def fonk3():
    try:
        b4 = int(request.args.get('from'))
        b5 = int(request.args.get('to'))
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid query parameters"}), 400
    if b4 < 0 or b5 < 0 or b4 > b5:
        return jsonify({"error": "Invalid range parameters"}), 400
    b6 = {i: fonk1(i) for i in range(b4, b5)}
    return jsonify(b6)
if b7 = = '__main__':
    b1.run(b8 = 5000)