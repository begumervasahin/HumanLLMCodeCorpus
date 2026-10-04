import time
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import apriori
b1 = ''
a1 = 9001
class class1(BaseHTTPRequestHandler):
    def fonk1(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
    def fonk2(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        b2 = self.fonk3()
        self.wfile.write(b2.encode('utf-8'))
    def fonk3(self):
        if "?" not in self.path:
            return "ERROR"
        b3 = parse_qs(urlparse(self.path).query)
        b4 = b3.get('b4', [])
        if not b4:
            return "ERROR"
        b4 = b4[0].split(",")
        print(f"b4 = = {b4}")
        b5 = apriori.start(b4)
        print(f"b5 = = {b5}")
        return str(b5)
if b6 = = '__main__':
    b7 = HTTPServer
    b8 = b7((b1, a1), class1)
    print(f"Server Starts - {b1}:{a1}")
    try:
        b8.serve_forever()
    except KeyboardInterrupt:
        pass
    b8.server_close()
    print(time.asctime(), f"Server Stops - {b1}:{a1}")