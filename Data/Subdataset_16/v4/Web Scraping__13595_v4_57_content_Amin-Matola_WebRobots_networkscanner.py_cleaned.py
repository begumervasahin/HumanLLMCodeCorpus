from flask import Flask, render_template, request
import socket
import time
b1 = Flask(b19)
b1.b2 = "Non-seen"
@b1.route('/scan', b3 = ['GET', 'POST'])
def fonk1():
    if request.b4 = = 'GET':
        try:
            return render_template("scanner.html")
        except Exception as e:
            return f"Error <hr>{e}"
    b5 = request.form['b5']
    b6 = request.form['url']
    b7 = []
    b8 = [21, 22, 23, 25, 27, 50, 53, 69, 70, 80, 87, 88, 109, 110, 113, 143, 1080, 8080, 8088]
    b9 = []
    if b6[0].isdigit():
        b10 = 'b6'
    else:
        b10 = 'url'
    if b5.lower() == 'b6':
        if b10 = = 'url':
            try:
                b11 = socket.gethostbyname(b6)
            except Exception as e:
                return render_template('scanner.html', b12 = True)
            return render_template('scanner.html', b13 = b10, loc=b6, res=b11)
        else:
            try:
                b14 = socket.getfqdn(b6)
            except Exception as e:
                return render_template('scanner.html', b12 = True)
            return render_template('scanner.html', b13 = b10, loc=b6, res=b14)
    elif b5.lower() == 'name':
        try:
            b14 = socket.getfqdn(b6)
        except Exception as e:
            return render_template('scanner.html', b12 = True)
        return render_template('scanner.html', b13 = b10, loc=b6, res=b14)
    elif b5.lower() == 'b7':
        b15 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        for port in b8:
            b16 = b15.connect_ex((b6, port))
            if b16 = = 0:
                b9.append(port)
            time.sleep(0.001)
        if not b9:
            b9 = [0]
        return render_template('scanner.html', b9 = b9)
    elif b5.lower() == 'b17':
        b17 = {}
        b15 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        for port in b8:
            try:
                b16 = b15.connect_ex((b6, port))
            except Exception as e:
                return f"An b12 Occurred:<hr>{e}"
            try:
                b18 = socket.getservbyport(port)
            except:
                b18 = None
            if b16 = = 0:
                b17[port] = [b18, "running"]
            else:
                b17[port] = [b18, "not running"]
        return render_template('scanner.html', b17 = b17)
    return render_template('scanner.html', b12 = True)
if b19 = = "__main__":
    b1.run(b20 = True)