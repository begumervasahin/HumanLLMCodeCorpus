import queue
import threading
from time import sleep
class Host:
    def __init__(self, name):
        self.name = name
        self.stop = False
        self.out_intf_L = {}
    def __str__(self):
        return self.name
    def run(self):
        print(f'{self}: Host is running')
        while not self.stop:
            sleep(0.5)
        print(f'{self}: Host stopped')
    def udt_send(self, dest, msg):
        if dest in self.out_intf_L:
            self.out_intf_L[dest].put(msg)
        else:
            print(f'{self}: Destination {dest} not found')
class Router:
    def __init__(self, name, cost_D, max_queue_size):
        self.name = name
        self.stop = False
        self.cost_D = cost_D
        self.max_queue_size = max_queue_size
        self.out_intf_L = {}
        self.routing_table = {}
    def __str__(self):
        return self.name
    def run(self):
        print(f'{self}: Router is running')
        while not self.stop:
            sleep(0.5)
        print(f'{self}: Router stopped')
    def send_routes(self, update_interval):
        print(f'{self}: Sending routing updates every {update_interval} seconds')
        sleep(update_interval)
        print(f'{self}: Routing updates sent')
    def print_routes(self):
        print(f'{self}: Routing table:')
        for dest, cost in self.routing_table.items():
            print(f'Destination: {dest}, Cost: {cost}')
class Link:
    def __init__(self, node_1, node_1_intf, node_2, node_2_intf):
        self.node_1 = node_1
        self.node_1_intf = node_1_intf
        self.node_2 = node_2
        self.node_2_intf = node_2_intf
        print(f'Created link: {self}')
    def __str__(self):
        return f'Link {self.node_1}-{self.node_1_intf} - {self.node_2}-{self.node_2_intf}'
class LinkLayer:
    def __init__(self):
        self.links = []
        self.stop = False
    def __str__(self):
        return 'Link Layer'
    def add_link(self, link):
        self.links.append(link)
    def run(self):
        print(f'{self}: Link layer is running')
        while not self.stop:
            sleep(0.5)
        print(f'{self}: Link layer stopped')
if __name__ == '__main__':
    object_L = []
    host_1 = Host('H1')
    object_L.append(host_1)
    host_2 = Host('H2')
    object_L.append(host_2)
    cost_D = {'H1': {0: 1}, 'RB': {1: 1}}
    router_a = Router(name='RA', cost_D=cost_D, max_queue_size=0)
    object_L.append(router_a)
    cost_D = {'H2': {1: 3}, 'RA': {0: 1}}
    router_b = Router(name='RB', cost_D=cost_D, max_queue_size=0)
    object_L.append(router_b)
    link_layer = LinkLayer()
    object_L.append(link_layer)
    link_layer.add_link(Link(host_1, 0, router_a, 0))
    link_layer.add_link(Link(router_a, 1, router_b, 0))
    link_layer.add_link(Link(router_b, 1, host_2, 0))
    thread_L = []
    for obj in object_L:
        thread_L.append(threading.Thread(name=obj.__str__(), target=obj.run))
    for t in thread_L:
        t.start()
    router_a.send_routes(1)
    sleep(2)
    print("Converged routing tables")
    for obj in object_L:
        if str(type(obj)) == "<class '__main__.Router'>":
            obj.print_routes()
    host_1.udt_send('H2', 'MESSAGE_FROM_H1')
    host_2.udt_send('H1', 'reply for MESSAGE_FROM_H1')
    sleep(2)
    for o in object_L:
        o.stop = True
    for t in thread_L:
        t.join()
    print("All simulation threads joined")