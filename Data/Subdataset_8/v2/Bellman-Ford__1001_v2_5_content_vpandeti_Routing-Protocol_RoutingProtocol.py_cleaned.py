from ast import literal_eval
import pickle
import socket
import sys
import threading
import time
SLEEP_TIME = 5
routing_node = sys.argv[1]
is_routing_table_changed = 1
with open(routing_node, 'rb') as file:
    node_routing_table = pickle.load(file)
routing_table = dict(node_routing_table)
print('Node routing table:')
print(routing_table)
timer_ticks = time.time()
def monitor():
    global routing_node, node_routing_table, is_routing_table_changed, routing_table
    while True:
        with open(routing_node, 'rb') as file:
            file_stream = pickle.load(file)
        if file_stream != node_routing_table:
            node_routing_table = dict(file_stream)
            print('Node routing table:', node_routing_table)
            for route in routing_table:
                if route in file_stream:
                    routing_table[route] = file_stream[route]
            print('Current routing table:', routing_table)
            print('Pick time:', time.time() - timer_ticks)
            is_routing_table_changed = 1
        time.sleep(SLEEP_TIME)
def client_thread():
    global routing_node, is_routing_table_changed
    json_file = open('connections', 'r')
    routing_paths = literal_eval(json_file.read())
    print(routing_paths)
    time.sleep(SLEEP_TIME)
    try:
        while True:
            if is_routing_table_changed:
                for route_node in routing_paths[routing_node]:
                    client_socket = socket.socket()
                    port = 12345
                    client_socket.connect((route_node, port))
                    client_socket.settimeout(None)
                    byte_stream = pickle.dumps(routing_table)
                    client_socket.send(byte_stream)
                    client_socket.close()
                is_routing_table_changed = 0
    except Exception as e:
        print(str(e))
def server_thread():
    global routing_node, is_routing_table_changed, timer_ticks
    json_file = open('connections', 'r')
    node_connections = literal_eval(json_file.read())
    print(node_connections)
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port = 12345
        print(port)
        server_socket.bind(('', port))
        server_socket.listen(12)
        while True:
            connection, address = server_socket.accept()
            print('Connection from', address)
            byte_stream = connection.recv(1024)
            routes = pickle.loads(byte_stream)
            source = node_connections[routing_node][address[0]]
            if source in routing_table:
                cost = routing_table[source]
                for neighbour in routes:
                    if neighbour not in routing_table:
                        routing_table[neighbour] = routes[neighbour] + cost
                        is_routing_table_changed = 1
                    else:
                        if routes[neighbour] + cost < routing_table[neighbour]:
                            routing_table[neighbour] = routes[neighbour] + cost
                            is_routing_table_changed = 1
                if is_routing_table_changed:
                    print('\n')
                    print('Updated routing costs:', source, ':', routing_table)
                    print('Elapsed time in ms:', time.time() - timer_ticks)
            connection.close()
    except Exception as e:
        print(str(e))
if __name__ == '__main__':
    global timer_ticks, routing_node
    timer_ticks = time.time()
    print(routing_node)
    threading.Thread(target=server_thread).start()
    threading.Thread(target=client_thread).start()
    threading.Thread(target=monitor).start()
    input()
