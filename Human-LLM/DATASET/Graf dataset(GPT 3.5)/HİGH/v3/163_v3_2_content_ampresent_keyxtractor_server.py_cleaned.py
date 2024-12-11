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
            logging.debug(f'Received data: {b4[:50]}...')
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            b5 = b1.extract(b4, top=15)
            self.wfile.write('\n'.join(b5).encode('utf-8'))
        except Exception as e:
            logging.error(f'Error during keyword extraction: {e}')
            self.send_response(500)
            self.end_headers()
if b6 = = '__main__':
    a1 = 27896
    if len(sys.argv) > 1:
        b7 = int(sys.argv[1])
    else:
        b7 = a1
    logging.info(f'Server is running at localhost:{b7}')
    b8 = ('127.0.0.1', b7)
    b9 = socketserver.TCPServer(b8, class1)
    logging.info(f'Server is connected to {b8}')
    try:
        logging.info('Server is running. Press Ctrl+C to shutdown.')
        b9.serve_forever()
    except KeyboardInterrupt:
        logging.info('Server is shutting down...')
        b9.shutdown()