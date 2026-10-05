import queue
import threading
from collections import OrderedDict, defaultdict
class Interface:
    def __init__(self, maxsize=0):
        self.in_queue = queue.Queue(maxsize)
        self.out_queue = queue.Queue(maxsize)
    def get(self, in_or_out):
        try:
            if in_or_out == 'in':
                pkt_S = self.in_queue.get(False)
                return pkt_S
            else:
                pkt_S = self.out_queue.get(False)
                return pkt_S
        except queue.Empty:
            return None
    def put(self, pkt, in_or_out, block=False):
        if in_or_out == 'out':
            self.out_queue.put(pkt, block)
        else:
            self.in_queue.put(pkt, block)
class NetworkPacket:
    DST_LENGTH = 5
    PROTOCOL_LENGTH = 1
    def __init__(self, dst, prot_S, data_S):
        self.dst = dst
        self.data_S = data_S
        self.prot_S = prot_S
    def __str__(self):
        return self.to_byte_S()
    def to_byte_S(self):
        byte_S = str(self.dst).zfill(self.DST_LENGTH)
        if self.prot_S == 'data':
            byte_S += '1'
        elif self.prot_S == 'control':
            byte_S += '2'
        else:
            raise ValueError(f'Unknown prot_S option: {self.prot_S}')
        byte_S += self.data_S
        return byte_S
    @classmethod
    def from_byte_S(cls, byte_S):
        dst = byte_S[:cls.DST_LENGTH].strip('0')
        prot_S = byte_S[cls.DST_LENGTH: cls.DST_LENGTH + cls.PROTOCOL_LENGTH]
        if prot_S == '1':
            prot_S = 'data'
        elif prot_S == '2':
            prot_S = 'control'
        else:
            raise ValueError(f'Unknown prot_S field: {prot_S}')
        data_S = byte_S[cls.DST_LENGTH + cls.PROTOCOL_LENGTH:]
        return cls(dst, prot_S, data_S)
class Host:
    def __init__(self, addr):
        self.addr = addr
        self.intf_L = [Interface()]
        self.stop = False
    def __str__(self):
        return self.addr
    def udt_send(self, dst, data_S):
        packet = NetworkPacket(dst, 'data', data_S)
        print(f'{self}: SENDING PACKET "{packet}"')
        self.intf_L[0].put(packet.to_byte_S(), 'out')
    def udt_receive(self):
        packet_S = self.intf_L[0].get('in')
        if packet_S is not None:
            print(f'{self}: RECEIVED PACKET "{packet_S}"')
            if self.addr == 'H2':
                self.udt_send('H1', 'The way you look should be a sin, you my sensation')
    def run(self):
        print(f'{threading.currentThread().getName()}: Starting')
        while True:
            self.udt_receive()
            if self.stop:
                print(f'{threading.currentThread().getName()}: Ending')
                return
