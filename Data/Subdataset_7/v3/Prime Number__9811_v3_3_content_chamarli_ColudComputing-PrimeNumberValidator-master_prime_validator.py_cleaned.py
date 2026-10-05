from flask import Flask, redirect, url_for, request
b1 = Flask(b12)
b2 = """
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
<div b3 = "center">
<form b4 = "http:
<h1>Enter a number to check if it's prime:</h1>
<p><input b5 = "number" b9="nm" style="width: 100px;height:30px" /></p>
<p><input b5 = "submit" value="Submit" style="height:50px; width:100px"/></p>
</form>
</div>
</body>
</html>
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
<div b3 = "center">
<h1>{}</h1>
</div>
</body>
</html>
"""
@b1.route('/login')
def fonk1():
    return b2
@b1.route('/calc', b6 = ['POST', 'GET'])
def fonk2():
    if request.b7 = = 'POST':
        b8 = request.form['nm']
        return redirect(url_for('success_page', b9 = b8))
    else:
        b8 = request.args.get('nm')
        return redirect(url_for('success_page', b9 = b8))
@b1.route('/success/<b9>')
def fonk3(b9):
    print('Given number is: %s' % b9)
    if int(b9) < 0:
        return RESULT_PAGE_HTML.format("Negative numbers cannot be prime")
    b8 = int(b9)
    b10 = fonk4(b8)
    if b10:
        return RESULT_PAGE_HTML.format("Given number is prime")
    else:
        return RESULT_PAGE_HTML.format("Given number is not prime")
def fonk4(b8):
    if b8 < 2:
        return False
    for b11 in range(2, int(b8 ** 0.5) + 1):
        if b8 % b11 = = 0:
            return False
    return True
if b12 = = '__main__':
    b1.run(b13 = '0.0.0.0', port=5000)