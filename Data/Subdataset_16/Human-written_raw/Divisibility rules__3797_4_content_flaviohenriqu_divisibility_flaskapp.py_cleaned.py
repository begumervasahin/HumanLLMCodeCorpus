from flask import Flask, render_template, flash, request
from flask_bootstrap import Bootstrap
from flask_wtf import Form, RecaptchaField
from flask_wtf.file import FileField
from wtforms import TextField, HiddenField, ValidationError, RadioField,\
    BooleanField, SubmitField, IntegerField, FormField, validators
class class1(Form):
    b1 = FileField('Input file')
    b2 = SubmitField('Run Code')
    def fonk1(b8, field):
        raise ValidationError('Always wrong')
def fonk2(n, b5, b11):
    b3 = b5
    if b5 < 1:
        b3 = 1
    b4 = []
    while b3 < n:
        if (b3 % b5 = = 0) and (b3 % b11 != 0):
            b4.append(b3)
        b3 += 1
    return b4
b6 = Flask(b13)
Bootstrap(b6)
b6.config['SECRET_KEY'] = 'devkey'
b6.config['RECAPTCHA_PUBLIC_KEY'] = \
    '6Lfol9cSAAAAADAkodaYl9wvQCwBMr3qGR_PPHcw'
@b6.route('/', b7 = ('GET', 'POST'))
def fonk3():
    b8 = class1()
    if b8.validate_on_submit():
        b9 = request.files['b1'].readlines()
        b10 = int(b9[0])
        if b10 < 100:
            for value in b9[1:]:
                n, b5, b11 = value.split(' ')
                b12 = ' '.join(str(b5) for b5 in fonk2(int(n), int(b5), int(b11)))
                flash(b12)
    return render_template('index.html', b8 = b8)
if b13 = = '__main__':
    b6.run()