class Router:
    def __init__(self, name, cost_D, max_queue_size):
        self.stop = False
        self.name = name
        self.intf_L = [Interface(max_queue_size) for _ in range(len(cost_D))]
        self.neighbors = cost_D
        self.rt_tbl_D = cost_D.copy()
        self.total_rt = defaultdict(dict)
        for neighbor_name, neighbor_info in self.neighbors.items():
            for interface, cost in neighbor_info.items():
                self.total_rt[name][neighbor_name] = [cost]
        print(f'{self}: Initialized routing table')
        self.print_routes()
    def __str__(self):
        return self.name
    def process_queues(self):
        for i in range(len(self.intf_L)):
            packet_S = self.intf_L[i].get('in')
            if packet_S is not None:
                packet = NetworkPacket.from_byte_S(packet_S)
                if packet.prot_S == 'data':
                    self.forward_packet(packet, i)
                elif packet.prot_S == 'control':
                    self.update_routes(packet, i)
                else:
                    raise ValueError(f'Unknown packet type in packet {packet}')
    def forward_packet(self, packet, i):
        try:
            route = self.rt_tbl_D.get(str(packet.dst))
            for interface, cost in route.items():
                j = int(interface)
                break
            self.intf_L[j].put(packet.to_byte_S(), 'out', True)
            print(f'{self}: forwarding packet "{packet}" from interface {i} to {j}')
        except queue.Full:
            print(f'{self}: packet "{packet}" lost on interface {i}')
    def send_routes(self, i):
        print('sending_routes')
        contents = f'{self.name}->'
        for k, j in self.rt_tbl_D.items():
            for link, cost in j.items():
                contents += f'{k}_{link}_{cost} '
        packet = NetworkPacket(0, 'control', contents)
        self.intf_L[i].put(packet.to_byte_S(), 'out', True)
    def update_routes(self, packet, i):
        update_flag = 0
        contents = packet.data_S.split("->")
        name = contents[0]
        route_list = contents[1].split(" ")
        for item in route_list:
            if item != '':
                node_list = item.split("_")
                cur_node = node_list[0]
                node_par = int(node_list[2])
                self.total_rt[name][cur_node] = [node_par]
                if cur_node == self.name:
                    nei_key_value = int(list(self.neighbors[name].keys())[0])
                    self.rt_tbl_D[cur_node] = {nei_key_value: 0}
                    self.total_rt[self.name][cur_node] = [0]
                    continue
                else:
                    if cur_node not in self.neighbors and cur_node not in self.rt_tbl_D:
                        nei_name_value = list(self.neighbors[name].values())[0]
                        nei_key_value = int(list(self.neighbors[name].keys())[0])
                        self.rt_tbl_D[cur_node] = {nei_key_value: node_par + nei_name_value}
                        self.total_rt[self.name][cur_node] = [node_par + nei_name_value]
                        update_flag = 1
                    elif cur_node not in self.neighbors and cur_node in self.rt_tbl_D:
                        nei_name_value = list(self.neighbors[name].values())[0]
                        nei_key_value = int(list(self.neighbors[name].keys())[0])
                        cur_node_value = list(self.rt_tbl_D[cur_node].values())[0]
                        if cur_node_value > int(nei_name_value) + node_par:
                            self.rt_tbl_D[cur_node] = {nei_key_value: node_par + nei_name_value}
                            self.total_rt[self.name][cur_node] = [node_par + nei_name_value]
                            update_flag = 1
        if update_flag == 1:
            for neighbor_name, neighbor_info in self.neighbors.items():
                for interface, cost in neighbor_info.items():
                    if 'R' in neighbor_name:
                        self.send_routes(interface)
    def print_routes(self):
        cost_table = []
        print(f'cost table for {self}:')
        sort_tbl = OrderedDict(sorted(self.total_rt.items()))
        interfaces = []
        for item, j in sort_tbl.items():
            for link, cost in j.items():
                if link not in interfaces:
                    interfaces.append(link)
        interfaces = sorted(interfaces)
        for interface in interfaces:
            print(f'{interface}\t', end='')
            for item, j in sort_tbl.items():
                for link, cost in j.items():
                    if link == interface:
                        print(f'{cost[0]}\t', end='')
                        cost_table.append(cost[0])
        print("\n")
        table_str1 = ''
        table_str2 = ''
        for i in range(int(len(cost_table) / 2 + 1)):
            table_str1 += '| '
            table_str1 += str(cost_table[(i - 1) * 2])
            if i < len(cost_table):
                table_str2 += '| '
                table_str2 += str(cost_table[(i - 1) * 2 + 1])
        table_str1 += ' | '
        table_str2 += ' | '
        print(table_str1)
        print(table_str2)
        print("\n")
    def run(self):
        print(f'{threading.currentThread().getName()}: Starting')
        while True:
            self.process_queues()
            if self.stop:
                print(f'{threading.currentThread().getName()}: Ending')
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
devices[0].udt_send('H2', 'Test message from H1 to H2')