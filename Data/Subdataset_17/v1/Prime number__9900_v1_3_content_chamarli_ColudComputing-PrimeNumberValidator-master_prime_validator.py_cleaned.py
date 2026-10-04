from flask import Flask, redirect, url_for, request
app = Flask(__name__)
@app.route('/login')
def index():
    return '''<html>
            <head>
            <style>
            body{background-image: url("static/images/PrimeImage.jpg");background-repeat:no-repeat;background-attachment:fixed;}
            .center{
            position:absolute;
            height: 300px;
            width: 400px;
            left:40%;
            top:30%;
            margin-top:-150px;
            margin-left:-200px;
            }
            </style>
            </head>
            <body>
            <div class="center">
            <form action="/calc" method="POST">
            <h1>Enter a number to check if it is prime or not:</h1>
            <p><input type="number" name="nm" style="width: 100px;height:30px" /></p>
            <p><input type="submit" value="Submit" style="height:50px; width:100px"/></p>
            </form>
            </div>
            </body></html>'''
@app.route('/success/<name>')
def success(name):
    print('Given number is: %s' % name)
    if int(name) < 0:
        return '''<html>
            <head>
            <style>
            body{background-image: url("../static/images/PrimeImage.jpg");background-repeat:no-repeat;background-attachment:fixed;}
            .center{
            position:absolute;
            height: 300px;
            width: 400px;
            left:40%;
            top:30%;
            margin-top:-150px;
            margin-left:-200px;
            }
            </style>
            </head>
            <body>
            <div class="center">
            <h1>Negative numbers cannot be prime</h1>
            </div></body></html>'''
    num = int(name)
    if num == 0 or num == 1:
        return '''<html>
            <head>
            <style>
            body{background-image: url("../static/images/PrimeImage.jpg");background-repeat:no-repeat;background-attachment:fixed;}
            .center{
            position:absolute;
            height: 300px;
            width: 400px;
            left:40%;
            top:30%;
            margin-top:-150px;
            margin-left:-200px;
            }
            </style>
            </head>
            <body>
            <div class="center">
            <h1>Given number is not prime</h1>
            </div></body></html>'''
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return '''<html>
            <head>
            <style>
            body{background-image: url("../static/images/PrimeImage.jpg");background-repeat:no-repeat;background-attachment:fixed;}
            .center{
            position:absolute;
            height: 300px;
            width: 400px;
            left:40%;
            top:30%;
            margin-top:-150px;
            margin-left:-200px;
            }
            </style>
            </head>
            <body>
            <div class="center">
            <h1>Given number is not prime</h1>
            </div></body></html>'''
    return '''<html>
            <head>
            <style>
            body{background-image: url("../static/images/PrimeImage.jpg");background-repeat:no-repeat;background-attachment:fixed;}
            .center{
            position:absolute;
            height: 300px;
            width: 400px;
            left:40%;
            top:30%;
            margin-top:-150px;
            margin-left:-200px;
            }
            </style>
            </head>
            <body>
            <div class="center">
            <h1>Given number is prime</h1>
            </div></body></html>'''
@app.route('/calc', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        num = request.form['nm']
    else:
        num = request.args.get('nm')
    return redirect(url_for('success', name=num))
if __name__ == '__main__':
    app.run(debug=True)