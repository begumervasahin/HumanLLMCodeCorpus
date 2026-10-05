import sys
import socket
import select
from collections import namedtuple
import thread
import time
time_since_last_message = time.time()
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
next_arg = 3
number_neighbors = (len(sys.argv[3:]))/3
start = time.time()
source = (my_ip, my_port)
nodeActive = True
if(len(sys.argv[3:])%3 != 0):
    print "incorrect usage, neighbors should be listed:ip address, port, weight"
    exit()
while(next_arg/3 <= number_neighbors):
    neighbor_ip = sys.argv[next_arg]
    neighbor_port = int(sys.argv[next_arg + 1])
    neighbor_weight = int(sys.argv[next_arg + 2])
    neighbor = (neighbor_ip, neighbor_port)
    dv[neighbor] = int(neighbor_weight)
    neighbor_distance[neighbor] = int(neighbor_weight)
    predecessor[neighbor] = neighbor
    first_predecessor[neighbor] = neighbor
    neighbors[neighbor] = start
    next_arg += 3
original_distances = neighbor_distance
def ROUTE_UPDATE():
    for neighbor in neighbors:
        msg = None
        if neighbor_distance.has_key(neighbor):
            msg = "ROUTE_UPDATE" + " " + my_ip + " " + str(my_port) + " " + str(neighbor_distance[neighbor]) + " "
        for v in dv:
            if msg is None:
                msg = "ROUTE_UPDATE "
            msg += str(v[0]) + " " + str(v[1]) + " " + str(dv[v]) + " "
        if msg is not None:
            msg += "EOT"
            sending_socket.sendto(msg, (neighbor[0], neighbor[1]))
            time_since_last_message = time.time()
def LINK_DOWN(node):
    print "SENDING LINKDOWN"
    msg = "LINKDOWN" + " " + source[0] + " " + str(source[1]) + " "
    sending_socket.sendto(msg, (node[0], node[1]))
def LINK_UP(node):
    print "SENDING LINKUP"
    msg = "LINKUP" + " " + source[0] + " " + str(source[1]) + " "
    sending_socket.sendto(msg, (node[0], node[1]))
def SHOW_RT():
    now = time.strftime("%H:%M:%S", time.localtime(time.time()))
    print str(now) + "\tDistance vector list is: "
    for node in dv:
        print "Destination=" + node[0] + ":" + str(node[1]) + "\tCost=" + str(dv[node]) +"\t\tLink:"+ str(predecessor[node])
def LINK_DESTROYED(broken_node, target_node):
    print "LINK DESTROYED"
    msg = "LINK_DESTROYED" + " " + source[0] + " " + str(source[1]) + " " + broken_node[0] + " " + str(broken_node[1]) + " "
    sending_socket.sendto(msg, (target_node[0], target_node[1]))
def run(self, delay):
    time_since_last_message = time.time()
    while nodeActive:
        now = time.time()
        nodes_to_remove = []
        for neighbor in neighbors:
            if(now - neighbors[neighbor] > timeout * 2):
                print "REMOVING DEACTIVATED NEIGHBOR"
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
        if (now - time_since_last_message > timeout):
            time_since_last_message = time.time()
            ROUTE_UPDATE()
        time.sleep(1)
