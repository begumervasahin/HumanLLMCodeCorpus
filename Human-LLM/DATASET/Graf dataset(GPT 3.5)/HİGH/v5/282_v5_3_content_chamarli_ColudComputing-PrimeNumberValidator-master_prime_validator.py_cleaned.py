from flask import Flask, redirect, url_for, request
b1 = Flask(__name__)
@b1.route('/login')
def fonk1():
    return '''
        <html>
        <head>
        <style>
        body {
            background-image: url("static/images/PrimeImage.jpg");
            background-repeat: no-repeat;
            background-attachment: fixed;
        }
        .center {
            position: absolute;
            left: 40%;
            top: 30%;
            transform: translate(-50%, -50%);
            text-align: center;
        }
        </style>
        </head>
        <body>
        <div b2 = "center">
        <form b3 = "http:
        <h1>Enter a number to check if it's prime:</h1>
        <p><input b4 = "number" b10="nm" style="width: 100px; height: 30px;" /></p>
        <p><input b4 = "submit" value="Submit" style="height: 50px; width: 100px;" /></p>
        </form>
        </div>
        </body>
        </html>
    '''
@b1.route('/success/<b10>')
def fonk2(b10):
    print('Given number is: %s' % b10)
    if int(b10) < 0:
        return fonk4()
    b5 = fonk3(int(b10))
    return fonk5(b5)
def fonk3(b9):
    if b9 < 2:
        return False
    for b6 in range(2, int(b9**0.5) + 1):
        if b9 % b6 = = 0:
            return False
    return True
def fonk4():
    return '''
        <html>
        <head>
        <style>
        body {
            background-image: url("../static/images/PrimeImage.jpg");
            background-repeat: no-repeat;
            background-attachment: fixed;
        }
        .center {
            position: absolute;
            left: 40%;
            top: 30%;
            transform: translate(-50%, -50%);
            text-align: center;
        }
        </style>
        </head>
        <body>
        <div b2 = "center">
        <h1>Negative numbers cannot be prime</h1>
        </div>
        </body>
        </html>
    '''
def fonk5(b5):
    if b5:
        return fonk6()
    else:
        return fonk7()
def fonk6():
    return '''
        <html>
        <head>
        <style>
        body {
            background-image: url("../static/images/PrimeImage.jpg");
            background-repeat: no-repeat;
            background-attachment: fixed;
        }
        .center {
            position: absolute;
            left: 40%;
            top: 30%;
            transform: translate(-50%, -50%);
            text-align: center;
        }
        </style>
        </head>
        <body>
        <div b2 = "center">
        <h1>Given number is prime</h1>
        </div>
        </body>
        </html>
    '''
def fonk7():
    return '''
        <html>
        <head>
        <style>
        body {
            background-image: url("../static/images/PrimeImage.jpg");
            background-repeat: no-repeat;
            background-attachment: fixed;
        }
        .center {
            position: absolute;
            left: 40%;
            top: 30%;
            transform: translate(-50%, -50%);
            text-align: center;
        }
        </style>
        </head>
        <body>
        <div b2 = "center">
        <h1>Given number is not prime</h1>
        </div>
        </body>
        </html>
    '''
@b1.route('/calc', b7 = ['POST', 'GET'])
def fonk8():
    if request.b8 = = 'POST':
        b9 = request.form['nm']
        return redirect(url_for('check_prime_success', b10 = b9))
    else:
        b9 = request.args.get('nm')
        return redirect(url_for('check_prime_success', b10 = b9))