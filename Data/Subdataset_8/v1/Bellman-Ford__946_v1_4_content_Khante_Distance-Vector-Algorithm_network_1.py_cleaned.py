import threading
import queue
from collections import defaultdict, OrderedDict
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
    dst_S_length = 5
    prot_S_length = 1
    def __init__(self, dst, prot_S, data_S):
        self.dst = dst
        self.data_S = data_S
        self.prot_S = prot_S
    def __str__(self):
        return self.to_byte_S()
    def to_byte_S(self):
        byte_S = str(self.dst).zfill(self.dst_S_length)
        if self.prot_S == 'data':
            byte_S += '1'
        elif self.prot_S == 'control':
            byte_S += '2'
        else:
            raise ValueError('%s: unknown prot_S option: %s' % (self, self.prot_S))
        byte_S += self.data_S
        return byte_S
    @classmethod
    def from_byte_S(cls, byte_S):
        dst = byte_S[0:cls.dst_S_length].strip('0')
        prot_S = byte_S[cls.dst_S_length:cls.dst_S_length + cls.prot_S_length]
        if prot_S == '1':
            prot_S = 'data'
        elif prot_S == '2':
            prot_S = 'control'
        else:
            raise ValueError('%s: unknown prot_S field: %s' % (cls, prot_S))
        data_S = byte_S[cls.dst_S_length + cls.prot_S_length:]
        return cls(dst, prot_S, data_S)
class Host:
    def __init__(self, addr):
        self.addr = addr
        self.intf_L = [Interface()]
        self.stop = False
    def __str__(self):
        return self.addr
    def udt_send(self, dst, data_S):
        p = NetworkPacket(dst, 'data', data_S)
        print('%s: SENDING PACKET "%s"' % (self, p))
        self.intf_L[0].put(p.to_byte_S(), 'out')
    def udt_receive(self):
        pkt_S = self.intf_L[0].get('in')
        if pkt_S is not None:
            print('%s: RECEIVED PACKET "%s"' % (self, pkt_S))
    def run(self):
        print(threading.currentThread().getName() + ': Starting')
        while True:
            self.udt_receive()
            if self.stop:
                print(threading.currentThread().getName() + ': Ending')
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
        print('%s: Initialized routing table' % self)
        self.print_routes()
    def __str__(self):
        return self.name
    def process_queues(self):
        for i in range(len(self.intf_L)):
            pkt_S = self.intf_L[i].get('in')
            if pkt_S is not None:
                p = NetworkPacket.from_byte_S(pkt_S)
                if p.prot_S == 'data':
                    self.forward_packet(p, i)
                elif p.prot_S == 'control':
                    self.update_routes(p, i)
                else:
                    raise ValueError('%s: Unknown packet type in packet %s' % (self, p))
    def forward_packet(self, p, i):
        try:
            route = self.rt_tbl_D.get(str(p.dst))
            for interface, cost in route.items():
                j = int(interface)
                break
            self.intf_L[j].put(p.to_byte_S(), 'out', True)
            print('%s: forwarding packet "%s" from interface %d to %d' % (self, p, i, j))
        except queue.Full:
            print('%s: packet "%s" lost on interface %d' % (self, p, i))
    def send_routes(self, i):
        print('sending_routes')
        contents = self.name + "->"
        for k, j in self.rt_tbl_D.items():
            for link, cost in j.items():
                contents += str(k) + "_" + str(link) + "_" + str(cost) + " "
        p = NetworkPacket(0, 'control', contents)
        self.intf_L[i].put(p.to_byte_S(), 'out', True)
    def update_routes(self, p, i):
        updateFlag = 0
        contents = p.data_S.split("->")
        name = contents[0]
        routeList = contents[1].split(" ")
        for i in routeList:
            if i != '':
                nodeList = i.split("_")
                curNode = nodeList[0]
                nodePar = int(nodeList[2])
                self.total_rt[name][curNode] = [nodePar]
                if curNode == self.name:
                    neiKeyValue = int(list(self.neighbors[name].keys())[0])
                    self.rt_tbl_D[curNode] = {neiKeyValue: 0}
                    self.total_rt[self.name][curNode] = [0]
                    continue
                else:
                    if curNode not in self.neighbors and curNode not in self.rt_tbl_D:
                        neiNameValue = list(self.neighbors[name].values())[0]
                        neiKeyValue = int(list(self.neighbors[name].keys())[0])
                        self.rt_tbl_D[curNode] = {neiKeyValue: nodePar + neiNameValue}
                        self.total_rt[self.name][curNode] = [nodePar + neiNameValue]
                        updateFlag = 1
                    elif curNode not in self.neighbors and curNode in self.rt_tbl_D:
                        neiNameValue = list(self.neighbors[name].values())[0]
                        neiKeyValue = int(list(self.neighbors[name].keys())[0])
                        curNodeValue = list(self.rt_tbl_D[curNode].values())[0]
                        if curNodeValue > int(neiNameValue) + nodePar:
                            self.rt_tbl_D[curNode] = {neiKeyValue: nodePar + neiNameValue}
                            self.total_rt[self.name][curNode] = [nodePar + neiNameValue]
                            updateFlag = 1
        if updateFlag == 1:
            for neighbor_name, neighbor_info in self.neighbors.items():
                for interface, cost in neighbor_info.items():
                    if 'R' in neighbor_name:
                        self.send_routes(interface)
    def print_routes(self):
        costTable = []
        print('cost table for %s: ' % self)
        sort_tbl = OrderedDict(sorted(self.total_rt.items()))
        interfaces = []
        for i, j in sort_tbl.items():
            for link, cost in j.items():
                if not link in interfaces:
                    interfaces.append(link)
        interfaces = sorted(interfaces)
        for interface in interfaces:
            print(str(interface) + "\t", end='')
            for i, j in sort_tbl.items():
                for link, cost in j.items():
                    if link == interface:
                        print(str(cost) + "\t", end='')
                        costTable += [cost]
        print("\n")
        tablestr1 = ''
        tablestr2 = ''
        for i in range(int(len(costTable) / 2 + 1)):
            tablestr1 += '| '
            tablestr1 += str(costTable[(i - 1) * 2])
            if i < len(costTable):
                tablestr2 += '| '
                tablestr2 += str(costTable[(i - 1) * 2 + 1])
        tablestr1 += ' | '
        tablestr2 += ' | '
        print(tablestr1)
        print(tablestr2)
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
devices.append(Host('H1'))
devices.append(Host('H2'))
for device in devices:
    t = threading.Thread(target=device.run)
    t.start()
devices[0].udt_send('H2', 'Test message from H1 to H2')