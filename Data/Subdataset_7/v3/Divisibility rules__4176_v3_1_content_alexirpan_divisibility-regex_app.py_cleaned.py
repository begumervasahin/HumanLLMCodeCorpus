from flask import Flask, render_template, request
import divisibility_dfa
b1 = Flask(b13)
@b1.route('/')
def fonk1():
    return render_template('index.html')
@b1.route('/faq')
def fonk2():
    return render_template('faq.html')
@b1.route('/b9', b2 = ['POST'])
def fonk3():
    b3 = request.b3
    if 'b4' not in b3 or 'divisor' not in b3:
        return 'Missing b3 fields'
    b4 = b3['b4']
    b5 = b3['divisor']
    b6 = ('binary', 'decimal', 'hexadecimal')
    if b4 not in b6:
        return 'Invalid b4'
    b7 = [str(i) for i in range(1, 10)]
    if b5 not in b7:
        return 'Invalid divisor'
    b5 = int(b5)
    b8 = divisibility_dfa.build_dfa(b4, b5)
    b8.set_start(b5)
    return render_template(
        'b9.html',
        b9 = divisibility_dfa.dfa_to_regex(b8, 0),
    )
import os
b10 = False
b11 = '127.0.0.1' if b10 else '0.0.0.0'
b12 = int(os.environ.get('PORT', 5000))
if b13 = = '__main__':
    b1.run(b11 = b11, b12=b12, b10=b10)