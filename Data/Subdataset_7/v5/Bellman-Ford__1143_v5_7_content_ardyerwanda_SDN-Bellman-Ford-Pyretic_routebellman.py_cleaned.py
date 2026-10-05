from multiprocessing import Lock
import copy
import time
from pyretic.lib.query import *
from pyretic.core import *
from pyretic.lib.corelib import *
from pyretic.lib.std import *
b1 = Lock()
def fonk1(source_ip, destination_ip, path):
    return {source_ip: {destination_ip: path}}
class class1:
    def fonk2(self, b3, b4, b5, b6, b2 = None):
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
        self.b6 = b6
        self.b2 = b2
    def fonk3(self):
        b7 = []
        b11, b8 = self.fonk4(self.b3, str(self.b4), self.b2)
        if b11:
            b9 = self.b5
            while b9 != self.b4:
                b7.append(Location(b11[b9], self.b3[b11[b9]][b9][b11[b9]]))
                b9 = b11[b9]
            b7.append(Location(self.b5, self.b6))
        return b7, b8
    def fonk4(self, graph, source, b2 = None, huge=1e30000):
        b10 = time.time()
        b11 = {}
        b12 = {}
        b13 = b2.copy() if b2 else {b15: {u: {v: 1 if u == v == b15 else 0 if u == v else huge for v in graph.edge} for u in graph.edge} for b15 in graph.edge}
        for k in graph.edge:
            b12[k] = huge
        while True:
            a1 = 0
            for x in graph.edge:
                for y in graph.edge:
                    for z in graph.edge:
                        if graph.has_edge(x, y) and b13[x][x][z] < b13[y][x][z]:
                            b13[y][x][z] = b13[x][x][z]
                            b13[y][y][z] = min(b13[y][y][z], b13[y][y][x] + b13[y][x][z])
                            a1 += 1
            if a1 = = 0:
                break
        for b15 in graph.edge:
            for other_node in graph.edge:
                for b14 in graph.edge:
                    if b14 = = self.b4 and b13[b15][other_node][b14] + route_table2[b15][other_node][b14] < b12[b15] and b15 != other_node:
                        b11[b15] = other_node
                        b12[b15] = b13[b15][other_node][b14] + route_table2[b15][other_node][b14]
                    if b15 = = self.b4 and b14 == self.b5 and b15 == other_node:
                        b8 = b13[b15][other_node][b14]
        return b11, b8
class class2(DynamicPolicy):
    def fonk5(self, b20, b16 = None):
        self.b16 = b16
        self.b17 = None
        self.b18 = None
        self.b19 = drop
        self.b20 = b20
        self.b3 = drop
        super(class2, self).fonk5()
    def fonk6(self, network):
        if network is not None:
            for src_ip in self.b20.keys():
                for dst_ip in self.b20[src_ip].keys():
                    for loc in self.b20[src_ip][dst_ip]:
                        self.b19 = if_(match(b17=loc.b17, srcip=src_ip, dstip=dst_ip), fwd(loc.port_no), self.b19)
            self.policy