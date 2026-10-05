from argparse import ArgumentParser
import socket
import pickle
import time
import math
from threading import Thread, Lock
SOCKET1 = socket.socket(type=socket.SOCK_DGRAM)
PRINT_LOCK = Lock()
INITIAL_CONFIG_FILE = ""
READ_CONFIG_COMP = False
DATA = {
    "router_id": "None",
    "port_no": "None",
    "destinations": [],
    "neighbor": [],
    "distance_vec": [],
    "n_d_vec": {},
    "forw_table": []
}
def current_time():
    return time.time()
def identify_remote_router(remote_address):
    global DATA
    port = remote_address[1]
    for router in DATA["neighbor"]:
        if router[2] == port:
            return router[0]
def distance_of_x_to_y(start_node, end_node):
    global DATA
    all_neighbor_ids = [neighbor[0] for neighbor in DATA["n_d_vec"][start_node]]
    try:
        if end_node in all_neighbor_ids:
            return next(neighbor[1] for neighbor in DATA["n_d_vec"][start_node] if neighbor[0] == end_node)
        else:
            return min(distance_of_x_to_y(start_node, neighbor) + distance_of_x_to_y(neighbor, end_node)
                       for neighbor in all_neighbor_ids)
    except TypeError as node_err:
        with PRINT_LOCK:
            print("The start node is not present in the n_d_vec at this moment.\n{}".format(node_err))
        return math.inf
def bellman_ford(router_id, distance_vector):
    global DATA
    with PRINT_LOCK:
        print("Bellman Ford is running on received data from {}".format(router_id))
    for dest in distance_vector:
        if dest[0] in DATA["destinations"]:
            continue
        else:
            DATA["destinations"].append(dest[0])
    all_neighbor_ids = [neighbor[0] for neighbor in DATA["neighbor"]]
    for dest in DATA["destinations"]:
        if dest in all_neighbor_ids:
            continue
        elif dest in [d[0] for d in DATA["distance_vec"]]:
            continue
        else:
            DATA["distance_vec"].append([dest, math.inf])
    for dest in DATA["distance_vec"]:
        dest[1] = distance_of_x_to_y(DATA["router_id"], dest[0])
def recving():
    global SOCKET1
    global PRINT_LOCK
    global DATA
    while True:
        msg, remote = SOCKET1.recvfrom(1024)
        msg = pickle.loads(msg)
        if msg == "is_alive":
            send_msg = pickle.dumps("yes")
            SOCKET1.sendto(send_msg, remote)
        else:
            remote_router_id = identify_remote_router(remote)
            DATA["n_d_vec"][remote_router_id] = msg
            bellman_ford(remote_router_id, msg)
def sending():
    global DATA
    start = current_time()
    while True:
        if current_time() - start < 10:
            time.sleep(2)
            continue
        else:
            data_to_send = pickle.dumps(DATA["distance_vec"])
            for neighbor in DATA["neighbor"]:
                send_address = ("127.0.0.1", neighbor[2])
                SOCKET1.sendto(data_to_send, send_address)
            start = current_time()
def check_if_alive():
    global SOCKET1
    global PRINT_LOCK
    global DATA
    start = current_time()
    msg = pickle.dumps("is_alive")
    while True:
        if current_time() - start < 10:
            continue
        for neighbor in DATA["neighbor"]:
            remote = ("127.0.0.1", neighbor[2])
            SOCKET1.settimeout(2)
            SOCKET1.sendto(msg, remote)
            try:
                recv_msg = pickle.loads(SOCKET1.recvfrom(512)[0])
                if recv_msg == "yes":
                    with PRINT_LOCK:
                        print("{} is alive".format(neighbor[0]))
            except (OSError, socket.timeout) as e_ra:
                SOCKET1.settimeout(socket.getdefaulttimeout())
                with PRINT_LOCK:
                    print("{} is dead: {}".format(neighbor[0], e_ra))
                index = DATA["neighbor"].index(neighbor)
                DATA["neighbor"].pop(index)
                index = DATA["distance_vec"].index([neighbor[0], neighbor[1]])
                DATA["distance_vec"].pop(index)
                bellman_ford(DATA["router_id"], DATA["distance_vec"])
        start = current_time()
def interface_thread(file_name):
    global INITIAL_CONFIG_FILE
    global READ_CONFIG_COMP
    if READ_CONFIG_COMP:
        start = current_time()
        while True:
            if current_time() - start < 30:
                time.sleep(5)
                continue
            else:
                file1 = open(file_name, "r")
                temp = file1.read()
                file1.close()
                if INITIAL_CONFIG_FILE == temp:
                    start = current_time()
                    continue
                else:
                    list_1 = INITIAL_CONFIG_FILE.split("\n")
                    list_2 = temp.split("\n")
                    diff = [(ind, x[1]) for ind, x in enumerate(zip(list_1, list_2)) if x[0] != x[1]]
                    for ind, new_str in diff:
                        DATA["neighbor"].pop(ind - 1)
                        new_en = [x for x in new_str.split(" ")]
                        new_en[1] = float(new_en[1])
                        new_en[2] = int(new_en[2])
                        DATA["neighbor"].insert(ind - 1, new_en)
                    DATA["n_d_vec"][DATA["router_id"]] = DATA["neighbor"]
                    INITIAL_CONFIG_FILE = temp
                    start = current_time()
def read_config_file(filename):
    global INITIAL_CONFIG_FILE
    global DATA
    with open(filename, "r") as file:
        INITIAL_CONFIG_FILE = file.read()
        file.seek(0)
        no_of_entries = int(file.readline())
        while no_of_entries:
            temp_line = file.readline()
            arguments = temp_line.split(" ")
            DATA["neighbor"].append([arguments[0], float(arguments[1]), int(arguments[2])])
            no_of_entries -= 1
    DATA["n_d_vec"][DATA["router_id"]] = DATA["neighbor"]
def initial_dvec_and_forw_insert():
    global DATA
    for neighbor in DATA["neighbor"]:
        DATA["distance_vec"].append([neighbor[0], neighbor[1]])
        DATA["forw_table"].append([neighbor[0], neighbor[1], DATA["router_id"]])
def main():
    parser = ArgumentParser()
    parser.add_argument("router_id", help="ID of the router")
    parser.add_argument("port_no", help="Port number at which the router is listening", type=int)
    parser.add_argument("router_config_file", help="Configuration file for the router")
    args = parser.parse_args()
    DATA["port"] = args.port_no
    DATA["router_id"] = args.router_id
    read_config_file(args.router_config_file)
    global READ_CONFIG_COMP
    READ_CONFIG_COMP = True
    initial_dvec_and_forw_insert()
    SOCKET1.bind(("", DATA["port"]))
    recv_th = Thread(target=recving)
    recv_th.start()
    send_th = Thread(target=sending)
    send_th.start()
    intf_th = Thread(target=interface_thread, args=(args.router_config_file, ), daemon=True)
    intf_th.start()
    find_th = Thread(target=check_if_alive, daemon=True)
    find_th.start()
if __name__ == "__main__":
    main()