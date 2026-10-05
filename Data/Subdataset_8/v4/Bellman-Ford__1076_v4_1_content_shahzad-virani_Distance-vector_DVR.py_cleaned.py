import threading
import time
import math
from socket import socket, AF_INET, SOCK_DGRAM
import sys
import os
SUSPEND_AFTER_TIMEOUT = 3.0
class Path:
    def __init__(self, distance, next_hop):
        self.distance = distance
        self.next_hop = next_hop
    def equals(self, other_path):
        return self.distance == other_path.distance and self.next_hop == other_path.next_hop
class Neighbour:
    def __init__(self, link_cost, port, timeout):
        self.link_cost = link_cost
        self.port = port
        self.timeout = timeout
        self.paths = {}
router_ID = ''
router_port = 0
router_filename = ''
router_neighbours = {}
router_routes = {}
lock = threading.Lock()
def create_packet(dest_id, send_link_cost):
    packet = f"{router_ID}"
    if send_link_cost:
        packet += f" {router_neighbours[dest_id].link_cost}"
    packet += '\n'
    for id, path in router_routes.items():
        if path.next_hop == dest_id:
            packet += f"{id} {math.inf}\n"
        else:
            packet += f"{id} {path.distance}\n"
    return bytes(packet, 'utf-8')
def send_distance_vector(send_link_cost):
    send_socket = socket(AF_INET, SOCK_DGRAM)
    lock.acquire()
    for id, neighbour in router_neighbours.items():
        send_socket.sendto(create_packet(id, send_link_cost), ('localhost', neighbour.port))
    lock.release()
    send_socket.close()
def print_table():
    header = '\t' + '\t'.join(sorted(router_routes.keys()))
    print(header)
    row_router = f"{router_ID}\t" + '\t'.join([f"{route.distance:.1f}" for route in sorted(router_routes.values())])
    print(row_router)
    for id, neighbour in sorted(router_neighbours.items()):
        row = f"{id}\t{neighbour.link_cost}"
        row += '\t' + '\t'.join([f"{neighbour.paths[route_ID].distance:.1f}" for route_ID in sorted(router_routes.keys())])
        print(row)
    print('')
def timeout_check():
    while True:
        time.sleep(1)
        for id, neighbour in router_neighbours.items():
            s = socket(AF_INET, SOCK_DGRAM)
            try:
                s.bind(('localhost', neighbour.port))
                s.close()
                if neighbour.link_cost != math.inf:
                    lock.acquire()
                    router_routes[id].distance = math.inf
                    neighbour.link_cost = math.inf
                    neighbour.timeout = time.time()
                    for key2, item2 in router_routes.items():
                        if item2.next_hop == id:
                            item2.distance = math.inf
                    lock.release()
                    send_distance_vector(False)
                    threading.Timer(SUSPEND_AFTER_TIMEOUT, target=bellman_ford).start()
            except Exception as e:
                pass
def listen():
    listen_socket = socket(AF_INET, SOCK_DGRAM)
    listen_socket.bind(('localhost', router_port))
    while True:
        message, socket_address = listen_socket.recvfrom(2048)
        lines = message.decode('utf-8').split('\n')
        first_line = lines[0].split()
        source = first_line[0]
        router_neighbours[source].timeout = -1.0
        if len(first_line) > 1:
            router_neighbours[source].link_cost = float(first_line[1])
            router_neighbours[source].timeout = -1
        lock.acquire()
        for line in lines[1:]:
            if line:
                tokens = line.split()
                new_path = Path(float(tokens[1]), 'direct')
                if tokens[0] not in router_neighbours[source].paths:
                    new_node(tokens[0])
                if not router_neighbours[source].paths[tokens[0]].equals(new_path):
                    router_neighbours[source].paths[tokens[0]] = new_path
        threading.Thread(target=bellman_ford).start()
        lock.release()
def new_node(name):
    global router_neighbours
    p = Path(math.inf, 'direct')
    router_routes[name] = p
    for id, neighbour in router_neighbours.items():
        neighbour.paths[name] = p
def bellman_ford():
    global router_routes
    is_changed = False
    lock.acquire()
    for id, route in router_routes.items():
        m_list = []
        if id == router_ID:
            continue
        if id in router_neighbours:
            if time.time() > router_neighbours[id].timeout and time.time() < router_neighbours[id].timeout + SUSPEND_AFTER_TIMEOUT:
                router_routes[id] = Path(math.inf, 'direct')
                continue
            else:
                m_list.append(Path(router_neighbours[id].link_cost, 'direct'))
        for id2, neighbour in router_neighbours.items():
            p = Path(router_neighbours[id2].link_cost + neighbour.paths[id].distance, id2)
            m_list.append(p)
        m_list.append(p)
        m = min(m_list, key=lambda x: x.distance)
        if not router_routes[id].equals(Path(m.distance, m.next_hop)):
            router_routes[id] = Path(m.distance, m.next_hop)
            is_changed = True
    lock.release()
    if is_changed:
        send_distance_vector(False)
def menu():
    while True:
        print(f"\n****I AM ROUTER {router_ID}****\n")
        option = int(input("1: Display Costs.\n2: Display distance vector table.\n3: Edit link costs\n4: Quit\nYour choice: "))
        if option == 1:
            print("Destination\tNext Hop\tDistance")
            for id, route in sorted(router_routes.items()):
                if id != router_ID:
                    print(f"     {id}\t\t{route.next_hop}\t\t{route.distance:.1f}")
        elif option == 2:
            print_table()
        elif option == 3:
            print("Neighbours:", ' '.join(sorted(router_neighbours.keys())))
            to_edit = input("Enter which link to edit: ")
            new_distance = float(input(f"Enter new distance for {to_edit}: "))
            router_neighbours[to_edit].link_cost = new_distance
            send_socket = socket(AF_INET, SOCK_DGRAM)
            lock.acquire()
            send_socket.sendto(create_packet(to_edit, True), ('localhost', router_neighbours[to_edit].port))
            lock.release()
            send_socket.close()
            threading.Thread(target=bellman_ford).start()
        elif option == 4:
            os._exit(-1)
if __name__ == '__main__':
    try:
        router_ID = sys.argv[1]
        router_port = int(sys.argv[2])
        router_filename = sys.argv[3]
    except (ValueError, IndexError):
        print("Incorrect command-line arguments.\nDVR.py <ID> <port> <filename>")
        exit(0)
    print(f"Router {router_ID}")
    router_routes[router_ID] = Path(0, 'direct')
    with open(router_filename) as file:
        lines = file.readlines()
        for line