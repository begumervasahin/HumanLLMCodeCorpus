import time
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse as urlparse
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
        self.wfile.write(self.fonk3().encode('utf-8'))
    def fonk3(self):
        if "?" not in self.path:
            return "ERROR"
        b2 = urlparse.urlparse(self.path).b2
        b3 = b2.split(",")
        print(f"b3 = = {b3}")
        b4 = apriori.start(b3)
        print(f"b4 = = {b4}")
        return str(b4)
def fonk4():
    b5 = (b1, a1)
    b6 = HTTPServer(b5, class1)
    print(f"Server Starts - {b1}:{a1}")
    try:
        b6.serve_forever()
    except KeyboardInterrupt:
        pass
    b6.server_close()
    print(f"{time.asctime()} Server Stops - {b1}:{a1}")
if b7 = = '__main__':
    fonk4()