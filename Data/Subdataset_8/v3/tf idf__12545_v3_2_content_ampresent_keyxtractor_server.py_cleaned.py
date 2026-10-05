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
            logging.debug(f'Received data: {post_data[:50]}...')
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            response = key_extractor.extract(post_data, top=15)
            self.wfile.write('\n'.join(response).encode('utf-8'))
        except Exception as e:
            logging.error(f'Error during keyword extraction: {e}')
            self.send_response(500)
            self.end_headers()
if __name__ == '__main__':
    DEFAULT_PORT = 27896
    if len(sys.argv) > 1:
        PORT = int(sys.argv[1])
    else:
        PORT = DEFAULT_PORT
    logging.info(f'Server is running at localhost:{PORT}')
    server_address = ('127.0.0.1', PORT)
    httpd = socketserver.TCPServer(server_address, MyHTTPServer)
    logging.info(f'Server is connected to {server_address}')
    try:
        logging.info('Server is running. Press Ctrl+C to shutdown.')
        httpd.serve_forever()
    except KeyboardInterrupt:
        logging.info('Server is shutting down...')
        httpd.shutdown()