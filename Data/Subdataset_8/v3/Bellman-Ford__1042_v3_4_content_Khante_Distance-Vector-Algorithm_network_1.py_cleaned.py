import threading
import queue
from collections import defaultdict, OrderedDict
class Interface:
    def __init__(self, maxsize=0):
        self.in_queue = queue.Queue(maxsize)
        self.out_queue = queue.Queue(maxsize)
    def get(self, direction):
        try:
            return self.in_queue.get(False) if direction == 'in' else self.out_queue.get(False)
        except queue.Empty:
            return None
    def put(self, pkt, direction, block=False):
        if direction == 'out':
            self.out_queue.put(pkt, block)
        else:
            self.in_queue.put(pkt, block)
class NetworkPacket:
    DST_LENGTH = 5
    PROTOCOL_LENGTH = 1
    def __init__(self, destination, protocol, data):
        self.destination = destination
        self.data = data
        self.protocol = protocol
    def __str__(self):
        return self.to_byte_S()
    def to_byte_S(self):
        byte_S = str(self.destination).zfill(self.DST_LENGTH)
        byte_S += '1' if self.protocol == 'data' else '2'
        byte_S += self.data
        return byte_S
    @classmethod
    def from_byte_S(cls, byte_S):
        destination = byte_S[:cls.DST_LENGTH].strip('0')
        protocol = 'data' if byte_S[cls.DST_LENGTH:cls.DST_LENGTH + cls.PROTOCOL_LENGTH] == '1' else 'control'
        data = byte_S[cls.DST_LENGTH + cls.PROTOCOL_LENGTH:]
        return cls(destination, protocol, data)
class Host:
    def __init__(self, address):
        self.address = address
        self.interfaces = [Interface()]
        self.stop = False
    def __str__(self):
        return self.address
    def send(self, destination, data):
        packet = NetworkPacket(destination, 'data', data)
        print('%s: SENDING PACKET "%s"' % (self, packet))
        self.interfaces[0].put(packet.to_byte_S(), 'out')
    def receive(self):
        packet = self.interfaces[0].get('in')
        if packet is not None:
            print('%s: RECEIVED PACKET "%s"' % (self, packet))
    def run(self):
        print(threading.currentThread().getName() + ': Starting')
        while True:
            self.receive()
            if self.stop:
                print(threading.currentThread().getName() + ': Ending')
                return
class Router:
    def __init__(self, name, neighbors, max_queue_size):
        self.stop = False
        self.name = name
        self.interfaces = [Interface(max_queue_size) for _ in range(len(neighbors))]
        self.neighbors = neighbors
        self.routing_table = neighbors.copy()
        self.total_routing_table = defaultdict(dict)
        for neighbor_name, neighbor_info in self.neighbors.items():
            for interface, cost in neighbor_info.items():
                self.total_routing_table[name][neighbor_name] = [cost]
        print('%s: Initialized routing table' % self)
        self.print_routing_table()
    def __str__(self):
        return self.name
    def process_queues(self):
        for i, interface in enumerate(self.interfaces):
            packet = interface.get('in')
            if packet is not None:
                packet_obj = NetworkPacket.from_byte_S(packet)
                if packet_obj.protocol == 'data':
                    self.forward_packet(packet_obj, i)
                elif packet_obj.protocol == 'control':
                    self.update_routing_table(packet_obj, i)
                else:
                    raise ValueError('%s: Unknown packet type in packet %s' % (self, packet_obj))
    def forward_packet(self, packet_obj, interface_index):
        try:
            route = self.routing_table.get(str(packet_obj.destination))
            destination_interface_index = next(iter(route))
            self.interfaces[destination_interface_index].put(packet_obj.to_byte_S(), 'out', True)
            print('%s: forwarding packet "%s" from interface %d to %d' % (self, packet_obj, interface_index, destination_interface_index))
        except queue.Full:
            print('%s: packet "%s" lost on interface %d' % (self, packet_obj, interface_index))
    def send_routing_table(self, interface_index):
        print('sending_routing_table')
        contents = f"{self.name}->"
        for node, neighbors in self.routing_table.items():
            for link, cost in neighbors.items():
                contents += f"{node}_{link}_{cost} "
        packet = NetworkPacket(0, 'control', contents)
        self.interfaces[interface_index].put(packet.to_byte_S(), 'out', True)
    def update_routing_table(self, packet_obj, interface_index):
        update_flag = 0
        source_node, route_data = packet_obj.data.split("->")
        for route in route_data.split():
            if route:
                current_node, _, node_cost = route.split("_")
                node_cost = int(node_cost)
                self.total_routing_table[source_node][current_node] = [node_cost]
                if current_node == self.name:
                    neighbor_interface_index = next(iter(self.neighbors[source_node]))
                    self.routing_table[current_node] = {neighbor_interface_index: 0}
                    self.total_routing_table[self.name][current_node] = [0]
                    continue
                else:
                    if current_node not in self.neighbors and current_node not in self.routing_table:
                        neighbor_cost = next(iter(self.neighbors[source_node].values()))
                        neighbor_interface_index = next(iter(self.neighbors[source_node].keys()))
                        self.routing_table[current_node] = {neighbor_interface_index: node_cost + neighbor_cost}
                        self.total_routing_table[self.name][current_node] = [node_cost + neighbor_cost]
                        update_flag = 1
                    elif current_node not in self.neighbors and current_node in self.routing_table:
                        neighbor_cost = next(iter(self.neighbors[source_node].values()))
                        neighbor_interface_index = next(iter(self.neighbors[source_node].keys()))
                        current_node_cost = next(iter(self.routing_table[current_node].values()))
                        if current_node_cost > neighbor_cost + node_cost:
                            self.routing_table[current_node] = {neighbor_interface_index: node_cost + neighbor_cost}
                            self.total_routing_table[self.name][current_node] = [node_cost + neighbor_cost]
                            update_flag = 1
        if update_flag == 1:
            for neighbor_name, neighbor_info in self.neighbors.items():
                for interface_index, cost in neighbor_info.items():
                    if 'R' in neighbor_name:
                        self.send_routing_table(interface_index)
    def print_routing_table(self):
        print(f'Routing table for {self}:')
        sorted_routing_table = OrderedDict(sorted(self.total_routing_table.items()))
        interfaces = sorted(set(interface for node in sorted_routing_table.values() for interface in node))
        for interface in interfaces:
            print(interface, end='\t')
            for node, neighbors in sorted_routing_table.items():
                for link, cost in neighbors.items():
                    if link == interface:
                        print(cost[0], end='\t')
        print("\n")
    def run(self):
        print(threading.currentThread().getName() + ': Starting')
        while True:
            self.process_queues()
            if self.stop:
                print(threading.currentThread().getName() + ': Ending')
                return
topology = {
    'H1': {'R1': {0: 1}},
    'R1': {'R2': {1: 1}},
    'R2': {'H2': {0: 1}},
}
router_configs = {
    'R1': {'R2': {1: 1}},
    'R2': {'R1': {0: 1}},
}
devices = []
for name, config in router_configs.items():
    devices.append(Router(name, config, max_queue_size=100))
devices.extend([Host('H1'), Host('H2')])
for device in devices:
    thread = threading.Thread(target=device.run)
    thread.start()
devices[0].send('H2', 'Test message from H1 to H2')