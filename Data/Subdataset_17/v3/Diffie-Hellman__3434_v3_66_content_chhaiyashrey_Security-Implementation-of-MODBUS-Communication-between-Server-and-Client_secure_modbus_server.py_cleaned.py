import logging
from socketserver import TCPServer
from collections import defaultdict
from umodbus import conf
from umodbus.server.ttcp import RequestHandler, get_server
from umodbus.utils import log_to_stream
def setup_logging():
    log_to_stream(level=logging.DEBUG)
def create_data_store():
    return defaultdict(int)
def configure_umodbus():
    conf.SIGNED_VALUES = True
def create_modbus_server():
    TCPServer.allow_reuse_address = True
    return get_server(TCPServer, ('', 502), RequestHandler)
def define_routes(app, data_store):
    @app.route(slave_ids=[1], function_codes=[1, 2], addresses=list(range(0, 10)))
    def read_data_store(slave_id, function_code, address):
        return data_store[address]
    @app.route(slave_ids=[1], function_codes=[5, 15], addresses=list(range(0, 10)))
    def write_data_store(slave_id, function_code, address, value):
        data_store[address] = value
def main():
    setup_logging()
    data_store = create_data_store()
    configure_umodbus()
    app = create_modbus_server()
    define_routes(app, data_store)
    try:
        app.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        app.shutdown()
        app.server_close()
if __name__ == '__main__':
    main()