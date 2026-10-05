from multiprocessing import Lock
from pyretic.lib.query import *
from pyretic.core import *
from pyretic.lib.corelib import *
from pyretic.lib.std import *
import copy
import time
b1 = Lock()
def fonk1(sip, dip, path):
    b2 = {}
    b2[sip] = {dip: path}
    return b2
class class1:
    def fonk2(self, b4, b22, b6, b7, b3 = None):
        self.b4 = b4
        self.b5 = b22
        self.b6 = b6
        self.b7 = b7
        self.b3 = b3
        print("<<<>>>")
        print(self.b4)
        print(self.b5)
        print(self.b6)
        print(self.b7)
        print(self.b3)
        print("<<<>>>")
    def fonk3(self):
        b8 = []
        b13, b9 = self.fonk4(self.b4, str(self.b5), self.b3)
        if b13:
            b10 = self.b6
            print("Asal  : Node ", self.b5)
            print("Tujuan: Node ", self.b6)
            while b10 != self.b5:
                b8.append(Location(b13[b10], self.b4[b13[b10]][b10][b13[b10]]))
                b10 = b13[b10]
            print("b8 <<b22[b23]>>: ")
            for a in reversed(b8):
                print(a, "->", b11 = "")
            print(Location(self.b6, self.b7))
            b8.append(Location(self.b6, self.b7))
            print("Total cost: ", b9)
        return b8
    def fonk4(self, G, source, b3 = None, huge=1e30000):
        b12 = time.time()
        b13 = {}
        b14 = {}
        b15 = {}
        b16 = {}
        b17 = {}
        if b3 is None:
            a1 = 0
            for a1 in G.edge:
                b15[a1] = {}
                for b18 in G.edge:
                    b15[a1][b18] = {}
                    b17[b18] = {}
                    for b10 in G.edge:
                        if b18 = = a1 and G.has_edge(b18, b10):
                            b17[b18][b10] = 1
                            b17[b18][b18] = 0
                        elif b18 = = b10 and b10 == a1:
                            b17[b18][b10] = 0
                        else:
                            b17[b18][b10] = huge
                        b15[a1][b18][b10] = b17[b18][b10]
                print("table node", a1, ": ", b15[a1])
                print(" ")
            b16 = copy.deepcopy(b15)
        else:
            b15 = copy.deepcopy(b3)
            b16 = copy.deepcopy(b3)
            for a1 in G.edge:
                print("table node", a1, ": ", b15[a1])
        for k in G.edge:
            b14[k] = huge
        b19 = False
        while not b19:
            a2 = 0
            for x in G.edge:
                for y in G.edge:
                    for z in G.edge:
                        if G.has_edge(x, y) and (b15[x][x][z] < b15[y][x][z]):
                            b15[y][x][z] = copy.deepcopy(b15[x][x][z])
                            b15[y][y][z] = min(b15[y][y][z], b15[y][y][x] + b15[y][x][z])
                            a2 += 1
            print("<<<<<<UPDATE>>>>>>")
            for a1 in G.edge:
                print("table node", a1, ": ")
                for RT2 in G.edge:
                    print(RT2, " to ", b15[a1][RT2])
                    print(RT2, " ke ", b16[a1][RT2])
                    for b20 in G.edge:
                        if b20 = = self.b5 and (b15[a1][RT2][b20] + b16[a1][a1][RT2]) < b14[a1] and (a1 != RT2):
                            b13[a1] = RT2
                            b14[a1] = copy.deepcopy(b15[a1][RT2][b20] + b16[a1][a1][RT2])
                        if a1 = = self.b5 and b20 == self.b6 and a1 == RT2:
                            b9 = b15[a1][RT2][b20]
                print(" ")
            if a2 = = 0:
                b19 = True
        print(b13)
        print("Waktu Eksekusi: ", time.time() - b12)
        return b13, b9
class class2(DynamicPolicy):
    def fonk5(self, b2, b21 = None):
        self.b21 = b21
        self.b22 = None
        self.b23 = None
        self.b24 = drop
        self.b2 = b2
        self.b4 = drop
        super(class2, self).fonk5()
    def fonk6(self, network):
        if network is not None:
            for sip in self.b2.keys():
                for dip in self.b2[sip].keys():
                    for loc in self.b2[sip][dip]:
                        self.b24 = if_(match(b22=loc.b22, srcip=sip, dstip=dip), fwd(loc.port_no), self.b24)
            self.b25 = self.b24
def fonk7():
    b4 = {}
    b22 = "switch1"
    b6 = "switch2"
    b7 = 2
    b2 = fonk1("10.0.0.1", "10.0.0.2", ["switch1[1]", "switch2[2]"])
    b26 = class1(b4, b22, b6, b7)
    b27 = b26.fonk3()
    b28 = class2(b2)
    b28.fonk6(b4)
    return b28
if b29 = = "__main__":
    fonk7()