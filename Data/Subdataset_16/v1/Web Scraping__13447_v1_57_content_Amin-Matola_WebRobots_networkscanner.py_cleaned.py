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
    try:
        if b5.lower() == 'b6':
            if b6[0].isdigit():
                b9 = socket.getfqdn(b6)
            else:
                b9 = socket.gethostbyname(b6)
            return render_template('scaner.html', b10 = b5, loc=b6, res=b9)
        elif b5.lower() == 'name':
            b9 = socket.getfqdn(b6)
            return render_template('scaner.html', b10 = b5, loc=b6, res=b9)
        elif b5.lower() == 'ports':
            b11 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            for port in b7:
                b12 = b11.connect_ex((b6, port))
                if b12 = = 0:
                    b8.append(port)
                time.sleep(0.001)
            if len(b8) <= 0:
                b8 = [0]
            return render_template('scaner.html', b8 = b8)
        elif b5.lower() == 'b15':
            b13 = {}
            b11 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            for port in b7:
                b12 = b11.connect_ex((b6, port))
                try:
                    b14 = socket.getservbyport(port)
                except:
                    b14 = "unknown"
                if b12 = = 0:
                    b13[port] = [b14, "running"]
                else:
                    b13[port] = [b14, "not running"]
            return render_template('scaner.html', b15 = b13)
        else:
            return render_template('scaner.html', b16 = True)
    except Exception as e:
        return f"An b16 occurred:<hr>{e}"
if b17 = = '__main__':
    b1.run(b18 = True)