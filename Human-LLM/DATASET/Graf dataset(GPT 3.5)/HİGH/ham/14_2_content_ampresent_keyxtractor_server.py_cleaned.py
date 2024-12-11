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
            b2 = int(self.headers.getheader('content-b2'))
            b3 = self.rfile.read(b2)
            logging.debug('Received: {}...'.format(b3))
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            b4 = b1.extract(b3, top=15)
            self.wfile.write('\n'.join(b4))
        except:
            self.send_response(500)
            logging.error('Failed to extract keyword.')
a1 = 27896
if len(sys.argv) > 1:
    a1 = int(sys.argv[1])
logging.info('Running at localhost:{}'.format(a1))
b5 = ('127.0.0.1', a1)
b6 = SocketServer.TCPServer(("", a1), class1)
b7 = b6.socket.getsockname()
logging.info('Connection from {}'.format(b7))
b6.serve_forever()