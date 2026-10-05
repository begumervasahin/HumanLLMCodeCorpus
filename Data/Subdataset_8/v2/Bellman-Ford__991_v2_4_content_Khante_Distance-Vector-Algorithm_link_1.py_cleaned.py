import queue
import threading
import time
class Link:
    def __init__(self, node_1, node_1_intf, node_2, node_2_intf):
        self.node_1 = node_1
        self.node_1_intf = node_1_intf
        self.node_2 = node_2
        self.node_2_intf = node_2_intf
        print(f'Created link {self}')
    def __str__(self):
        return f'Link {self.node_1}-{self.node_1_intf} - {self.node_2}-{self.node_2_intf}'
    def tx_pkt(self):
        for node_a, node_a_intf, node_b, node_b_intf in [(self.node_1, self.node_1_intf, self.node_2, self.node_2_intf), (self.node_2, self.node_2_intf, self.node_1, self.node_1_intf)]:
            intf_a = node_a.intf_L[node_a_intf]
            intf_b = node_b.intf_L[node_b_intf]
            pkt_S = intf_a.get('out')
            if pkt_S is None:
                continue
            try:
                intf_b.put(pkt_S, 'in')
                print(f'{self}: transmitting packet "{pkt_S}" on {node_a} {node_a_intf} -> {node_b}, {node_b_intf}')
            except queue.Full:
                print(f'{self}: packet lost')
                pass
class LinkLayer:
    def __init__(self):
        self.link_L = []
        self.stop = False
    def __str__(self):
        return 'Network'
    def add_link(self, link):
        self.link_L.append(link)
    def transfer(self):
        for link in self.link_L:
            link.tx_pkt()
    def run(self):
        print(f'{threading.currentThread().getName()}: Starting')
        while True:
            self.transfer()
            if self.stop:
                print(f'{threading.currentThread().getName()}: Ending')
                return
if __name__ == '__main__':
    node1 = object()
    node2 = object()
    intf1 = {'out': 'packet1'}
    intf2 = queue.Queue(maxsize=1)
    node1.intf_L = {0: intf1}
    node2.intf_L = {0: intf2}
    link_layer = LinkLayer()
    link = Link(node1, 0, node2, 0)
    link_layer.add_link(link)
    link_layer_thread = threading.Thread(target=link_layer.run)
    link_layer_thread.start()
    time.sleep(1)
    intf1['out'] = 'packet2'
    time.sleep(2)
    link_layer.stop = True
    link_layer_thread.join()