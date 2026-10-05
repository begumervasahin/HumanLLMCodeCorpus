import sys
import socket
import select
import pickle
from time import time, sleep
import datetime
import copy
DEBUG = 1
DEBUG2 = DEBUG
BUFFER_SIZE = 4096
costs = {}
last_contact = {}
uplink = {}
dv = {}
me = (0, 0)
last_broadcast = time()
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.setblocking(0)
my_addr = socket.gethostbyname(socket.gethostname())
if my_addr[:3] == '127':
    my_addr = '127.0.0.1'
MAX_COST = float("inf")
def kill_link(client):
    sock.sendto('DOWN', client)
def add_neighbor_initial(client, weight):
    costs[client] = float(weight)
    last_contact[client] = time()
    uplink[client] = 1
    dv[me][client] = [client, float(weight)]
    dv[client] = {}
    dv[client][client] = [client, 0]
def add_neighbor_new(client, vector):
    dv[client] = vector
    dv[me][client] = [client, dv[client][me][1]]
    costs[client] = float(dv[client][me][1])
def broadcast():
    global last_broadcast
    if DEBUG:
        print(dv[me])
        print(uplink)
    for neighbor, vector in dv.items():
        if neighbor is not me:
            if DEBUG2:
                print(neighbor)
                print(uplink[neighbor])
            if uplink[neighbor] == 1:
                if DEBUG2:
                    print("broadcast: sending to client " + str(neighbor))
                dv_poisoned = copy.deepcopy(dv[me])
                for dest, path in dv[me].items():
                    if path[0] == neighbor and dest != neighbor:
                        dv_poisoned[dest][1] = MAX_COST
                if DEBUG:
                    print("poisoned message to neighbor %s : %s" % (neighbor, dv_poisoned))
                    print("actual dv[me] " + str(dv[me]))
                sock.sendto(pickle.dumps(dv_poisoned), neighbor)
    last_broadcast = time()
def showroute():
    print(str(datetime.datetime.now()) + ", Current Distance Vector is:")
    for dest, path in dv[me].items():
        if dest is not me:
            if DEBUG:
                print("dest = " + str(dest))
                print("path = " + str(path))
            print("Destination=%s:%d, Cost = %.1f, Link = (%s:%d)" % (dest[0], dest[1], float(path[1]), path[0][0], path[0][1]))
def update_dv():
    changed = 0
    for dest, cost in dv[me].items():
        path = cost[0]
        try:
            dv[me][dest][1] = dv[me][path][1] + dv[path][dest][1]
        except:
            dv[me][dest][1] = MAX_COST
    path = ("UNREACHABLE", 0)
    for dest, cost in dv[me].items():
        if dest is not me:
            if DEBUG:
                print("----updating distance to dest : " + str(dest))
                print("----old cost = " + str(cost))
            try:
                if DEBUG:
                    print("^^^^^^^^^^^^^^ TRYING INITIAL CLEANUP")
                    print("dest = " + str(dest))
                    print("cost[0] = " + str(dest))
                    print("dv[me][dest]" + str(dv[me][dest]))
                    print("dv[cost[0]] = " + str(dv[cost[0]]))
                    print("dv[cost[0]][me][1] = " + str(dv[cost[0]][me][1]))
                    print("dv[cost[0]][dest][1] = " +  str(dv[cost[0]][dest][1]))
                if dv[cost[0]][me][1] + dv[cost[0]][dest][1] > dv[me][dest][1]:
                    dv[me][dest] = [dest, dv[cost[0]][me][1] + dv[cost[0]][dest][1]]
            except:
                pass
        oldcost = dv[me][dest][1]
        min_cost = MAX_COST
        for neighbor, links in dv.items():
            if uplink[neighbor] and neighbor != me:
                if DEBUG:
                    print("-neighbor is not me, neighbor = " + str(neighbor))
                    print("-me: " + str(me))
                try:
                    neighbor_to_dest = dv[neighbor][dest][1]
                except:
                    neighbor_to_dest = MAX_COST
                if DEBUG:
                    print("-dv[me] = " + str(dv[me]))
                    print("-dv[me][neighbor] = " + str(dv[me][neighbor]))
                    print("-dv[me][neighbor][1] = " + str(dv[me][neighbor][1]))
                    print("-dv[neighbor][dest][1] = " + str(neighbor_to_dest))
                    print("-oldcost = " + str(oldcost))
                if neighbor != dest:
                    me_to_neighbor = dv[me][neighbor][1]
                else:
                    me_to_neighbor = costs[neighbor]
                if me_to_neighbor + neighbor_to_dest < min_cost:
                    if DEBUG:
                        print("-route discovered, dv[%s][%s] + dv[%s][%s] = %s" % (me, neighbor, neighbor, dest, dv[me][neighbor][1] + neighbor_to_dest))
                    min_cost = me_to_neighbor + neighbor_to_dest
                    path = neighbor
        if oldcost != min_cost:
            if DEBUG:
                print("====New route superior; CHANGE RECORDED")
                print("====oldcost = " + str(oldcost))
                print("====min_cost = " +str(min_cost))
                print("====destination = " + str(dest))
                print("====via path" + str(path))
            changed = 1
            dv[me][dest] = [path, min_cost]
        if DEBUG:
            print("====================================================")
    return changed
def linkdown(client_input):
    client = client_input
    if client[0] == 'localhost' or client[0][:3] == '127':
        client = (my_addr, client_input[1])
    uplink[client] = 0
    costs[client] = dv[me][client][1]
    dv[me][client][1] = MAX_COST
    try:
        dv[client][me][1] = MAX_COST
    except:
        if DEBUG:
            print("don't have the DV for " + str(client) + " yet.")
    if DEBUG2:
        print(dv[me])
    for dest, path in dv[me].items():
        if DEBUG:
            print("****killing intermediary... dest = " +