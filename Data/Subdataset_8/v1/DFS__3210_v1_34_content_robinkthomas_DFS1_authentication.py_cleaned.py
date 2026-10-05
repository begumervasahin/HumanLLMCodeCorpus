import re
import base64
import shelve
from http.server import BaseHTTPRequestHandler, HTTPServer
class MyRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(401)
        self.send_header('WWW-Authenticate', 'Basic realm="Auth example"')
        self.end_headers()
        self.wfile.write(b'not authorized!')
    def do_AUTHHEAD(self):
        self.send_response(401)
        self.send_header('WWW-Authenticate', 'Basic realm="Auth example"')
        self.end_headers()
    def do_POST(self):
        auth_header = self.headers.get('Authorization')
        if auth_header:
            auth_header = auth_header.split()
            if len(auth_header) == 2:
                if auth_header[0] == 'Basic':
                    auth_decoded = base64.b64decode(auth_header[1]).decode()
                    username, password = auth_decoded.split(':')
                    try:
                        with shelve.open("login.dat") as shelve1:
                            if username in shelve1 and shelve1[username] == password:
                                self.send_response(200)
                                self.end_headers()
                                self.wfile.write(b'Authorized!')
                                return
                    except Exception as e:
                        print("Error:", e)
        self.do_AUTHHEAD()
        self.wfile.write(b'Not Authorized!')
def run(server_class=HTTPServer, handler_class=MyRequestHandler, port=8083):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}...")
    httpd.serve_forever()
if __name__ == '__main__':
    run()