import sys
import socket
import select
import time
from collections import defaultdict
class Node:
    def __init__(self, ip, port, weight=float('inf')):
        self.ip = ip
        self.port = port
        self.weight = weight
class DistanceVector:
    def __init__(self):
        self.dv = defaultdict(lambda: float('inf'))
        self.predecessor = {}
        self.neighbors = {}
        self.neighbor_distance = {}
        self.original_distances = {}
        self.first_predecessor = {}
        self.broken_links = {}
        self.linked_down_nodes = {}
        self.deactivated_links = {}
def main():
    if len(sys.argv) < 4 or len(sys.argv[3:]) % 3 != 0:
        print("Usage: python script.py <port> <timeout> <neighbor1_ip> <neighbor1_port> <neighbor1_weight> ...")
        return
    port = int(sys.argv[1])
    timeout = int(sys.argv[2])
    node_active = True
    distance_vector = DistanceVector()
    def send_route_update():
        for neighbor, weight in distance_vector.neighbor_distance.items():
            if weight != float('inf'):
                msg = f"ROUTE_UPDATE {my_ip} {my_port} {weight} "
                for dest, w in distance_vector.dv.items():
                    msg += f"{dest.ip} {dest.port} {w} "
                msg += "EOT"
                sending_socket.sendto(msg, (neighbor.ip, neighbor.port))
    def link_down(node):
        msg = f"LINKDOWN {my_ip} {my_port} "
        sending_socket.sendto(msg, (node.ip, node.port))
    def link_up(node):
        msg = f"LINKUP {my_ip} {my_port} "
        sending_socket.sendto(msg, (node.ip, node.port))
    def show_rt():
        now = time.strftime("%H:%M:%S", time.localtime(time.time()))
        print(f"{now}\tDistance vector list is:")
        for dest, w in distance_vector.dv.items():
            print(f"Destination={dest.ip}:{dest.port}\tCost={w}\t\tLink:{distance_vector.predecessor[dest]}")
    def link_destroyed(broken_node, target_node):
        msg = f"LINK_DESTROYED {my_ip} {my_port} {broken_node.ip} {broken_node.port} "
        sending_socket.sendto(msg, (target_node.ip, target_node.port))
    def run(delay):
        time_since_last_message = time.time()
        while node_active:
            now = time.time()
            nodes_to_remove = []
            for neighbor, last_seen in distance_vector.neighbors.items():
                if now - last_seen > timeout * 2:
                    distance_vector.deactivated_links[neighbor] = distance_vector.neighbor_distance[neighbor]
                    nodes_to_remove.append(neighbor)
            for inactive_node in nodes_to_remove:
                if inactive_node in distance_vector.neighbors:
                    distance_vector.dv[inactive_node] = float("inf")
                    del distance_vector.neighbors[inactive_node]
                for key, value in distance_vector.predecessor.items():
                    if value == inactive_node:
                        if key in distance_vector.neighbors:
                            distance_vector.dv[key] = distance_vector.neighbor_distance[key]
                        else:
                            distance_vector.dv[inactive_node] = float("inf")
                            distance_vector.dv[key] = float("inf")
                            distance_vector.predecessor[key] = "no link exists"
                send_route_update()
            if now - time_since_last_message > timeout:
                time_since_last_message = time.time()
                send_route_update()
            time.sleep(1)
    def process_command(command):
        command = command.split()
        if command[0] == "LINKDOWN" and len(command) > 2:
            command_ip = command[1]
            command_port = int(command[2])
            node = Node(command_ip, command_port)
            if node in distance_vector.neighbors:
                distance_vector.dv[node] = float("inf")
                distance_vector.linked_down_nodes[node] = distance_vector.dv[node]
            else:
                print("Node is not a neighbor, can't Linkdown")
            for node in distance_vector.linked_down_nodes:
                if node in distance_vector.neighbors:
                    del distance_vector.neighbors[node]
                    link_down(node)
                    send_route_update()
        elif command[0] == "LINKUP" and len(command) > 2:
            node = Node(command_ip, command_port)
            if node not in distance_vector.neighbors:
                distance_vector.neighbors[node] = time.time()
                if node in distance_vector.dv:
                    distance_vector.dv[node] = int(distance_vector.neighbor_distance[node])
                    link_up(node)
        elif command[0] == "CLOSE":
            print("Node shutting down")
            node_active = False
        elif command[0] == "SHOW_RT":
            show_rt()
        else:
            print(command[0] + "Command not recognized")
    thread.start_new_thread(run, (2,))
    sending_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    receiving_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    receiving_socket.bind((my_ip, my_port))
    input = [receiving_socket, sys.stdin]
    while node_active:
        try:
            inputready, _, _ = select.select(input, [], [])
            for s in inputready:
                if s == sys.stdin:
                    command = sys.stdin.readline()
                    process_command(command)
                else:
                    data, _ = s.recvfrom(1024)
                    data = data.split()
                    if data[0] == "ROUTE_UPDATE":
                        sender_ip = data[1]
                        sender_port = int(data[2])
                        if data[3] == "inf":
                            sender_weight = float("inf")
                        else:
                            sender_weight = int(data[3])
                        sender = Node(sender_ip, sender_port)
                        if sender not in distance_vector.deactivated_links:
                            if sender in distance_vector.neighbors:
                                distance_vector.neighbors[sender] = time.time()
                                if sender in distance_vector.neighbor_distance:
                                    if distance_vector.neighbor_distance[sender] > sender_weight:
                                        distance_vector.neighbor_distance[sender] = sender_weight
                                        distance_vector.dv[sender] = sender_weight
                                else:
                                    print("don't have neighbor in neighbor distance for some reason")
                            else:
                                distance_vector.neighbors[sender] = time.time()
                                distance_vector.neighbor_distance[sender] = sender_weight
                                distance_vector.dv[sender] = sender_weight
                                distance_vector.predecessor[sender] = sender
                                distance_vector.first_predecessor = sender
                            end_of_message = False
                            counter = 4
                            new_dv = {}
                            while not end_of_message:
                                if data[counter+2] == "inf":
                                    weight = float("inf")
                                else:
                                    weight = int(data[counter+2])
                                new_dv[Node(data[counter], int(data[counter+1]))] = weight
                                counter += 3
