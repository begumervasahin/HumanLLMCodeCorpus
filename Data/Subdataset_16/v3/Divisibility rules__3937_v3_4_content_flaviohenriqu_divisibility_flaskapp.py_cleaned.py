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
def fonk2(n, b4, b8):
    b3 = []
    for i in range(max(b4, 1), n):
        if i % b4 = = 0 and i % b8 != 0:
            b3.append(i)
    return b3
def fonk3(b1):
    b5 = b1.readlines()
    try:
        b6 = int(b5[0].strip())
    except ValueError:
        return ["The first line of the b1 should be an integer."]
    if b6 >= 100:
        return ["The number of elements exceeds the limit."]
    b7 = []
    for line in b5[1:]:
        try:
            n, b4, b8 = map(int, line.strip().split())
            b3 = fonk2(n, b4, b8)
            b7.append(' '.join(map(str, b3)))
        except ValueError:
            return ["Each line after the first should contain three integers."]
    return b7
b9 = Flask(b13)
Bootstrap(b9)
b9.config['SECRET_KEY'] = 'devkey'
b9.config['RECAPTCHA_PUBLIC_KEY'] = '6Lfol9cSAAAAADAkodaYl9wvQCwBMr3qGR_PPHcw'
@b9.route('/', b10 = ['GET', 'POST'])
def fonk4():
    b11 = class1()
    if b11.validate_on_submit():
        b1 = b11.b1.data
        b12 = secure_filename(b1.b12)
        b7 = fonk3(b1)
        if b7:
            flash('<br>'.join(b7))
    return render_template('index.html', b11 = b11)
if b13 = = '__main__':
    b9.run(b14 = True)