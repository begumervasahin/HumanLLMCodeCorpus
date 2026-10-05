import socketserver
import http.server
import sys
import logging
import extractor
key_extractor = extractor.Extractor()
logging.basicConfig(level=logging.DEBUG)
class MyHTTPServer(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            logging.debug('Received: {}...'.format(post_data))
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            response = key_extractor.extract(post_data, top=15)
            self.wfile.write('\n'.join(response).encode('utf-8'))
        except Exception as e:
            logging.error('Failed to extract keyword: {}'.format(e))
            self.send_response(500)
            self.end_headers()
if __name__ == '__main__':
    PORT = 27896
    if len(sys.argv) > 1:
        PORT = int(sys.argv[1])
    logging.info('Running at localhost:{}'.format(PORT))
    server_address = ('127.0.0.1', PORT)
    httpd = socketserver.TCPServer(server_address, MyHTTPServer)
    sa = httpd.socket.getsockname()
    logging.info('Connection from {}'.format(sa))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        logging.info('Server shutting down...')
        httpd.shutdown()