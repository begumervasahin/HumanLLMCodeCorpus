import time
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
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
        response = self.answer()
        self.wfile.write(response.encode('utf-8'))
    def answer(self):
        if "?" not in self.path:
            return "ERROR"
        query_components = parse_qs(urlparse(self.path).query)
        tags = query_components.get('tags', [])
        if not tags:
            return "ERROR"
        tags = tags[0].split(",")
        print("tags == " + str(tags))
        dic = apriori.start(tags)
        print("dic == " + str(dic))
        return str(dic)
if __name__ == '__main__':
    server_class = HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    print("Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print(time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER))