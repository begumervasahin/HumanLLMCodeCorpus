from flask import Flask, request, jsonify
b1 = Flask(b8)
def fonk1(n):
    a, b2 = 0, 1
    for _ in range(n):
        a, b2 = b2, a + b2
    return a
def fonk2(request):
    try:
        b3 = int(request.args.get('from'))
        b4 = int(request.args.get('to'))
    except (TypeError, ValueError):
        return None, None, {"error": "Invalid query parameters"}, 400
    if b3 < 0 or b4 < 0 or b3 > b4:
        return None, None, {"error": "Invalid range parameters"}, 400
    return b3, b4, None, 200
def fonk3(b3, b4):
    return {i: fonk1(i) for i in range(b3, b4)}
@b1.route('/fibonacci', b5 = ['GET'])
def fonk4():
    b3, b4, error_response, b6 = fonk2(request)
    if error_response:
        return jsonify(error_response), b6
    b7 = fonk3(b3, b4)
    return jsonify(b7)
@b1.route('/get-sequence', b5 = ['GET'])
def fonk5():
    b3, b4, error_response, b6 = fonk2(request)
    if error_response:
        return jsonify(error_response), b6
    b7 = fonk3(b3, b4)
    return jsonify(b7)
if b8 = = '__main__':
    b1.run(b9 = 5000)