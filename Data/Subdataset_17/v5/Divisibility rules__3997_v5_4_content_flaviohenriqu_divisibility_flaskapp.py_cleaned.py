from flask import Flask, render_template, flash, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import SubmitField, ValidationError
from werkzeug.utils import secure_filename
class SimpleForm(FlaskForm):
    file = FileField('Input file')
    submit_button = SubmitField('Run Code')
    def validate_file(self, field):
        if not field.data:
            raise ValidationError('No file uploaded.')
def calculate_valid_multiples(n, x, y):
    result = []
    for i in range(max(x, 1), n):
        if i % x == 0 and i % y != 0:
            result.append(i)
    return result
def process_file(file):
    try:
        file_lines = file.readlines()
        elems = int(file_lines[0].strip())
        if elems >= 100:
            return ["The number of elements exceeds the limit."]
        results = []
        for line in file_lines[1:]:
            try:
                n, x, y = map(int, line.strip().split())
                result = calculate_valid_multiples(n, x, y)
                results.append(' '.join(map(str, result)))
            except ValueError:
                return ["Each line after the first should contain three integers."]
        return results
    except Exception as e:
        return [f"An error occurred: {str(e)}"]
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
        results = process_file(file)
        if results:
            flash('<br>'.join(results))
    return render_template('index.html', form=form)
if __name__ == '__main__':
    app.run(debug=True)