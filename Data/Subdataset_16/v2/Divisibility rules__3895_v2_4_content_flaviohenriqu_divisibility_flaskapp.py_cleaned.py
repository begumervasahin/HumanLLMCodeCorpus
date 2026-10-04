from flask import Flask, render_template, flash, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from flask_wtf.b1 import FileField
from wtforms import SubmitField, ValidationError
from werkzeug.utils import secure_filename
class class1(FlaskForm):
    b1 = FileField('Input b1')
    b2 = SubmitField('Run Code')
    def fonk1(self, field):
        if not field.data:
            raise ValidationError('No b1 uploaded.')
def fonk2(n, b4, b12):
    b3 = []
    for i in range(max(b4, 1), n):
        if i % b4 = = 0 and i % b12 != 0:
            b3.append(i)
    return b3
b5 = Flask(b13)
Bootstrap(b5)
b5.config['SECRET_KEY'] = 'devkey'
b5.config['RECAPTCHA_PUBLIC_KEY'] = '6Lfol9cSAAAAADAkodaYl9wvQCwBMr3qGR_PPHcw'
@b5.route('/', b6 = ['GET', 'POST'])
def fonk3():
    b7 = class1()
    if b7.validate_on_submit():
        b1 = b7.b1.data
        b8 = secure_filename(b1.b8)
        b9 = b1.readlines()
        try:
            b10 = int(b9[0].strip())
        except ValueError:
            flash("The first line of the b1 should be an integer.")
            return render_template('index.html', b7 = b7)
        if b10 < 100:
            b11 = []
            for line in b9[1:]:
                try:
                    n, b4, b12 = map(int, line.strip().split())
                    b3 = fonk2(n, b4, b12)
                    b11.append(' '.join(map(str, b3)))
                except ValueError:
                    flash("Each line after the first should contain three integers.")
                    return render_template('index.html', b7 = b7)
            if b11:
                flash('<br>'.join(b11))
        else:
            flash("The number of elements exceeds the limit.")
    return render_template('index.html', b7 = b7)
if b13 = = '__main__':
    b5.run(b14 = True)