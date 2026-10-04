import time
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
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
        response = self.process_request()
        self.wfile.write(response.encode('utf-8'))
    def process_request(self):
        if "?" not in self.path:
            return "ERROR: No query parameters found."
        query_components = parse_qs(urlparse(self.path).query)
        tags = query_components.get('tags', [])
        if not tags:
            return "ERROR: 'tags' parameter is missing."
        tags = tags[0].split(",")
        print(f"Received tags: {tags}")
        results = apriori.start(tags)
        print(f"Apriori results: {results}")
        return str(results)
def run_server():
    server_address = (HOST_NAME, PORT_NUMBER)
    httpd = HTTPServer(server_address, RequestHandler)
    print(f"Server Starts - {HOST_NAME}:{PORT_NUMBER}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print(time.asctime(), f"Server Stops - {HOST_NAME}:{PORT_NUMBER}")
if __name__ == '__main__':
    run_server()