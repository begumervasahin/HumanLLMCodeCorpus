from flask import Flask, render_template, flash, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import SubmitField
from wtforms.validators import InputRequired
def find_special_numbers(n, x, y):
    start = x if x >= 1 else 1
    special_numbers = []
    while start < n:
        if start % x == 0 and start % y != 0:
            special_numbers.append(start)
        start += 1
    return special_numbers
class SimpleForm(FlaskForm):
    fileName = FileField('Input file', validators=[InputRequired()])
    submit_button = SubmitField('Run Code')
app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = 'devkey'
app.config['RECAPTCHA_PUBLIC_KEY'] = '6Lfol9cSAAAAADAkodaYl9wvQCwBMr3qGR_PPHcw'
@app.route('/', methods=('GET', 'POST'))
def index():
    form = SimpleForm()
    if form.validate_on_submit():
        values = request.files['fileName'].readlines()
        num_elements = int(values[0])
        if num_elements < 100:
            for value in values[1:]:
                n, x, y = value.split()
                result = ' '.join(str(num) for num in find_special_numbers(int(n), int(x), int(y)))
                flash(result)
    return render_template('index.html', form=form)
if __name__ == '__main__':
    app.run()