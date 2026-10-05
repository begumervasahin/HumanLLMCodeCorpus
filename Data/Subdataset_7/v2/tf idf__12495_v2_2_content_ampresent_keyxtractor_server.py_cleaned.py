import socketserver
import http.server
import sys
import logging
import extractor
b1 = extractor.Extractor()
logging.basicConfig(b2 = logging.DEBUG)
class class1(http.server.BaseHTTPRequestHandler):
    def fonk1(self):
        try:
            b3 = int(self.headers['Content-Length'])
            b4 = self.rfile.read(b3)
            logging.debug('Received: {}...'.format(b4))
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            b5 = b1.extract(b4, top=15)
            self.wfile.write('\n'.join(b5).encode('utf-8'))
        except Exception as e:
            logging.error('Failed to extract keyword: {}'.format(e))
            self.send_response(500)
            self.end_headers()
if b6 = = '__main__':
    a1 = 27896
    if len(sys.argv) > 1:
        a1 = int(sys.argv[1])
    logging.info('Server is running at localhost:{}'.format(a1))
    b7 = ('127.0.0.1', a1)
    b8 = socketserver.TCPServer(b7, class1)
    b9 = b8.socket.getsockname()
    logging.info('Connected to {}'.format(b9))
    try:
        logging.info('Server is running. Press Ctrl+C to shutdown.')
        b8.serve_forever()
    except KeyboardInterrupt:
        logging.info('Server is shutting down...')
        b8.shutdown()