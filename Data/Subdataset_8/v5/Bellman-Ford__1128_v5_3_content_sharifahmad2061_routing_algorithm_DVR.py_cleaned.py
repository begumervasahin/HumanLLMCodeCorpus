import socket
import pickle
import time
import math
from threading import Thread, Lock
from argparse import ArgumentParser
SOCKET = socket.socket(type=socket.SOCK_DGRAM)
PRINT_LOCK = Lock()
INITIAL_CONFIG_FILE = ""
READ_CONFIG_COMPLETED = False
ROUTER_DATA = {
    "router_id": None,
    "port_no": None,
    "destinations": [],
    "neighbor": [],
    "distance_vec": [],
    "n_d_vec": {},
    "forw_table": []
}
def current_time():
    return time.time()
def identify_remote_router(remote_address):
    global ROUTER_DATA
    port = remote_address[1]
    for router in ROUTER_DATA["neighbor"]:
        if router[2] == port:
            return router[0]
def calculate_distance(start_node, end_node):
    global ROUTER_DATA
    all_neighbor_ids = [neighbor[0] for neighbor in ROUTER_DATA["n_d_vec"][start_node]]
    try:
        if end_node in all_neighbor_ids:
            return next(neighbor[1] for neighbor in ROUTER_DATA["n_d_vec"][start_node] if neighbor[0] == end_node)
        else:
            return min(calculate_distance(start_node, neighbor) + calculate_distance(neighbor, end_node)
                       for neighbor in all_neighbor_ids)
    except TypeError as node_err:
        with PRINT_LOCK:
            print("The start node is not present in the n_d_vec at this moment.\n{}".format(node_err))
        return math.inf
def bellman_ford(router_id, distance_vector):
    global ROUTER_DATA
    with PRINT_LOCK:
        print("Bellman Ford is running on received data from {}".format(router_id))
    for dest in distance_vector:
        if dest[0] in ROUTER_DATA["destinations"]:
            continue
        else:
            ROUTER_DATA["destinations"].append(dest[0])
    all_neighbor_ids = [neighbor[0] for neighbor in ROUTER_DATA["neighbor"]]
    for dest in ROUTER_DATA["destinations"]:
        if dest in all_neighbor_ids:
            continue
        elif dest in [d[0] for d in ROUTER_DATA["distance_vec"]]:
            continue
        else:
            ROUTER_DATA["distance_vec"].append([dest, math.inf])
    for dest in ROUTER_DATA["distance_vec"]:
        dest[1] = calculate_distance(ROUTER_DATA["router_id"], dest[0])
def receive_data():
    global SOCKET
    global PRINT_LOCK
    global ROUTER_DATA
    while True:
        msg, remote = SOCKET.recvfrom(1024)
        msg = pickle.loads(msg)
        if msg == "is_alive":
            send_msg = pickle.dumps("yes")
            SOCKET.sendto(send_msg, remote)
        else:
            remote_router_id = identify_remote_router(remote)
            ROUTER_DATA["n_d_vec"][remote_router_id] = msg
            bellman_ford(remote_router_id, msg)
def send_data():
    global ROUTER_DATA
    start_time = current_time()
    while True:
        if current_time() - start_time < 10:
            time.sleep(2)
            continue
        else:
            data_to_send = pickle.dumps(ROUTER_DATA["distance_vec"])
            for neighbor in ROUTER_DATA["neighbor"]:
                send_address = ("127.0.0.1", neighbor[2])
                SOCKET.sendto(data_to_send, send_address)
            start_time = current_time()
