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
            return "ERROR: No query parameters found."
        b3 = parse_qs(urlparse(self.path).query)
        b4 = b3.get('b4', [])
        if not b4:
            return "ERROR: 'b4' parameter is missing."
        b4 = b4[0].split(",")
        print(f"Received b4: {b4}")
        b5 = apriori.start(b4)
        print(f"Apriori b5: {b5}")
        return str(b5)
def fonk4():
    b6 = (b1, a1)
    b7 = HTTPServer(b6, class1)
    print(f"Server Starts - {b1}:{a1}")
    try:
        b7.serve_forever()
    except KeyboardInterrupt:
        pass
    b7.server_close()
    print(time.asctime(), f"Server Stops - {b1}:{a1}")
if b8 = = '__main__':
    fonk4()