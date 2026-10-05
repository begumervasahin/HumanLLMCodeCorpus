from flask import Flask, render_template, flash, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm, RecaptchaField
from flask_wtf.file import FileField
from wtforms import ValidationError, SubmitField
from wtforms.validators import InputRequired
def solution(n, x, y):
    initial = x if x >= 1 else 1
    result = []
    while initial < n:
        if initial % x == 0 and initial % y != 0:
            result.append(initial)
        initial += 1
    return result
class SimpleForm(FlaskForm):
    fileName = FileField('Input file', validators=[InputRequired()])
    submit_button = SubmitField('Run Code')
    def validate_hidden_field(form, field):
        raise ValidationError('Always wrong')
app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = 'devkey'
@app.route('/', methods=('GET', 'POST'))
def index():
    form = SimpleForm()
    if form.validate_on_submit():
        values = request.files['fileName'].readlines()
        elems = int(values[0])
        if elems < 100:
            for value in values[1:]:
                n, x, y = map(int, value.split())
                str_result = ' '.join(str(x) for x in solution(n, x, y))
                flash(str_result)
    return render_template('index.html', form=form)
if __name__ == '__main__':
    app.run()