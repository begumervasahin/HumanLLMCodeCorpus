import SocketServer
import BaseHTTPServer
import SimpleHTTPServer
import sys
import extractor
import logging
key_extractor = extractor.Extractor()
class MyHTTPServer(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_POST(self, *args):
        try:
            content_length = int(self.headers.getheader('content-length'))
            query = self.rfile.read(content_length)
            logging.debug('Received query: {}...'.format(query))
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            response = key_extractor.extract(query, top=15)
            self.wfile.write('\n'.join(response))
        except Exception as e:
            self.send_response(500)
            logging.error('Failed to extract keyword: {}'.format(str(e)))
DEFAULT_PORT = 27896
if len(sys.argv) > 1:
    port = int(sys.argv[1])
else:
    port = DEFAULT_PORT
logging.info('Server is running at localhost:{}'.format(port))
server_address = ('127.0.0.1', port)
httpd = SocketServer.TCPServer(("", port), MyHTTPServer)
socket_address = httpd.socket.getsockname()
logging.info('Connection from {}'.format(socket_address))
httpd.serve_forever()