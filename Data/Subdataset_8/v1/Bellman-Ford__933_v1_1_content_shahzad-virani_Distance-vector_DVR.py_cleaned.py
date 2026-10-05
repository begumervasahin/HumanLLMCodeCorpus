import threading
import time
import math
from socket import socket, AF_INET, SOCK_DGRAM
SUSPEND_AFTER_TIMEOUT = 3.0
class Path:
    def __init__(self, distance, next_hop):
        self.distance = distance
        self.next_hop = next_hop
    def equals(self, path2):
        return self.distance == path2.distance and self.next_hop == path2.next_hop
class Neighbour:
    def __init__(self, link_cost, port, timeout):
        self.link_cost = link_cost
        self.port = port
        self.timeout = timeout
        self.paths = {}
r_ID = str()
r_port = int()
r_fileName = str()
r_neighbours = {}
r_routes = {}
lock = threading.Lock()
def create_pkt(dest_id, send_link_cost):
    distance_vector = str(r_ID)
    if send_link_cost:
        distance_vector += ' ' + str(r_neighbours[dest_id].link_cost)
    distance_vector += '\n'
    for id, path in r_routes.items():
        if path.next_hop == dest_id:
            distance_vector += str(id) + " " + str(math.inf) + '\n'
        else:
            distance_vector += str(id) + " " + str(path.distance) + '\n'
    return bytes(distance_vector, 'utf-8')
def sendDV(send_link_cost):
    send_socket = socket(AF_INET, SOCK_DGRAM)
    lock.acquire()
    for id, neighbour in r_neighbours.items():
        send_socket.sendto(create_pkt(id, send_link_cost), ('localhost', neighbour.port))
    lock.release()
    send_socket.close()
def printTable():
    string = '\t'
    for id in sorted(r_routes.keys()):
        string += '\t' + id
    print(string)
    string = r_ID + '\t'
    for id in sorted(r_routes.keys()):
        string += '\t' + str("%.1f" % r_routes[id].distance)
    print(string)
    for id in sorted(r_neighbours.keys()):
        string = id+'\t'+str(r_neighbours[id].link_cost)
        for key2 in sorted(r_neighbours[id].paths.keys()):
            string += '\t' + str("%.1f" % r_neighbours[id].paths[key2].distance)
        print(string)
    print('')
def timeOutCheck():
    while True:
        time.sleep(1)
        for id, neighbour in r_neighbours.items():
            s = socket(AF_INET, SOCK_DGRAM)
            try:
                s.bind(('localhost', neighbour.port))
                s.close()
                if r_neighbours[id].link_cost != math.inf:
                    lock.acquire()
                    r_routes[id].distance = math.inf
                    neighbour.link_cost = math.inf
                    neighbour.timeout = time.time()
                    for key2, item2 in r_routes.items():
                        if item2.next_hop == id:
                            item2.distance = math.inf
                    lock.release()
                    sendDV(False)
                    threading.Timer(SUSPEND_AFTER_TIMEOUT, target=bellManFord).start()
            except:
                pass
def listen():
    listen_socket = socket(AF_INET, SOCK_DGRAM)
    listen_socket.bind(('localhost', r_port))
    while True:
        message, socketAddress = listen_socket.recvfrom(2048)
        lines = str(message)[2:len(str(message))-1].split('\\n')
        firstLine = lines[0].split()
        source = firstLine[0]
        r_neighbours[source].timeout = -1.0
        if len(firstLine) > 1:
            r_neighbours[source].link_cost = float(firstLine[1])
            r_neighbours[source].timeout = -1
        lock.acquire()
        for i in range(1, len(lines)):
            if lines[i] == '':
                continue
            tokens = lines[i].split()
            newPath = Path(float(tokens[1]),'direct')
            if tokens[0] not in r_neighbours[source].paths:
                newNode(tokens[0])
            if not r_neighbours[source].paths[tokens[0]].equals(newPath):
                r_neighbours[source].paths[tokens[0]] = newPath
        threading.Thread(target=bellManFord).start()
        lock.release()
def newNode(name):
    global r_neighbours
    p = Path(math.inf, 'direct')
    r_routes[name] = p
    for id, neighbour in r_neighbours.items():
        neighbour.paths[name] = p
def bellManFord():
    global r_routes
    isChanged = False
    lock.acquire()
    for id, route in r_routes.items():
        m_list = []
        if id == r_ID:
            continue
        if id in r_neighbours:
            if time.time() > r_neighbours[id].timeout and time.time() < r_neighbours[id].timeout + SUSPEND_AFTER_TIMEOUT:
                r_routes[id] = Path(math.inf, 'direct')
                continue
            else:
                m_list.append(Path(r_neighbours[id].link_cost, 'direct'))
        for id2, neighbour in r_neighbours.items():
            p = Path(r_neighbours[id2].link_cost + neighbour.paths[id].distance, id2)
            m_list.append(p)
        m_list.append(p)
        m = min(m_list, key=lambda x: x.distance)
        if not r_routes[id].equals(Path(m.distance, m.next_hop)):
            r_routes[id] = Path(m.distance, m.next_hop)
            isChanged = True
    lock.release()
    if isChanged:
        sendDV(False)
def menu():
    option = 0
    while True:
        print('\n****I AM ROUTER ' + r_ID + '****\n')
        option = int(input('1: Display Costs.\n2: Display distance vector table.\n3: Edit link costs\n4: Quit\nYour choice: '))
        if option == 1:
            print('Destination\tNext Hop\tDistance')
            for id, route in sorted(r_routes.items()):
                if id != r_ID:
                    print('     ' + id + '\t\t' + route.next_hop + '\t\t' + str("%.1f" % route.distance))
        elif option == 2:
            printTable()
        elif option == 3:
            string = 'Neighbours:'
            for id in sorted(r_neighbours.keys()):
                string += ' ' + id
            print(string)
            toEdit = input('Enter which link to edit: ')
            newDistance = float(input('Enter new distance for ' + toEdit + ': '))
            r_neighbours[toEdit].link_cost = newDistance
            sendSocket = socket(AF_INET, SOCK_DGRAM)
            lock.acquire()
            sendSocket.sendto(create_pkt(toEdit, True), ('localhost', r_neighbours[toEdit].port))
            lock.release()
            sendSocket.close()
            threading.Thread(target=bellManFord).start()
        elif option == 4:
            os._exit(-1)
if __name__ == '__main__':
    try:
        r_ID = sys.argv[1]
        r_port = int(sys.argv[2])
        r_fileName =