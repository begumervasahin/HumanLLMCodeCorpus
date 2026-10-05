import SocketServer
import BaseHTTPServer
import SimpleHTTPServer
import sys
import extractor
import logging
b1 = extractor.Extractor()
class class1(BaseHTTPServer.BaseHTTPRequestHandler):
    def fonk1(self, *args):
        try:
            b2 = int(self.headers.getheader('content-length'))
            b3 = self.rfile.read(b2)
            logging.debug('Received b3: {}...'.format(b3))
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            b4 = b1.extract(b3, top=15)
            self.wfile.write('\n'.join(b4))
        except Exception as e:
            self.send_response(500)
            logging.error('Failed to extract keyword: {}'.format(str(e)))
a1 = 27896
if len(sys.argv) > 1:
    b5 = int(sys.argv[1])
else:
    b5 = a1
logging.info('Server is running at localhost:{}'.format(b5))
b6 = ('127.0.0.1', b5)
b7 = SocketServer.TCPServer(("", b5), class1)
b8 = b7.socket.getsockname()
logging.info('Connection from {}'.format(b8))
b7.serve_forever()