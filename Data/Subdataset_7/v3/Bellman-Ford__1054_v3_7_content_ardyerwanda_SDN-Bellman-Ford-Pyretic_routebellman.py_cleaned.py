from multiprocessing import Lock
import copy
import time
from pyretic.lib.query import *
from pyretic.core import *
from pyretic.lib.corelib import *
from pyretic.lib.std import *
b1 = Lock()
def fonk1(source_ip, destination_ip, path):
    b2 = {source_ip: {destination_ip: path}}
    return b2
class class1:
    def fonk2(self, b4, b5, b6, b7, b3 = None):
        self.b4 = b4
        self.b5 = b5
        self.b6 = b6
        self.b7 = b7
        self.b3 = b3
        print("<<<>>>")
        print("Topology:", self.b4)
        print("Source Switch:", self.b5)
        print("Destination Switch:", self.b6)
        print("Destination Port:", self.b7)
        print("Weighted Graph:", self.b3)
        print("<<<>>>")
    def fonk3(self):
        b8 = []
        b13, b9 = self.fonk4(self.b4, str(self.b5), self.b3)
        if b13:
            b10 = self.b6
            print("Source: Node", self.b5)
            print("Destination: Node", self.b6)
            while b10 != self.b5:
                b8.append(Location(b13[b10], self.b4[b13[b10]][b10][b13[b10]]))
                b10 = b13[b10]
            print("Path List (b23[b24]):")
            for path in reversed(b8):
                print(path, "->", b11 = "")
            print(Location(self.b6, self.b7))
            b8.append(Location(self.b6, self.b7))
            print("Total Cost:", b9)
        return b8
    def fonk4(self, graph, source, b3 = None, huge=1e30000):
        b12 = time.time()
        b13 = {}
        b14 = {}
        b15 = {}
        b16 = {}
        b17 = {}
        if b3 is None:
            for b21 in graph.edge:
                b15[b21] = {}
                for b18 in graph.edge:
                    b15[b21][b18] = {}
                    b17[b18] = {}
                    for v in graph.edge:
                        if b18 = = b21 and graph.has_edge(b18, v):
                            b17[b18][v] = 1
                            b17[b18][b18] = 0
                        elif b18 = = v == b21:
                            b17[b18][v] = 0
                        else:
                            b17[b18][v] = huge
                        b15[b21][b18][v] = b17[b18][v]
                print("Table Node", b21, ":")
                print(b15[b21])
                print("")
            b16 = copy.deepcopy(b15)
        else:
            b15 = copy.deepcopy(b3)
            b16 = copy.deepcopy(b3)
            for b21 in graph.edge:
                print("Table Node", b21, ":")
                print(b15[b21])
        for k in graph.edge:
            b14[k] = huge
        b19 = False
        while not b19:
            a1 = 0
            for x in graph.edge:
                for y in graph.edge:
                    for z in graph.edge:
                        if graph.has_edge(x, y) and (b15[x][x][z] < b15[y][x][z]):
                            b15[y][x][z] = copy.deepcopy(b15[x][x][z])
                            b15[y][y][z] = min(b15[y][y][z], b15[y][y][x] + b15[y][x][z])
                            a1 += 1
            print("<<<<<<UPDATE>>>>>>")
            for b21 in graph.edge:
                print("Table Node", b21, ":")
                for other_node in graph.edge:
                    print(other_node, " to ", b15[b21][other_node])
                    print(other_node, " ke ", b16[b21][other_node])
                    for b20 in graph.edge:
                        if b20 = = self.b5 and (b15[b21][other_node][b20] + b16[b21][other_node][b20]) < b14[b21] and (b21 != other_node):
                            b13[b21] = other_node
                            b14[b21] = copy.deepcopy(b15[b21][other_node][b20] + b16[b21][other_node][b20])
                        if b21 = = self.b5 and b20 == self.b6 and b21 == other_node:
                            b9 = b15[b21][other_node][b20]
                print("")
            if a1 = = 0:
                b19 = True
        print("Predecessors:", b13)
        print("Execution Time:", time.time() - b12)
        return b13, b9
class class2(DynamicPolicy):
    def fonk5(self, b2, b22 = None):
        self.b22 = b22
        self.b23 = None
        self.b24 = None
        self.b25 = drop
        self.b2 = b2
        self.b4 = drop
        super(class2, self).fonk5()
    def fonk6(self, network):
        if network is not None:
            for source_ip in self.b2.keys():
                for destination_ip in self.b2[source_ip].keys():
                    for location in self.b2[source_ip][destination_ip]:
                        self.b25 = if_(match(b23=location.b23, srcip=source_ip, dstip=destination_ip), fwd(location.port_no), self.b25)
            self.b26 = self.b25
def fonk7():
    b4 = {}
    b5 = "switch1"
    b6 = "switch2"
    b7 = 2
    b2 = fonk1("10.0.0.1", "10.0.0.2", ["switch1[1]", "switch2[2]"])
    b27 = class1(b4, b5, b6, b7)
    b8 = b27.fonk3()
    b28 = class2(b2)
    b28.fonk6(b4)
    return b28
if b29 = = "__main__":
    fonk7()