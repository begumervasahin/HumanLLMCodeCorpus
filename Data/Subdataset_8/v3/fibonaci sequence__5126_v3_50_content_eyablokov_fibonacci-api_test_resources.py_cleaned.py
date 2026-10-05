
from flask import Flask, jsonify
from sequence_generators.fibonacci import generate_sequence
app = Flask(__name__)
@app.route('/fibonacci/<int:size>', methods=['GET'])
def fibonacci_sequence(size):
    if size < 0:
        return jsonify({'error': 'Size must be a positive integer.', 'actual_size': size}), 400
    elif size > 1000:
        return jsonify({'error': 'Size must be <= 1000.', 'actual_size': size}), 400
    else:
        fibonacci_list = generate_sequence(size)
        return jsonify({'fibonacci_sequence': fibonacci_list}), 200
@app.errorhandler(404)
def not_found_error(error):
    return jsonify({'error': 'Invalid path.'}), 404
@app.errorhandler(Exception)
def unhandled_exception_error(error):
    return jsonify({'error': 'An unhandled exception occurred.'}), 500
if __name__ == '__main__':
    app.run(debug=True)