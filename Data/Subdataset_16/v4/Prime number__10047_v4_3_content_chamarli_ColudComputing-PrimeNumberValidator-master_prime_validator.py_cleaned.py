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
                    height: 200px;  /* Adjust as needed */
                    width: 400px;  /* Adjust as needed */
                    left: 40%;
                    top: 30%;
                    margin-top: -100px;  /* Half of height */
                    margin-left: -200px;  /* Half of width */
                }
            </style>
        </head>
        <body>
            <div b2 = "center">
                <form b3 = "http:
                    <h1>Enter a b9 to check prime or not:</h1>
                    <p><input b4 = "b9" name="nm" style="width: 100px; height: 30px" /></p>
                    <p><input b4 = "submit" value="Submit" style="height: 50px; width: 100px" /></p>
                </form>
            </div>
        </body>
    </html>
    '''
@b1.route('/success/<int:b9>')
def fonk2(b9):
    if b9 < 0:
        b5 = "Negative numbers cannot be prime"
    else:
        if fonk4(b9):
            b5 = "Given b9 is prime"
        else:
            b5 = "Given b9 is not prime"
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
                    height: 200px;  /* Adjust as needed */
                    width: 400px;  /* Adjust as needed */
                    left: 40%;
                    top: 30%;
                    margin-top: -100px;  /* Half of height */
                    margin-left: -200px;  /* Half of width */
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
@b1.route('/calc', b6 = ['POST', 'GET'])
def fonk3():
    if request.b7 = = 'POST':
        b8 = request.form['nm']
    else:
        b8 = request.args.get('nm')
    return redirect(url_for('success', b9 = int(b8)))
def fonk4(b9):
    if b9 < 2:
        return False
    for b10 in range(2, int(b9 ** 0.5) + 1):
        if b9 % b10 = = 0:
            return False
    return True
if b11 = = '__main__':
    print('Program start')
    b1.run(b12 = True, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
    print('Program terminated')