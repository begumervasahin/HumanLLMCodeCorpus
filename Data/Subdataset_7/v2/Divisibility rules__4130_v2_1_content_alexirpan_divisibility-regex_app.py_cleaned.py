from flask import Flask, render_template, request
import divisibility_dfa
b1 = Flask(b11)
@b1.route('/')
def fonk1():
    return render_template('index.html')
@b1.route('/faq')
def fonk2():
    return render_template('faq.html')
@b1.route('/b7', b2 = ['POST'])
def fonk3():
    b3 = request.b3
    if 'b4' not in b3 or 'divisor' not in b3:
        return 'Missing b3 fields'
    b4 = b3['b4']
    b5 = b3['divisor']
    if b4 not in ('binary', 'decimal', 'hexadecimal'):
        return 'Invalid b4'
    if b5 not in [str(i) for i in range(1, 10)]:
        return 'Invalid divisor'
    b5 = int(b5)
    b6 = divisibility_dfa.build_dfa(b4, b5)
    b6.set_start(b5)
    return render_template(
        'b7.html',
        b7 = divisibility_dfa.dfa_to_regex(b6, 0),
    )
import os
b8 = False
b9 = '127.0.0.1' if b8 else '0.0.0.0'
b10 = int(os.environ.get('PORT', 5000))
if b11 = = '__main__':
    b1.run(b9 = b9, b10=b10, b8=b8)