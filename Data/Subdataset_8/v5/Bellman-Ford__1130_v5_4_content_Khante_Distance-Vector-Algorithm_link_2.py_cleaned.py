import queue
import threading
class Link:
    def __init__(self, node_1, node_1_intf, node_2, node_2_intf):
        self.node_1 = node_1
        self.node_1_intf = node_1_intf
        self.node_2 = node_2
        self.node_2_intf = node_2_intf
        print(f'Created link: {self}')
    def __str__(self):
        return f'Link {self.node_1}-{self.node_1_intf} - {self.node_2}-{self.node_2_intf}'
    def transmit_packet(self):
        src_node, src_intf, dest_node, dest_intf = self.node_1, self.node_1_intf, self.node_2, self.node_2_intf
        src_intf_obj = src_node.intf_L[src_intf]
        dest_intf_obj = dest_node.intf_L[dest_intf]
        packet = src_intf_obj.get('out')
        if packet is None:
            return
        try:
            dest_intf_obj.put(packet, 'in')
            print(f'{self}: {src_node}-{src_intf} -> {dest_node}-{dest_intf}: transmitting packet "{packet}"')
        except queue.Full:
            print(f'{self}: {src_node}-{src_intf} -> {dest_node}-{dest_intf}: packet lost')
class LinkLayer:
    def __init__(self):
        self.links = []
        self.stop = False
    def __str__(self):
        return 'Link Layer'
    def add_link(self, link):
        self.links.append(link)
    def transfer_packets(self):
        for link in self.links:
            link.transmit_packet()
    def run(self):
        print(f'{threading.currentThread().getName()}: Link layer started')
        while not self.stop:
            self.transfer_packets()
        print(f'{threading.currentThread().getName()}: Link layer stopped')
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
    intf1['out'] = 'packet2'
    link_layer.stop = True
    link_layer_thread.join()