thread.start_new_thread( run, ("thread1", 2, ) )
sending_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
receiving_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
receiving_socket.bind((my_ip, my_port))
input = [receiving_socket, sys.stdin]
output = [sys.stdin]
time.sleep(1)
while nodeActive:
    try:
        inputready,outputready,exceptready = select.select(input,[],[])
        for s in inputready:
            if s == sys.stdin:
                command = sys.stdin.readline()
                command = command.split()
                if command[0] == "LINKDOWN" and len(command) > 2:
                    command_ip = command[1]
                    command_port = int(command[2])
                    node = (command_ip, command_port)
                    if node in neighbors:
                        dv[node] = float("inf")
                        linked_down_nodes[node] = dv[node]
                    else:
                        print "Node is not a neighbor, can't Linkdown"
                    for node in linked_down_nodes:
                        if node in neighbors:
                            del neighbors[node]
                            LINK_DOWN(node)
                            ROUTE_UPDATE()
                elif command[0] == "LINKUP" and len(command) > 2:
                    node = (command_ip, command_port)
                    if node not in neighbors:
                        neighbors[node] = time.time()
                        if node in dv:
                            dv[node] = int(neighbor_distance[node])
                            LINK_UP(node)
                elif command[0] == "CLOSE":
                    print "Node shutting down"
                    nodeActive = False
                elif command[0] == "SHOW_RT":
                    SHOW_RT()
                else:
                    print command[0] + "Command not recognized"
            else:
                data = s.recv(1024)
                data = data.split()
                if data[0] == "ROUTE_UPDATE":
                    sender_ip = data[1]
                    sender_port = int(data[2])
                    if data[3] is float("inf"):
                        sender_weight = data[3]
                    else:
                        sender_weight = int(data[3])
                    sender = (sender_ip, sender_port)
                    if(sender not in deactivated_links):
                        if(neighbors.has_key(sender)):
                            neighbors[sender] = time.time()
                            if neighbor_distance.has_key(sender):
                                if(neighbor_distance[sender] > sender_weight):
                                    neighbor_distance[sender] = sender_weight
                                    dv[sender] = sender_weight
                            else:
                                print "don't have neighbor in neighbor distance for some reason"
                        else:
                            neighbors[sender] = time.time()
                            neighbor_distance[sender] = sender_weight
                            dv[sender] = sender_weight
                            predecessor[sender] = sender
                            first_predecessor = sender
                        end_of_message = False
                        counter = 4
                        new_dv = {}
                        while(end_of_message is False):
                            if data[counter+2] == str("inf"):
                                weight = float("inf")
                            else:
                                weight = int(data[counter+2])
                            new_dv[data[counter], int(data[counter+1])] = weight
                            counter += 3
                            if(data[counter] == "EOT"):
                                end_of_message = True
                        for node in new_dv:
                            if node in predecessor:
                                if sender == predecessor[node] and node in dv:
                                    if new_dv[node] > dv[node]:
                                        if node in neighbor_distance:
                                            my_distance_to_node = neighbor_distance[node]
                            if str(node[0]) != str(my_ip) or str(node[1]) != str(my_port):
                                if dv.has_key(node):
                                    if (neighbor_distance[sender] == float('inf')):
                                        distance_to_neighbor = neighbor_distance[sender]
                                    else:
                                        distance_to_neighbor = int(neighbor_distance[sender])
                                    if (new_dv[node] == float('inf')):
                                        if sender == predecessor[node]:
                                            if node in neighbor_distance:
                                                my_distance_to_node = neighbor_distance[node]
                                        neighbors_distance_to_node = new_dv[node]
                                    else:
                                        neighbors_distance_to_node = int(new_dv[node])
                                    if (dv[node] == float('inf')):
                                        my_distance_to_node = dv[node]
                                    else:
                                        my_distance_to_node = int(dv[node])
                                    if distance_to_neighbor + neighbors_distance_to_node < my_distance_to_node:
                                        dv[node] = distance_to_neighbor + neighbors_distance_to_node
                                        predecessor[node] = (sender_ip, sender_port)
                                else:
                                    dv[node] = int(new_dv[node]) + int(data[3])
                                    predecessor[node] = (sender_ip, sender_port)
                                    first_predecessor[node] = (sender_ip, sender_port)
                elif data[0] == "LINKUP":
                    print "LINKUP"
                    sender = (data[1], int(data[2]))
                    if(dv[sender] == float("inf")):
                        if(deactivated_links[sender] is not None):
                            dv[sender] = int(deactivated_links[sender])
                            del deactivated_links[sender]
                            neighbors[sender] = time.time()
                            ROUTE_UPDATE()
                            print "LINK RESTORED"
                elif data[0] == "LINKDOWN":
                    sender = (data[1], int(data[2]))
                    deactivated_links[sender] = int(dv[sender])
                    dv[sender] = float("inf");
                    del neighbors[sender]
                    for v in dv:
                        LINK_DESTROYED(sender, v)
                    ROUTE_UPDATE()
                    print "LINK DEACTIVATED"
                elif data[0] == "LINK_DESTROYED":
                    print data
                    sender = (data[1], int(data[2]))
                    target = (data[3], int(data[4]))
                    broken_links[sender] = target
                    broken_links[target] = sender
                    if target in predecessor:
                        if target in dv:
                            if predecessor[target] == sender:
                                if target in original_distances:
                                    dv[target] = original_distances[target]
                                else:
                                    dv[target] = float("inf")
                elif data[0] is not None:
                    print "Unrecognized message received: "
                    print data
                else:
                    s.close()
                    input.remove(s)
    except socket.error, e:
        if e.errno != errno.EAGAIN:
            raise e
        print "blocking with", len(buf), "remaining"
        select.select([], [input], [])
        print "unblocked"