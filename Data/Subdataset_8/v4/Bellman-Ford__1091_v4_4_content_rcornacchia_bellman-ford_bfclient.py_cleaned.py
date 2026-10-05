import sys
import socket
import select
import thread
import time
from collections import defaultdict
Node = namedtuple('Node', ['ip', 'port'])
my_ip = socket.gethostbyname(socket.gethostname())
my_port = int(sys.argv[1])
timeout = int(sys.argv[2])
dv = {}
predecessor = {}
neighbors = {}
neighbor_distance = {}
original_distances = {}
first_predecessor = {}
broken_links = {}
linked_down_nodes = {}
deactivated_links = {}
time_since_last_message = time.time()
if len(sys.argv[3:]) % 3 != 0:
    print("Incorrect usage. Neighbors should be listed as: ip address, port, weight")
    exit()
next_arg = 3
while next_arg / 3 <= len(sys.argv[3:]) / 3:
    neighbor_ip = sys.argv[next_arg]
    neighbor_port = int(sys.argv[next_arg + 1])
    neighbor_weight = int(sys.argv[next_arg + 2])
    neighbor = Node(neighbor_ip, neighbor_port)
    dv[neighbor] = int(neighbor_weight)
    neighbor_distance[neighbor] = int(neighbor_weight)
    predecessor[neighbor] = neighbor
    first_predecessor[neighbor] = neighbor
    neighbors[neighbor] = time.time()
    next_arg += 3
original_distances = neighbor_distance
def ROUTE_UPDATE():
    for neighbor in neighbors:
        msg = None
        if neighbor_distance.get(neighbor):
            msg = f"ROUTE_UPDATE {my_ip} {my_port} {neighbor_distance[neighbor]} "
            for v in dv:
                msg += f"{v.ip} {v.port} {dv[v]} "
            msg += "EOT"
            sending_socket.sendto(msg, (neighbor.ip, neighbor.port))
            time_since_last_message = time.time()
def LINK_DOWN(node):
    print("Sending LINKDOWN")
    msg = f"LINKDOWN {my_ip} {my_port} "
    sending_socket.sendto(msg, (node.ip, node.port))
def LINK_UP(node):
    print("Sending LINKUP")
    msg = f"LINKUP {my_ip} {my_port} "
    sending_socket.sendto(msg, (node.ip, node.port))
def SHOW_RT():
    now = time.strftime("%H:%M:%S", time.localtime(time.time()))
    print(f"{now}\tDistance vector list is: ")
    for node in dv:
        print(f"Destination={node.ip}:{node.port}\tCost={dv[node]}\t\tLink:{predecessor[node]}")
def LINK_DESTROYED(broken_node, target_node):
    print("LINK DESTROYED")
    msg = f"LINK_DESTROYED {my_ip} {my_port} {broken_node.ip} {broken_node.port} "
    sending_socket.sendto(msg, (target_node.ip, target_node.port))
def run(delay):
    time_since_last_message = time.time()
    while nodeActive:
        now = time.time()
        nodes_to_remove = []
        for neighbor in neighbors:
            if now - neighbors[neighbor] > timeout * 2:
                print("Removing deactivated neighbor")
                deactivated_links[neighbor] = neighbor_distance[neighbor]
                nodes_to_remove.append(neighbor)
        for inactive_node in nodes_to_remove:
            if inactive_node in neighbors:
                dv[inactive_node] == float("inf")
                del neighbors[inactive_node]
            for key in predecessor:
                if predecessor[key] == inactive_node:
                    if key in neighbors:
                        dv[key] = neighbor_distance[key]
                    else:
                        dv[inactive_node] = float("inf")
                        dv[key] = float("inf")
                        predecessor[key] = "no link exists"
            ROUTE_UPDATE()
        if now - time_since_last_message > timeout:
            time_since_last_message = time.time()
            ROUTE_UPDATE()
        time.sleep(1)
thread.start_new_thread(run, ("thread1", 2,))
sending_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
receiving_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
receiving_socket.bind((my_ip, my_port))
input = [receiving_socket, sys.stdin]
output = [sys.stdin]
time.sleep(1)
while nodeActive:
    try:
        inputready, outputready, exceptready = select.select(input, [], [])
        for s in inputready:
            if s == sys.stdin:
                command = sys.stdin.readline()
                command = command.split()
                if command[0] == "LINKDOWN" and len(command) > 2:
                    command_ip = command[1]
                    command_port = int(command[2])
                    node = Node(command_ip, command_port)
                    if node in neighbors:
                        dv[node] = float("inf")
                        linked_down_nodes[node] = dv[node]
                    else:
                        print("Node is not a neighbor, can't Linkdown")
                    for node in linked_down_nodes:
                        if node in neighbors:
                            del neighbors[node]
                            LINK_DOWN(node)
                            ROUTE_UPDATE()
                elif command[0] == "LINKUP" and len(command) > 2:
                    node = Node(command_ip, command_port)
                    if node not in neighbors:
                        neighbors[node] = time.time()
                        if node in dv:
                            dv[node] = int(neighbor_distance[node])
                            LINK_UP(node)
                elif command[0] == "CLOSE":
                    print("Node shutting down")
                    nodeActive = False
                elif command[0] == "SHOW_RT":
                    SHOW_RT()
                else:
                    print(f"{command[0]} Command not recognized")
            else:
                data = s.recv(1024)
                data = data.split()
                if data[0] == "ROUTE_UPDATE":
                    sender_ip = data[1]
                    sender_port = int(data[2])
                    if data[3] == float("inf"):
                        sender_weight = data[3]
                    else:
                        sender_weight = int(data[3])
                    sender = Node(sender_ip, sender_port)
                    if sender not in deactivated_links:
                        if sender in neighbors:
                            neighbors[sender] = time.time()
                            if sender in neighbor_distance:
                                if neighbor_distance[sender] > sender_weight:
                                    neighbor_distance[sender] = sender_weight
                                    dv[sender] = sender_weight
                            else:
                                print("Don't have neighbor in neighbor distance for some reason")
                        else:
                            neighbors[sender] = time.time()
                            neighbor_distance[sender] = sender_weight
                            dv[sender] = sender_weight
                            predecessor[sender] = sender
                            first_predecessor = sender
                        end_of_message = False
                        counter = 4
                        new_dv = {}
                        while not end_of_message:
                            if data[counter + 2] == str("inf"):
                                weight = float("inf")
                            else:
                                weight = int(data[counter + 2])
                            new_dv[data[counter], int(data[counter + 1])] = weight
                            counter += 3
                            if data[counter] == "EOT":
                                end_of_message = True