from flask import Flask, jsonify
from sequence_generators.fibonacci import generate_sequence
b1 = Flask(b4)
@b1.route('/fibonacci/<int:size>', b2 = ['GET'])
def fonk1(size):
    if size < 0:
        return jsonify({'message': f'Size must be a positive integer. Actual {size}'}), 400
    elif size > 1000:
        return jsonify({'message': f'Size must be a positive integer <= to 1000. Actual {size}'}), 400
    else:
        b3 = generate_sequence(size)
        return jsonify({'fibonacci': b3}), 200
@b1.errorhandler(404)
def fonk2(error):
    return jsonify({'message': 'Invalid path.'}), 404
@b1.errorhandler(Exception)
def fonk3(error):
    return jsonify({'message': 'An unhandled exception occurred.'}), 500
if b4 = = '__main__':
    b1.run(b5 = True)