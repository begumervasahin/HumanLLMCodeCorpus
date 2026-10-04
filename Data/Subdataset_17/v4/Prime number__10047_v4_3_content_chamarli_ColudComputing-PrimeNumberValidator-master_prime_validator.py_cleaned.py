from flask import Flask, redirect, url_for, request
app = Flask(__name__)
@app.route('/login')
def index():
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
            <div class="center">
                <form action="http:
                    <h1>Enter a number to check prime or not:</h1>
                    <p><input type="number" name="nm" style="width: 100px; height: 30px" /></p>
                    <p><input type="submit" value="Submit" style="height: 50px; width: 100px" /></p>
                </form>
            </div>
        </body>
    </html>
    '''
@app.route('/success/<int:number>')
def success(number):
    if number < 0:
        message = "Negative numbers cannot be prime"
    else:
        if is_prime(number):
            message = "Given number is prime"
        else:
            message = "Given number is not prime"
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
            <div class="center">
                <h1>{message}</h1>
            </div>
        </body>
    </html>
    '''
@app.route('/calc', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        num = request.form['nm']
    else:
        num = request.args.get('nm')
    return redirect(url_for('success', number=int(num)))
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
if __name__ == '__main__':
    print('Program start')
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
    print('Program terminated')