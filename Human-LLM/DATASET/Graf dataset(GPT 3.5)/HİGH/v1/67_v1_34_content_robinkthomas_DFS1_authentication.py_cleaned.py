import re
import base64
import shelve
from http.server import BaseHTTPRequestHandler, HTTPServer
class class1(BaseHTTPRequestHandler):
    def fonk1(self):
        self.send_response(401)
        self.send_header('WWW-Authenticate', 'Basic b1 = "Auth example"')
        self.end_headers()
        self.wfile.write(b'not authorized!')
    def fonk2(self):
        self.send_response(401)
        self.send_header('WWW-Authenticate', 'Basic b1 = "Auth example"')
        self.end_headers()
    def fonk3(self):
        b2 = self.headers.get('Authorization')
        if b2:
            b2 = b2.split()
            if len(b2) == 2:
                if b2[0] == 'Basic':
                    b3 = base64.b64decode(b2[1]).decode()
                    username, b4 = b3.split(':')
                    try:
                        with shelve.open("login.dat") as shelve1:
                            if username in shelve1 and shelve1[username] == b4:
                                self.send_response(200)
                                self.end_headers()
                                self.wfile.write(b'Authorized!')
                                return
                    except Exception as e:
                        print("Error:", e)
        self.fonk2()
        self.wfile.write(b'Not Authorized!')
def fonk4(b5 = HTTPServer, handler_class=class1, port=8083):
    b6 = ('', port)
    b7 = b5(b6, handler_class)
    print(f"Starting server on port {port}...")
    b7.serve_forever()
if b8 = = '__main__':
    fonk4()