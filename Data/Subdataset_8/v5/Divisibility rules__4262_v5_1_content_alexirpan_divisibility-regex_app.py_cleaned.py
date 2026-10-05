from flask import Flask, render_template, request
import divisibility_dfa
app = Flask(__name__)
@app.route('/')
def render_homepage():
    return render_template('index.html')
@app.route('/faq')
def render_faq():
    return render_template('faq.html')
@app.route('/regex', methods=['POST'])
def generate_regex():
    form_data = request.form
    if 'base' not in form_data or 'divisor' not in form_data:
        return 'Missing form fields'
    base = form_data['base']
    divisor = form_data['divisor']
    valid_bases = ('binary', 'decimal', 'hexadecimal')
    if base not in valid_bases:
        return 'Invalid base'
    valid_divisors = [str(i) for i in range(1, 10)]
    if divisor not in valid_divisors:
        return 'Invalid divisor'
    divisor = int(divisor)
    dfa = divisibility_dfa.build_dfa(base, divisor)
    dfa.set_start(divisor)
    return render_template('regex.html', regex=divisibility_dfa.dfa_to_regex(dfa, 0))
debug = False
host = '127.0.0.1' if debug else '0.0.0.0'
port = int(os.environ.get('PORT', 5000))
if __name__ == '__main__':
    app.run(host=host, port=port, debug=debug)