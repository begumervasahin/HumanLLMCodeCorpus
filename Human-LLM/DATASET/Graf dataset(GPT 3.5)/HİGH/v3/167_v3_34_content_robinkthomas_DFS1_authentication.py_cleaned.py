import re
import base64
import shelve
from http.server import BaseHTTPRequestHandler, HTTPServer
class class1(BaseHTTPRequestHandler):
    def fonk1(self):
        self.fonk3()
    def fonk2(self):
        b1 = self.headers.get('Authorization')
        if b1:
            b2 = self.fonk5(b1)
            if b2:
                username, b3 = b2
                if self.fonk6(username, b3):
                    self.fonk4()
                    return
        self.fonk3()
    def fonk3(self):
        self.send_response(401)
        self.send_header('WWW-Authenticate', 'Basic b4 = "Auth example"')
        self.end_headers()
        self.wfile.write(b'Not Authorized!')
    def fonk4(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Authorized!')
    def fonk5(self, b1):
        try:
            auth_scheme, b5 = b1.split()
            if auth_scheme.lower() == 'basic':
                b6 = base64.b64decode(b5).decode()
                return b6.split(':', 1)
        except Exception as e:
            print("Error parsing authorization header:", e)
        return None
    def fonk6(self, username, b3):
        try:
            with shelve.open("login.dat") as user_db:
                b7 = user_db.get(username)
                if b7 and b7 = = b3:
                    return True
        except Exception as e:
            print("Error authenticating user:", e)
        return False
def fonk7(b8 = HTTPServer, handler_class=class1, port=8083):
    b9 = ('', port)
    b10 = b8(b9, handler_class)
    print(f"Starting server on port {port}...")
    b10.serve_forever()
if b11 = = '__main__':
    fonk7()