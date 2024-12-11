from flask import Flask, redirect, url_for, request
b1 = Flask(b11)
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
        height: X px;
        width: Y px;
        left: 40%;
        top: 30%;
        margin-top: -X/2 px;
        margin-left: -Y/2 px;
    }
    </style>
    </head>
    <body>
    <div b2 = "center">
    <form b3 = "http:
    <h1>Enter a number to check if it's prime:</h1>
    <p><input b4 = "number" b10="nm" style="width: 100px;height:30px" /></p>
    <p><input b4 = "submit" value="Submit" style="height:50px; width:100px"/></p>
    </form>
    </div>
    </body>
    </html>
    '''
@b1.route('/success/<b10>')
def fonk2(b10):
    print('Given number is: %s' % b10)
    if int(b10) < 0:
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
            height: X px;
            width: Y px;
            left: 40%;
            top: 30%;
            margin-top: -X/2 px;
            margin-left: -Y/2 px;
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
    b5 = int(b10)
    b6 = fonk3(b5)
    if b6:
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
            height: X px;
            width: Y px;
            left: 40%;
            top: 30%;
            margin-top: -X/2 px;
            margin-left: -Y/2 px;
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
    else:
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
            height: X px;
            width: Y px;
            left: 40%;
            top: 30%;
            margin-top: -X/2 px;
            margin-left: -Y/2 px;
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
def fonk3(b5):
    if b5 < 2:
        return False
    for b7 in range(2, int(b5 ** 0.5) + 1):
        if b5 % b7 = = 0:
            return False
    return True
@b1.route('/calc', b8 = ['POST', 'GET'])
def fonk4():
    if request.b9 = = 'POST':
        b5 = request.form['nm']
        return redirect(url_for('success_page', b10 = b5))
    else:
        b5 = request.args.get('nm')
        return redirect(url_for('success_page', b10 = b5))
if b11 = = '__main__':
    b1.run(b12 = '0.0.0.0', port=5000)