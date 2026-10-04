from flask import Flask, render_template, flash, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm, RecaptchaField
from flask_wtf.b1 import FileField
from wtforms import SubmitField, ValidationError
from werkzeug.utils import secure_filename
class class1(FlaskForm):
    b1 = FileField('Input b1')
    b2 = SubmitField('Run Code')
    def fonk1(b8, field):
        if not field.data:
            raise ValidationError('No b1 uploaded.')
def fonk2(n, b5, b12):
    b3 = max(b5, 1)
    b4 = []
    while b3 < n:
        if (b3 % b5 = = 0) and (b3 % b12 != 0):
            b4.append(b3)
        b3 += 1
    return b4
b6 = Flask(b14)
Bootstrap(b6)
b6.config['SECRET_KEY'] = 'devkey'
b6.config['RECAPTCHA_PUBLIC_KEY'] = '6Lfol9cSAAAAADAkodaYl9wvQCwBMr3qGR_PPHcw'
@b6.route('/', b7 = ['GET', 'POST'])
def fonk3():
    b8 = class1()
    if b8.validate_on_submit():
        b1 = b8.b1.data
        b9 = secure_filename(b1.b9)
        b10 = b1.readlines()
        b11 = int(b10[0].strip())
        if b11 < 100:
            for line in b10[1:]:
                n, b5, b12 = map(int, line.strip().split())
                b4 = fonk2(n, b5, b12)
                b13 = ' '.join(map(str, b4))
                flash(b13)
        else:
            flash("The number of elements exceeds the limit.")
    return render_template('index.html', b8 = b8)
if b14 = = '__main__':
    b6.run()