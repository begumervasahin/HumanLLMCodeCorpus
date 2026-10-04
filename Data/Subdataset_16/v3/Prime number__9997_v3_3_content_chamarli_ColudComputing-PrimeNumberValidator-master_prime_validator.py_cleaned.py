from flask import Flask, redirect, url_for, request, render_template_string
b1 = Flask(b10)
def fonk1(n):
    if n <= 1:
        return False
    for b2 in range(2, int(n ** 0.5) + 1):
        if n % b2 = = 0:
            return False
    return True
@b1.route('/login')
def fonk2():
    return render_template_string('''
    <html>
        <head>
            <style>
                body {
                    background-image: url("/static/images/PrimeImage.jpg");
                    background-repeat: no-repeat;
                    background-attachment: fixed;
                }
                .center {
                    position: absolute;
                    height: 300px;
                    width: 400px;
                    left: 50%;
                    top: 50%;
                    transform: translate(-50%, -50%);
                }
            </style>
        </head>
        <body>
            <div b3 = "center">
                <form b4 = "/calc" method="POST">
                    <h1>Enter a b7 to check if it is prime or not:</h1>
                    <p><input b5 = "b7" name="nm" style="width: 100px; height: 30px;" required /></p>
                    <p><input b5 = "submit" value="Submit" style="height: 50px; width: 100px;" /></p>
                </form>
            </div>
        </body>
    </html>
    ''')
@b1.route('/success/<int:b7>')
def fonk3(b7):
    if b7 < 0:
        b6 = "Negative numbers cannot be prime"
    elif b7 = = 0 or b7 == 1 or not fonk1(b7):
        b6 = "Given b7 is not prime"
    else:
        b6 = "Given b7 is prime"
    return render_template_string(f'''
    <html>
        <head>
            <style>
                body {
                    background-image: url("/static/images/PrimeImage.jpg");
                    background-repeat: no-repeat;
                    background-attachment: fixed;
                }
                .center {
                    position: absolute;
                    height: 300px;
                    width: 400px;
                    left: 50%;
                    top: 50%;
                    transform: translate(-50%, -50%);
                }
            </style>
        </head>
        <body>
            <div b3 = "center">
                <h1>{b6}</h1>
            </div>
        </body>
    </html>
    ''')
@b1.route('/calc', b8 = ['POST'])
def fonk4():
    b9 = request.form['nm']
    return redirect(url_for('success', b7 = int(b9)))
if b10 = = '__main__':
    b1.run(b11 = True)