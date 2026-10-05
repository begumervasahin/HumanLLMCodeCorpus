import logging
from socketserver import TCPServer
from collections import defaultdict
from umodbus import conf
from umodbus.server.tcp import RequestHandler, get_server
from umodbus.utils import log_to_stream
log_to_stream(level=logging.DEBUG)
data_store = defaultdict(int)
conf.SIGNED_VALUES = True
TCPServer.allow_reuse_address = True
app = get_server(TCPServer, ('', 502), RequestHandler)
@app.route(slave_ids=[1], function_codes=[1, 2], addresses=list(range(0, 10)))
def read_data_store(slave_id, function_code, address):
    "
    return data_store[address]
@app.route(slave_ids=[1], function_codes=[5, 15], addresses=list(range(0, 10)))
def write_data_store(slave_id, function_code, address, value):
    "
    data_store[address] = value
if __name__ == '__main__':
    try:
        app.serve_forever()
    finally:
        app.shutdown()
        app.server_close()