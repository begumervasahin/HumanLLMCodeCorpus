
from flask import Flask, jsonify
from sequence_generators.fibonacci import generate_sequence
b1 = Flask(b4)
@b1.route('/fibonacci/<int:size>', b2 = ['GET'])
def fonk1(size):
    if size < 0:
        return jsonify({'error': 'Size must be a positive integer.', 'actual_size': size}), 400
    elif size > 1000:
        return jsonify({'error': 'Size must be <= 1000.', 'actual_size': size}), 400
    else:
        b3 = generate_sequence(size)
        return jsonify({'fibonacci_sequence': b3}), 200
@b1.errorhandler(404)
def fonk2(error):
    return jsonify({'error': 'Invalid path.'}), 404
@b1.errorhandler(Exception)
def fonk3(error):
    return jsonify({'error': 'An unhandled exception occurred.'}), 500
if b4 = = '__main__':
    b1.run(b5 = True)