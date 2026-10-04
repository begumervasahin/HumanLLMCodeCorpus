import time
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse as urlparse
import apriori
HOST_NAME = ''
PORT_NUMBER = 9001
class RequestHandler(BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(self.generate_response().encode('utf-8'))
    def generate_response(self):
        if "?" not in self.path:
            return "ERROR"
        query = urlparse.urlparse(self.path).query
        tags = query.split(",")
        print(f"tags == {tags}")
        result_dict = apriori.start(tags)
        print(f"result_dict == {result_dict}")
        return str(result_dict)
def run_server():
    server_address = (HOST_NAME, PORT_NUMBER)
    httpd = HTTPServer(server_address, RequestHandler)
    print(f"Server Starts - {HOST_NAME}:{PORT_NUMBER}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print(f"{time.asctime()} Server Stops - {HOST_NAME}:{PORT_NUMBER}")
if __name__ == '__main__':
    run_server()