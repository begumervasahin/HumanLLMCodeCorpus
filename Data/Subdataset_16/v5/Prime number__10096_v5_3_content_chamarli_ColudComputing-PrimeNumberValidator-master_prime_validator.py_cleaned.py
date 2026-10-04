from flask import Flask, redirect, url_for, request
b1 = Flask(b10)
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
                    height: 200px;
                    width: 400px;
                    left: 50%;
                    top: 50%;
                    transform: translate(-50%, -50%);
                }
            </style>
        </head>
        <body>
            <div b2 = "center">
                <form b3 = "/calc" method="POST">
                    <h1>Enter a b8 to check if it is prime:</h1>
                    <p><input b4 = "b8" name="nm" style="width: 100px; height: 30px" /></p>
                    <p><input b4 = "submit" value="Submit" style="height: 50px; width: 100px" /></p>
                </form>
            </div>
        </body>
    </html>
    '''
@b1.route('/success/<int:b8>')
def fonk2(b8):
    if b8 < 0:
        b5 = "Negative numbers cannot be prime"
    else:
        b5 = "Given b8 is prime" if fonk4(b8) else "Given b8 is not prime"
    return f'''
    <html>
        <head>
            <style>
                body {{
                    background-image: url("../static/images/PrimeImage.jpg");
                    background-repeat: no-repeat;
                    background-attachment: fixed;
                }}
                .center {{
                    position: absolute;
                    height: 200px;
                    width: 400px;
                    left: 50%;
                    top: 50%;
                    transform: translate(-50%, -50%);
                }}
            </style>
        </head>
        <body>
            <div b2 = "center">
                <h1>{b5}</h1>
            </div>
        </body>
    </html>
    '''
@b1.route('/calc', b6 = ['POST'])
def fonk3():
    b7 = request.form['nm']
    return redirect(url_for('success', b8 = int(b7)))
def fonk4(b8):
    if b8 < 2:
        return False
    for b9 in range(2, int(b8 ** 0.5) + 1):
        if b8 % b9 = = 0:
            return False
    return True
if b10 = = '__main__':
    print('Program start')
    b1.run(b11 = True, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
    print('Program terminated')