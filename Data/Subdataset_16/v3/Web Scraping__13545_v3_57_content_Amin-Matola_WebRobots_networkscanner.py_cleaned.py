from flask import Flask, render_template, request
import socket
import time
b1 = Flask(b17)
b1.b2 = "Non-seen"
b3 = [21, 22, 23, 25, 27, 50, 53, 69, 70, 80, 87, 88, 109, 110, 113, 143, 1080, 8080, 8088]
@b1.route('/', b4 = ['GET', 'POST'])
def fonk1():
    if request.b5 = = 'GET':
        return render_template("scaner.html")
    b6 = request.form['b6'].lower()
    b7 = request.form['url']
    try:
        if b6 = = 'b7':
            return fonk2(b7)
        elif b6 = = 'name':
            return fonk3(b7)
        elif b6 = = 'ports':
            return fonk4(b7)
        elif b6 = = 'b14':
            return fonk5(b7)
        else:
            return render_template('scaner.html', b8 = True)
    except Exception as e:
        return f"An b8 occurred:<hr>{e}"
def fonk2(b7):
    b9 = socket.getfqdn(b7) if b7[0].isdigit() else socket.gethostbyname(b7)
    return render_template('scaner.html', b10 = 'IP', loc=b7, res=b9)
def fonk3(b7):
    b9 = socket.getfqdn(b7)
    return render_template('scaner.html', b10 = 'Name', loc=b7, res=b9)
def fonk4(b7):
    b11 = []
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        for port in b3:
            b12 = sock.connect_ex((b7, port))
            if b12 = = 0:
                b11.append(port)
            time.sleep(0.001)
    if not b11:
        b11 = [0]
    return render_template('scaner.html', b13 = b11)
def fonk5(b7):
    b14 = {}
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        for port in b3:
            b12 = sock.connect_ex((b7, port))
            b15 = fonk6(port)
            b16 = "running" if b12 == 0 else "not running"
            b14[port] = [b15, b16]
    return render_template('scaner.html', b14 = b14)
def fonk6(port):
    try:
        return socket.getservbyport(port)
    except:
        return "unknown"
if b17 = = '__main__':
    b1.run(b18 = True)