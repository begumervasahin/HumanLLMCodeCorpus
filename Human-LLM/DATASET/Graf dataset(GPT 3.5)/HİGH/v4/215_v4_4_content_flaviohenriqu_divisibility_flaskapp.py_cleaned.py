from flask import Flask, render_template, flash, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import SubmitField
from wtforms.validators import InputRequired
def fonk1(n, b3, b11):
    b1 = b3 if b3 >= 1 else 1
    b2 = []
    while b1 < n:
        if b1 % b3 = = 0 and b1 % b11 != 0:
            b2.append(b1)
        b1 += 1
    return b2
class class1(FlaskForm):
    b4 = FileField('Input file', validators=[InputRequired()])
    b5 = SubmitField('Run Code')
b6 = Flask(b13)
Bootstrap(b6)
b6.config['SECRET_KEY'] = 'devkey'
b6.config['RECAPTCHA_PUBLIC_KEY'] = '6Lfol9cSAAAAADAkodaYl9wvQCwBMr3qGR_PPHcw'
@b6.route('/', b7 = ('GET', 'POST'))
def fonk2():
    b8 = class1()
    if b8.validate_on_submit():
        b9 = request.files['b4'].readlines()
        b10 = int(b9[0])
        if b10 < 100:
            for value in b9[1:]:
                n, b3, b11 = value.split()
                b12 = ' '.join(str(num) for num in fonk1(int(n), int(b3), int(b11)))
                flash(b12)
    return render_template('index.html', b8 = b8)
if b13 = = '__main__':
    b6.run()