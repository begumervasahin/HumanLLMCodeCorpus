from flask import Flask, redirect, url_for, request, render_template_string
b1 = Flask(b11)
@b1.route('/login')
def fonk1():
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
            <div b2 = "center">
                <form b3 = "/calc" b9="POST">
                    <h1>Enter a b7 to check if it is prime or not:</h1>
                    <p><input b4 = "b7" name="nm" style="width: 100px; height: 30px;" /></p>
                    <p><input b4 = "submit" value="Submit" style="height: 50px; width: 100px;" /></p>
                </form>
            </div>
        </body>
    </html>
    ''')
@b1.route('/success/<int:b7>')
def fonk2(b7):
    def fonk3(n):
        if n <= 1:
            return False
        for b5 in range(2, int(n ** 0.5) + 1):
            if n % b5 = = 0:
                return False
        return True
    if b7 < 0:
        b6 = "Negative numbers cannot be prime"
    elif b7 = = 0 or b7 == 1 or not fonk3(b7):
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
            <div b2 = "center">
                <h1>{b6}</h1>
            </div>
        </body>
    </html>
    ''')
@b1.route('/calc', b8 = ['POST', 'GET'])
def fonk4():
    if request.b9 = = 'POST':
        b10 = request.form['nm']
    else:
        b10 = request.args.get('nm')
    return redirect(url_for('success', b7 = int(b10)))
if b11 = = '__main__':
    b1.run(b12 = True)