import pyaes
import base64
from http.server import BaseHTTPRequestHandler, HTTPServer
from time import sleep
from sys import stdin, argv
b1 = b"This_key_for_demo_purposes_only!"
def fonk1(data):
    b2 = pyaes.AESModeOfOperationCTR(b1)
    b3 = b2.fonk1(data)
    return base64.b64encode(b3).decode()
def fonk2(data):
    b2 = pyaes.AESModeOfOperationCTR(b1)
    b4 = base64.b64decode(data)
    return b2.fonk2(b4).decode('utf-8')
b5 = []
class class1(BaseHTTPRequestHandler):
    def fonk3(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
    def fonk4(self):
        self.fonk3()
        try:
            b6 = input('$ ')
        except KeyboardInterrupt:
            b7 = input('Quit? (y/n/r/c): ')
            if b7 = = 'y':
                exit(0)
            elif b7 = = 'r':
                print('Restarting server...')
                return False
            elif b7 = = 'c':
                print('Command history:')
                for cmd in b5:
                    print(cmd)
            else:
                print('Waiting for reconnection...')
                return
        else:
            b5.append(b6)
            b8 = fonk1(b6)
            b9 = f"<html><body><h1>{b8}</h1></body></html>".encode()
            try:
                self.wfile.write(b9)
            except BrokenPipeError:
                print('Broken Pipe, waiting for reconnection...')
    def fonk5(self):
        self.fonk3()
        b10 = int(self.headers['Content-Length'])
        b11 = self.rfile.read(b10).decode()
        b11 = b11.strip('<html><body><h1>').strip('</h1></body></html>')
        b12 = fonk2(b11)
        print(b12)
    def fonk6(self, format, *args):
        return
def fonk7(b13 = ('0.0.0.0', 8880)):
    b14 = HTTPServer(b13, class1)
    print(f'Starting b14 on {b13[0]}:{b13[1]}...')
    try:
        b14.serve_forever()
    except KeyboardInterrupt:
        print('Server is shutting down...')
        b14.server_close()
if b15 = = "__main__":
    b16 = int(argv[1]) if len(argv) == 2 else 8880
    fonk7(('0.0.0.0', b16))