from flask import Flask, redirect, url_for, request, render_template_string
app = Flask(__name__)
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
@app.route('/login')
def index():
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
            <div class="center">
                <form action="/calc" method="POST">
                    <h1>Enter a number to check if it is prime or not:</h1>
                    <p><input type="number" name="nm" style="width: 100px; height: 30px;" required /></p>
                    <p><input type="submit" value="Submit" style="height: 50px; width: 100px;" /></p>
                </form>
            </div>
        </body>
    </html>
    ''')
@app.route('/success/<int:number>')
def success(number):
    if number < 0:
        message = "Negative numbers cannot be prime"
    elif number == 0 or number == 1 or not is_prime(number):
        message = "Given number is not prime"
    else:
        message = "Given number is prime"
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
            <div class="center">
                <h1>{message}</h1>
            </div>
        </body>
    </html>
    ''')
@app.route('/calc', methods=['POST'])
def calc():
    num = request.form['nm']
    return redirect(url_for('success', number=int(num)))
if __name__ == '__main__':
    app.run(debug=True)