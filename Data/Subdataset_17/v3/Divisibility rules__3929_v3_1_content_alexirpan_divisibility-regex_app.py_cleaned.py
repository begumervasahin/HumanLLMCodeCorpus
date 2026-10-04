from flask import Flask, render_template, request
import divisibility_dfa
app = Flask(__name__)
@app.route('/')
def homepage():
    return render_template('index.html')
@app.route('/faq')
def faq():
    return render_template('faq.html')
@app.route('/regex', methods=['POST'])
def generate_regex():
    form = request.form
    if 'base' not in form or 'divisor' not in form:
        return 'Missing form fields', 400
    base = form['base']
    divisor = form['divisor']
    valid_bases = {'binary', 'decimal', 'hexadecimal'}
    if base not in valid_bases:
        return 'Invalid base', 400
    valid_divisors = {str(i) for i in range(1, 10)}
    if divisor not in valid_divisors:
        return 'Invalid divisor', 400
    divisor = int(divisor)
    dfa = divisibility_dfa.build_dfa(base, divisor)
    dfa.set_start(divisor)
    regex = divisibility_dfa.dfa_to_regex(dfa, 0)
    return render_template('regex.html', regex=regex)
if __name__ == '__main__':
    debug = False
    host = '127.0.0.1' if debug else '0.0.0.0'
    port = int(os.environ.get('PORT', 5000))
    app.run(host=host, port=port, debug=debug)