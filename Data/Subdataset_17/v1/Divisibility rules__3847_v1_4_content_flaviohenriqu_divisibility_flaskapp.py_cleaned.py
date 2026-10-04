from flask import Flask, render_template, flash, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm, RecaptchaField
from flask_wtf.file import FileField
from wtforms import SubmitField, ValidationError
from werkzeug.utils import secure_filename
class SimpleForm(FlaskForm):
    file = FileField('Input file')
    submit_button = SubmitField('Run Code')
    def validate_file(form, field):
        if not field.data:
            raise ValidationError('No file uploaded.')
def solution(n, x, y):
    initial = max(x, 1)
    result = []
    while initial < n:
        if (initial % x == 0) and (initial % y != 0):
            result.append(initial)
        initial += 1
    return result
app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = 'devkey'
app.config['RECAPTCHA_PUBLIC_KEY'] = '6Lfol9cSAAAAADAkodaYl9wvQCwBMr3qGR_PPHcw'
@app.route('/', methods=['GET', 'POST'])
def index():
    form = SimpleForm()
    if form.validate_on_submit():
        file = form.file.data
        filename = secure_filename(file.filename)
        file_lines = file.readlines()
        elems = int(file_lines[0].strip())
        if elems < 100:
            for line in file_lines[1:]:
                n, x, y = map(int, line.strip().split())
                result = solution(n, x, y)
                str_result = ' '.join(map(str, result))
                flash(str_result)
        else:
            flash("The number of elements exceeds the limit.")
    return render_template('index.html', form=form)
if __name__ == '__main__':
    app.run()