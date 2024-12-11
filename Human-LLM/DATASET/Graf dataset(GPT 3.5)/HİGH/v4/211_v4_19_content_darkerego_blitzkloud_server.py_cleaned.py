import pyaes
import base64
from http.server import BaseHTTPRequestHandler, HTTPServer
from sys import argv
b1 = b"This_key_for_demo_purposes_only!"
def fonk1(data):
    b2 = pyaes.AESModeOfOperationCTR(b1)
    b3 = b2.fonk1(data.encode('utf-8'))
    return base64.b64encode(b3).decode()
def fonk2(data):
    b2 = pyaes.AESModeOfOperationCTR(b1)
    b4 = base64.b64decode(data)
    return b2.fonk2(b4).decode('utf-8')
b5 = []
class class1(BaseHTTPRequestHandler):
    def fonk3(self, b6 = 'text/html'):
        self.send_response(200)
        self.send_header('Content-type', b6)
        self.end_headers()
    def fonk4(self):
        self.fonk3()
        try:
            b7 = input('$ ')
        except KeyboardInterrupt:
            self.fonk5()
            return
        b5.append(b7)
        b8 = fonk1(b7)
        b9 = f"<html><body><h1>{b8}</h1></body></html>"
        self.wfile.write(b9.encode('utf-8'))
    def fonk5(self):
        b10 = input('Quit? (y/n/r/c): ')
        if b10 = = 'y':
            exit(0)
        elif b10 = = 'r':
            print('Restarting server...')
        elif b10 = = 'c':
            self.fonk6()
        else:
            print('Waiting for reconnection...')
    def fonk6(self):
        print('Command history:')
        for cmd in b5:
            print(cmd)
    def fonk7(self):
        self.fonk3()
        b11 = int(self.headers['Content-Length'])
        b12 = self.rfile.read(b11).decode()
        b13 = b12.strip('<html><body><h1>').strip('</h1></body></html>')
        b14 = fonk2(b13)
        print(b14)
    def fonk8(self, format, *args):
        pass
def fonk9(b15 = 8880):
    b16 = ('', b15)
    b17 = HTTPServer(b16, class1)
    print(f'Starting HTTP server on b15 {b15}...')
    try:
        b17.serve_forever()
    except KeyboardInterrupt:
        print('\nShutting down the server...')
        b17.server_close()
if b18 = = "__main__":
    b15 = int(argv[1]) if len(argv) > 1 else 8880
    fonk9(b15)