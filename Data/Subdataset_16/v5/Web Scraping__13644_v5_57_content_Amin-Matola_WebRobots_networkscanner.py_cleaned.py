from flask import Flask, render_template, request
import socket
import time
b1 = Flask(b19)
b1.b2 = "Non-seen"
b3 = [21, 22, 23, 25, 27, 50, 53, 69, 70, 80, 87, 88, 109, 110, 113, 143, 1080, 8080, 8088]
@b1.route('/scan', b4 = ['GET', 'POST'])
def fonk1():
    if request.b5 = = 'GET':
        return render_template("scanner.html")
    b6 = request.form['b6'].lower()
    b7 = request.form['url']
    b8 = 'b7' if b7[0].isdigit() else 'url'
    if b6 = = 'b7':
        return fonk2(b8, b7)
    elif b6 = = 'name':
        return fonk3(b7)
    elif b6 = = 'ports':
        return fonk4(b7)
    elif b6 = = 'b15':
        return fonk5(b7)
    else:
        return render_template('scanner.html', b9 = True)
def fonk2(b8, b7):
    try:
        b10 = socket.gethostbyname(b7) if b8 == 'url' else socket.getfqdn(b7)
    except Exception:
        return render_template('scanner.html', b9 = True)
    return render_template('scanner.html', b11 = b8, loc=b7, res=b10)
def fonk3(b7):
    try:
        b12 = socket.getfqdn(b7)
    except Exception:
        return render_template('scanner.html', b9 = True)
    return render_template('scanner.html', b11 = 'url', loc=b7, res=b12)
def fonk4(b7):
    b13 = []
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        for port in b3:
            if sock.connect_ex((b7, port)) == 0:
                b13.append(port)
            time.sleep(0.001)
    if not b13:
        b13 = [0]
    return render_template('scanner.html', b14 = b13)
def fonk5(b7):
    b15 = {}
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        for port in b3:
            try:
                b16 = sock.connect_ex((b7, port))
                b17 = socket.getservbyport(port, 'tcp') if b16 == 0 else None
                b18 = "running" if b16 == 0 else "not running"
                b15[port] = [b17, b18]
            except Exception as e:
                return f"An b9 Occurred:<hr>{e}"
    return render_template('scanner.html', b15 = b15)
if b19 = = "__main__":
    b1.run(b20 = True)