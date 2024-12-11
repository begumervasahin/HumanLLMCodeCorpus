from multiprocessing import Lock
import copy
import time
from pyretic.lib.query import *
from pyretic.core import *
from pyretic.lib.corelib import *
from pyretic.lib.std import *
b1 = Lock()
def fonk1(sip, dip, path):
    b2 = {sip: {dip: path}}
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
            for a in reversed(b8):
                print(a, "->", b11 = "")
            print(Location(self.b6, self.b7))
            b8.append(Location(self.b6, self.b7))
            print("Total Cost:", b9)
        return b8
    def fonk4(self, G, source, b3 = None, huge=1e30000):
        b12 = time.time()
        b13 = {}
        b14 = {}
        b15 = {}
        b16 = {}
        b17 = {}
        if b3 is None:
            for b21 in G.edge:
                b15[b21] = {}
                for b18 in G.edge:
                    b15[b21][b18] = {}
                    b17[b18] = {}
                    for b10 in G.edge:
                        if b18 = = b21 and G.has_edge(b18, b10):
                            b17[b18][b10] = 1
                            b17[b18][b18] = 0
                        elif b18 = = b10 and b10 == b21:
                            b17[b18][b10] = 0
                        else:
                            b17[b18][b10] = huge
                        b15[b21][b18][b10] = b17[b18][b10]
                print("Table Node", b21, ":")
                print(b15[b21])
                print("")
            b16 = copy.deepcopy(b15)
        else:
            b15 = copy.deepcopy(b3)
            b16 = copy.deepcopy(b3)
            for b21 in G.edge:
                print("Table Node", b21, ":")
                print(b15[b21])
        for k in G.edge:
            b14[k] = huge
        b19 = False
        while not b19:
            a1 = 0
            for x in G.edge:
                for y in G.edge:
                    for z in G.edge:
                        if G.has_edge(x, y) and (b15[x][x][z] < b15[y][x][z]):
                            b15[y][x][z] = copy.deepcopy(b15[x][x][z])
                            b15[y][y][z] = min(b15[y][y][z], b15[y][y][x] + b15[y][x][z])
                            a1 += 1
            print("<<<<<<UPDATE>>>>>>")
            for b21 in G.edge:
                print("Table Node", b21, ":")
                for RT2 in G.edge:
                    print(RT2, " to ", b15[b21][RT2])
                    print(RT2, " ke ", b16[b21][RT2])
                    for b20 in G.edge:
                        if b20 = = self.b5 and (b15[b21][RT2][b20] + b16[b21][b21][RT2]) < b14[b21] and (b21 != RT2):
                            b13[b21] = RT2
                            b14[b21] = copy.deepcopy(b15[b21][RT2][b20] + b16[b21][b21][RT2])
                        if b21 = = self.b5 and b20 == self.b6 and b21 == RT2:
                            b9 = b15[b21][RT2][b20]
                print("")
            if a1 = = 0:
                b19 = True
        print("Pred:", b13)
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
            for sip in self.b2.keys():
                for dip in self.b2[sip].keys():
                    for loc in self.b2[sip][dip]:
                        self.b25 = if_(match(b23=loc.b23, srcip=sip, dstip=dip), fwd(loc.port_no), self.b25)
            self.b26 = self.b25
def fonk7():
    b4 = {}
    b5 = "switch1"
    b6 = "switch2"
    b7 = 2
    b2 = fonk1("10.0.0.1", "10.0.0.2", ["switch1[1]", "switch2[2]"])
    b27 = class1(b4, b5, b6, b7)
    b28 = b27.fonk3()
    b29 = class2(b2)
    b29.fonk6(b4)
    return b29
if b30 = = "__main__":
    fonk7()