import logging
from socketserver import TCPServer
from collections import defaultdict
from umodbus import conf
from umodbus.server.tcp import RequestHandler, get_server
from umodbus.utils import log_to_stream
def fonk1():
    log_to_stream(b1 = logging.DEBUG)
def fonk2():
    return defaultdict(int)
def fonk3():
    conf.b2 = True
def fonk4():
    TCPServer.b3 = True
    return get_server(TCPServer, ('', 502), RequestHandler)
def fonk5(b6, b5):
    @b6.route(b4 = [1], function_codes=[1, 2], addresses=list(range(0, 10)))
    def fonk6(slave_id, function_code, address):
        return b5[address]
    @b6.route(b4 = [1], function_codes=[5, 15], addresses=list(range(0, 10)))
    def fonk7(slave_id, function_code, address, value):
        b5[address] = value
def fonk8(b6):
    try:
        b6.serve_forever()
    finally:
        b6.shutdown()
        b6.server_close()
def fonk9():
    fonk1()
    b5 = fonk2()
    fonk3()
    b6 = fonk4()
    fonk5(b6, b5)
    fonk8(b6)
if b7 = = '__main__':
    fonk9()