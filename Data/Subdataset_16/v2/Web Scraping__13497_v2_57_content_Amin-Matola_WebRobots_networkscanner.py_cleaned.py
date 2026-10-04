from flask import Flask, render_template, request
import socket
import time
b1 = Flask(b17)
b1.b2 = "Non-seen"
@b1.route('/', b3 = ['GET', 'POST'])
def fonk1():
    if request.b4 = = 'GET':
        return render_template("scaner.html")
    b5 = request.form['b5']
    b6 = request.form['url']
    b7 = [21, 22, 23, 25, 27, 50, 53, 69, 70, 80, 87, 88, 109, 110, 113, 143, 1080, 8080, 8088]
    b8 = []
    b9 = {}
    try:
        if b5.lower() == 'b6':
            b10 = socket.getfqdn(b6) if b6[0].isdigit() else socket.gethostbyname(b6)
            return render_template('scaner.html', b11 = 'IP', loc=b6, res=b10)
        elif b5.lower() == 'name':
            b10 = socket.getfqdn(b6)
            return render_template('scaner.html', b11 = 'Name', loc=b6, res=b10)
        elif b5.lower() == 'ports':
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                for port in b7:
                    b12 = sock.connect_ex((b6, port))
                    if b12 = = 0:
                        b8.append(port)
                    time.sleep(0.001)
            if not b8:
                b8 = [0]
            return render_template('scaner.html', b13 = b8)
        elif b5.lower() == 'b9':
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                for port in b7:
                    b12 = sock.connect_ex((b6, port))
                    try:
                        b14 = socket.getservbyport(port)
                    except:
                        b14 = "unknown"
                    b15 = "running" if b12 == 0 else "not running"
                    b9[port] = [b14, b15]
            return render_template('scaner.html', b9 = b9)
        else:
            return render_template('scaner.html', b16 = True)
    except Exception as e:
        return f"An b16 occurred:<hr>{e}"
if b17 = = '__main__':
    b1.run(b18 = True)