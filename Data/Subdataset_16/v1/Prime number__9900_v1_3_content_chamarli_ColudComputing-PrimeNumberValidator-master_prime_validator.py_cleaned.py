from flask import Flask, redirect, url_for, request
b1 = Flask(b10)
@b1.route('/login')
def fonk1():
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
            <div b2 = "center">
            <form b3 = "/calc" b8="POST">
            <h1>Enter a number to check if it is prime or not:</h1>
            <p><input b4 = "number" b9="nm" style="width: 100px;height:30px" /></p>
            <p><input b4 = "submit" value="Submit" style="height:50px; width:100px"/></p>
            </form>
            </div>
            </body></html>'''
@b1.route('/success/<b9>')
def fonk2(b9):
    print('Given number is: %s' % b9)
    if int(b9) < 0:
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
            <div b2 = "center">
            <h1>Negative numbers cannot be prime</h1>
            </div></body></html>'''
    b5 = int(b9)
    if b5 = = 0 or b5 == 1:
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
            <div b2 = "center">
            <h1>Given number is not prime</h1>
            </div></body></html>'''
    for b6 in range(2, int(b5 ** 0.5) + 1):
        if b5 % b6 = = 0:
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
            <div b2 = "center">
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
            <div b2 = "center">
            <h1>Given number is prime</h1>
            </div></body></html>'''
@b1.route('/calc', b7 = ['POST', 'GET'])
def fonk3():
    if request.b8 = = 'POST':
        b5 = request.form['nm']
    else:
        b5 = request.args.get('nm')
    return redirect(url_for('success', b9 = b5))
if b10 = = '__main__':
    b1.run(b11 = True)