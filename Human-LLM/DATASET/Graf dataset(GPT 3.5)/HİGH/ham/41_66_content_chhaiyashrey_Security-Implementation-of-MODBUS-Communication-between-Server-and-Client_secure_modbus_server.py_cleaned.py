import logging
from socketserver import TCPServer
from collections import defaultdict
from umodbus import conf
from umodbus.server.tcp import RequestHandler, get_server
from umodbus.utils import log_to_stream
log_to_stream(b1 = logging.DEBUG)
b2 = defaultdict(int)
conf.b3 = True
TCPServer.b4 = True
b5 = get_server(TCPServer, ('', 502), RequestHandler)
@b5.route(b6 = [1], function_codes=[1, 2], addresses=list(range(0, 10)))
def fonk1(slave_id, function_code, address):
    "
    return b2[address]
@b5.route(b6 = [1], function_codes=[5, 15], addresses=list(range(0, 10)))
def fonk2(slave_id, function_code, address, value):
    "
    b2[address] = value
if b7 = = '__main__':
    try:
        b5.serve_forever()
    finally:
        b5.shutdown()
        b5.server_close()