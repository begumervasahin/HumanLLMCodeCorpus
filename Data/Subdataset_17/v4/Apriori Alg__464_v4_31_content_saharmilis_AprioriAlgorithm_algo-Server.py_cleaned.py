import time
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse as urlparse
import apriori
HOST_NAME = ''
PORT_NUMBER = 9001
class MyHandler(BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(self.answer().encode('utf-8'))
    def answer(self):
        if "?" not in self.path:
            return "ERROR"
        tags = urlparse.urlparse(self.path).query.split(",")
        print(f"tags == {tags}")
        dic = apriori.start(tags)
        print(f"dic == {dic}")
        return str(dic)
def run_server():
    server_address = (HOST_NAME, PORT_NUMBER)
    httpd = HTTPServer(server_address, MyHandler)
    print(f"Server Starts - {HOST_NAME}:{PORT_NUMBER}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print(f"{time.asctime()} Server Stops - {HOST_NAME}:{PORT_NUMBER}")
if __name__ == '__main__':
    run_server()