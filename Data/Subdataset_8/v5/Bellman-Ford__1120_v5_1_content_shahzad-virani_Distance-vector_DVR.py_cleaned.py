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
class Neighbor:
    def __init__(self, link_cost, port, timeout):
        self.link_cost = link_cost
        self.port = port
        self.timeout = timeout
        self.paths = {}
router_id = ''
router_port = 0
router_filename = ''
router_neighbors = {}
router_routes = {}
lock = threading.Lock()
def create_packet(dest_id, send_link_cost):
    packet = f"{router_id}"
    if send_link_cost:
        packet += f" {router_neighbors[dest_id].link_cost}"
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
    for id, neighbor in router_neighbors.items():
        send_socket.sendto(create_packet(id, send_link_cost), ('localhost', neighbor.port))
    lock.release()
    send_socket.close()
def print_table():
    header = '\t' + '\t'.join(sorted(router_routes.keys()))
    print(header)
    row_router = f"{router_id}\t" + '\t'.join([f"{route.distance:.1f}" for route in sorted(router_routes.values())])
    print(row_router)
    for id, neighbor in sorted(router_neighbors.items()):
        row = f"{id}\t{neighbor.link_cost}"
        row += '\t' + '\t'.join([f"{neighbor.paths[route_id].distance:.1f}" for route_id in sorted(router_routes.keys())])
        print(row)
    print('')
def timeout_check():
    while True:
        time.sleep(1)
        for id, neighbor in router_neighbors.items():
            s = socket(AF_INET, SOCK_DGRAM)
            try:
                s.bind(('localhost', neighbor.port))
                s.close()
                if neighbor.link_cost != math.inf:
                    lock.acquire()
                    router_routes[id].distance = math.inf
                    neighbor.link_cost = math.inf
                    neighbor.timeout = time.time()
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
        router_neighbors[source].timeout = -1.0
        if len(first_line) > 1:
            router_neighbors[source].link_cost = float(first_line[1])
            router_neighbors[source].timeout = -1
        lock.acquire()
        for line in lines[1:]:
            if line:
                tokens = line.split()
                new_path = Path(float(tokens[1]), 'direct')
                if tokens[0] not in router_neighbors[source].paths:
                    new_node(tokens[0])
                if not router_neighbors[source].paths[tokens[0]].equals(new_path):
                    router_neighbors[source].paths[tokens[0]] = new_path
        threading.Thread(target=bellman_ford).start()
        lock.release()
def new_node(name):
    global router_neighbors
    p = Path(math.inf, 'direct')
    router_routes[name] = p
    for id, neighbor in router_neighbors.items():
        neighbor.paths[name] = p
def bellman_ford():
    global router_routes
    is_changed = False
    lock.acquire()
    for id, route in router_routes.items():
        m_list = []
        if id == router_id:
            continue
        if id in router_neighbors:
            if time.time() > router_neighbors[id].timeout and time.time() < router_neighbors[id].timeout + SUSPEND_AFTER_TIMEOUT:
                router_routes[id] = Path(math.inf, 'direct')
                continue
            else:
                m_list.append(Path(router_neighbors[id].link_cost, 'direct'))
        for id2, neighbor in router_neighbors.items():
            p = Path(router_neighbors[id2].link_cost + neighbor.paths[id].distance, id2)
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
        print(f"\n****I AM ROUTER {router_id}****\n")
        option = int(input("1: Display Costs.\n2: Display distance vector table.\n3: Edit link costs\n4: Quit\nYour choice: "))
        if option == 1:
            print("Destination\tNext Hop\tDistance")
            for id, route in sorted(router_routes.items()):
                if id != router_id:
                    print(f"     {id}\t\t{route.next_hop}\t\t{route.distance:.1f}")
        elif option == 2:
            print_table()
        elif option == 3:
            print("Neighbours:", ' '.join(sorted(router_neighbors.keys())))
            to_edit = input("Enter which