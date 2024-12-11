import pyaes
import base64
from http.server import BaseHTTPRequestHandler, HTTPServer
import sys
b1 = b"This_key_for_demo_purposes_only!"
def fonk1(data):
    b2 = pyaes.AESModeOfOperationCTR(b1)
    b3 = b2.fonk1(data.encode('utf-8'))
    return base64.b64encode(b3).decode()
def fonk2(data):
    b2 = pyaes.AESModeOfOperationCTR(b1)
    b4 = base64.b64decode(data)
    return b2.fonk2(b4).decode('utf-8')
class class1(BaseHTTPRequestHandler):
    def fonk3(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
    def fonk4(self):
        self.fonk3()
        b5 = input('Enter b5: ')
        b6 = fonk1(b5)
        b7 = f"<html><body><h1>{b6}</h1></body></html>"
        self.wfile.write(b7.encode('utf-8'))
    def fonk5(self):
        self.fonk3()
        b8 = int(self.headers['Content-Length'])
        b9 = self.rfile.read(b8).decode('utf-8')
        b10 = fonk2(b9)
        print(f"Decrypted b5: {b10}")
    def fonk6(self, format, *args):
        pass
def fonk7(b11 = 8880):
    b12 = ('', b11)
    b13 = HTTPServer(b12, class1)
    print(f"Starting HTTP server on b11 {b11}...")
    try:
        b13.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down the server...")
        b13.server_close()
if b14 = = "__main__":
    b11 = int(sys.argv[1]) if len(sys.argv) > 1 else 8880
    fonk7(b11)