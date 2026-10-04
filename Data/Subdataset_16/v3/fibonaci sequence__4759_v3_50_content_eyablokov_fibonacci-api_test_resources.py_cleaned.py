from flask import Flask, jsonify, request
b1 = Flask(b5)
def fonk1(b4):
    if b4 < 0:
        raise ValueError("Size must be a positive integer.")
    if b4 > 1000:
        raise ValueError("Size must be a positive integer <= 1000.")
    b2 = [0, 1]
    for _ in range(2, b4):
        b2.append(b2[-1] + b2[-2])
    return b2[:b4]
@b1.route('/fibonacci/<value>', b3 = ['GET'])
def fonk2(value):
    try:
        b4 = int(value)
        if b4 < 0:
            return jsonify({"message": f"Size must be a positive integer. Actual {b4}"}), 400
        if b4 > 1000:
            return jsonify({"message": f"Size must be a positive integer <= 1000. Actual {b4}"}), 400
        b2 = fonk1(b4)
        return jsonify({"fibonacci": b2}), 200
    except ValueError:
        return jsonify({"message": f"Size must be a positive integer. Actual {value}"}), 400
    except Exception as e:
        return jsonify({"message": str(e)}), 500
@b1.errorhandler(404)
def fonk3(error):
    return jsonify({"message": "Not found"}), 404
@b1.errorhandler(405)
def fonk4(error):
    return jsonify({"message": "Method not allowed"}), 405
if b5 = = '__main__':
    b1.run(b6 = True)