def check_neighbor_alive():
    global SOCKET
    global PRINT_LOCK
    global ROUTER_DATA
    start_time = current_time()
    msg = pickle.dumps("is_alive")
    while True:
        if current_time() - start_time < 10:
            continue
        for neighbor in ROUTER_DATA["neighbor"]:
            remote = ("127.0.0.1", neighbor[2])
            SOCKET.settimeout(2)
            SOCKET.sendto(msg, remote)
            try:
                recv_msg = pickle.loads(SOCKET.recvfrom(512)[0])
                if recv_msg == "yes":
                    with PRINT_LOCK:
                        print("{} is alive".format(neighbor[0]))
            except (OSError, socket.timeout) as e_ra:
                SOCKET.settimeout(socket.getdefaulttimeout())
                with PRINT_LOCK:
                    print("{} is dead: {}".format(neighbor[0], e_ra))
                index = ROUTER_DATA["neighbor"].index(neighbor)
                ROUTER_DATA["neighbor"].pop(index)
                index = ROUTER_DATA["distance_vec"].index([neighbor[0], neighbor[1]])
                ROUTER_DATA["distance_vec"].pop(index)
                bellman_ford(ROUTER_DATA["router_id"], ROUTER_DATA["distance_vec"])
        start_time = current_time()
def interface_thread(file_name):
    global INITIAL_CONFIG_FILE
    global READ_CONFIG_COMPLETED
    if READ_CONFIG_COMPLETED:
        start_time = current_time()
        while True:
            if current_time() - start_time < 30:
                time.sleep(5)
                continue
            else:
                file1 = open(file_name, "r")
                temp = file1.read()
                file1.close()
                if INITIAL_CONFIG_FILE == temp:
                    start_time = current_time()
                    continue
                else:
                    list_1 = INITIAL_CONFIG_FILE.split("\n")
                    list_2 = temp.split("\n")
                    diff = [(ind, x[1]) for ind, x in enumerate(zip(list_1, list_2)) if x[0] != x[1]]
                    for ind, new_str in diff:
                        ROUTER_DATA["neighbor"].pop(ind - 1)
                        new_en = [x for x in new_str.split(" ")]
                        new_en[1] = float(new_en[1])
                        new_en[2] = int(new_en[2])
                        ROUTER_DATA["neighbor"].insert(ind - 1, new_en)
                    ROUTER_DATA["n_d_vec"][ROUTER_DATA["router_id"]] = ROUTER_DATA["neighbor"]
                    INITIAL_CONFIG_FILE = temp
                    start_time = current_time()
def read_config_file(filename):
    global INITIAL_CONFIG_FILE
    global ROUTER_DATA
    with open(filename, "r") as file:
        INITIAL_CONFIG_FILE = file.read()
        file.seek(0)
        no_of_entries = int(file.readline())
        while no_of_entries:
            temp_line = file.readline()
            arguments = temp_line.split(" ")
            ROUTER_DATA["neighbor"].append([arguments[0], float(arguments[1]), int(arguments[2])])
            no_of_entries -= 1
    ROUTER_DATA["n_d_vec"][ROUTER_DATA["router_id"]] = ROUTER_DATA["neighbor"]
def initialize_distance_vector():
    global ROUTER_DATA
    for neighbor in ROUTER_DATA["neighbor"]:
        ROUTER_DATA["distance_vec"].append([neighbor[0], neighbor[1]])
        ROUTER_DATA["forw_table"].append([neighbor[0], neighbor[1], ROUTER_DATA["router_id"]])
def main():
    parser = ArgumentParser()
    parser.add_argument("router_id", help="ID of the router")
    parser.add_argument("port_no", help="Port number at which the router is listening", type=int)
    parser.add_argument("router_config_file", help="Configuration file for the router")
    args = parser.parse_args()
    ROUTER_DATA["port_no"] = args.port_no
    ROUTER_DATA["router_id"] = args.router_id
    read_config_file(args.router_config_file)
    global READ_CONFIG_COMPLETED
    READ_CONFIG_COMPLETED = True
    initialize_distance_vector()
    SOCKET.bind(("", ROUTER_DATA["port_no"]))
    recv_thread = Thread(target=receive_data)
    recv_thread.start()
    send_thread = Thread(target=send_data)
    send_thread.start()
    intf_thread = Thread(target=interface_thread, args=(args.router_config_file, ), daemon=True)
    intf_thread.start()
    find_thread = Thread(target=check_neighbor_alive, daemon=True)
    find_thread.start()
if __name__ == "__main__":
    main()