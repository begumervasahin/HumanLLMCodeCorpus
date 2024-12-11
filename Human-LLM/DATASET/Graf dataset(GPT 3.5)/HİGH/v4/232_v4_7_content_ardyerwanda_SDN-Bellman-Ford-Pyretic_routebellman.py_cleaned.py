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
        print("<<<>>>")
        print("Topology:", self.b3)
        print("Source Switch:", self.b4)
        print("Destination Switch:", self.b5)
        print("Destination Port:", self.b6)
        print("Weighted Graph:", self.b2)
        print("<<<>>>")
    def fonk3(self):
        b7 = []
        b12, b8 = self.fonk4(self.b3, str(self.b4), self.b2)
        if b12:
            b9 = self.b5
            print("Source: Node", self.b4)
            print("Destination: Node", self.b5)
            while b9 != self.b4:
                b7.append(Location(b12[b9], self.b3[b12[b9]][b9][b12[b9]]))
                b9 = b12[b9]
            print("Path list <<b22[b23]>>:")
            for a in reversed(b7):
                print(a, "->", b10 = "")
            print(Location(self.b5, self.b6))
            b7.append(Location(self.b5, self.b6))
            print("Total cost:", b8)
        return b7
    def fonk4(self, graph, source, b2 = None, huge=1e30000):
        b11 = time.time()
        b12 = {}
        b13 = {}
        b14 = {}
        b15 = {}
        b16 = {}
        if b2 is None:
            for b20 in graph.edge:
                b14[b20] = {}
                for b17 in graph.edge:
                    b14[b20][b17] = {}
                    b16[b17] = {}
                    for b9 in graph.edge:
                        if b17 = = b20 and graph.has_edge(b17, b9):
                            b16[b17][b9] = 1
                            b16[b17][b17] = 0
                        elif b17 = = b9 == b20:
                            b16[b17][b9] = 0
                        else:
                            b16[b17][b9] = huge
                        b14[b20][b17][b9] = b16[b17][b9]
                print("Table node", b20, ":")
                print(b14[b20])
                print("")
            b15 = copy.deepcopy(b14)
        else:
            b14 = copy.deepcopy(b2)
            b15 = copy.deepcopy(b2)
            for b20 in graph.edge:
                print("Table node", b20, ":")
                print(b14[b20])
        for k in graph.edge:
            b13[k] = huge
        b18 = False
        while not b18:
            a1 = 0
            for x in graph.edge:
                for y in graph.edge:
                    for z in graph.edge:
                        if graph.has_edge(x, y) and (b14[x][x][z] < b14[y][x][z]):
                            b14[y][x][z] = copy.deepcopy(b14[x][x][z])
                            b14[y][y][z] = min(b14[y][y][z], b14[y][y][x] + b14[y][x][z])
                            a1 += 1
            print("<<<<<<UPDATE>>>>>>")
            for b20 in graph.edge:
                print("Table node", b20, ":")
                for rt2 in graph.edge:
                    print(rt2, " to ", b14[b20][rt2])
                    print(rt2, " ke ", b15[b20][rt2])
                    for b19 in graph.edge:
                        if b19 = = self.b4 and (b14[b20][rt2][b19] + b15[b20][b20][rt2]) < b13[b20] and (b20 != rt2):
                            b12[b20] = rt2
                            b13[b20] = copy.deepcopy(b14[b20][rt2][b19] + b15[b20][b20][rt2])
                        if b20 = = self.b4 and b19 == self.b5 and b20 == rt2:
                            b8 = b14[b20][rt2][b19]
                print(" ")
            if a1 = = 0:
                b18 = True
        print("Pred:", b12)
        print("Execution Time:", time.time() - b11)
        return b12, b8
class class2(DynamicPolicy):
    def fonk5(self, b25, b21 = None):
        self.b21 = b21
        self.b22 = None
        self.b23 = None
        self.b24 = drop
        self.b25 = b25
        self.b3 = drop
        super(class2, self).fonk5()
    def fonk6(self, network):
        if network is not None:
            for sip in self.b25.keys():
                for dip in self.b25[sip].keys():
                    for loc in self.b25[sip][dip]:
                        self.b24 = if_(match(b22=loc.b22, srcip=sip, dstip=dip), fwd(loc.port_no), self.b24)
            self.b26 = self.b24
def fonk7():
    b3 = {}
    b4 = "switch1"
    b5 = "switch2"
    b6 = 2
    b25 = fonk1("10.0.0.1", "10.0.0.2", ["switch1[1]", "switch2[2]"])
    b27 = class1(b3, b4, b5, b6)
    b7 = b27.fonk3()
    b28 = class2(b25)
    b28.fonk6(b3)
    return b28
if b29 = = "__main__":
    fonk7()