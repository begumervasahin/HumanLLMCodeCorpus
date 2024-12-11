from multiprocessing import Lock
from pyretic.lib.query import *
from pyretic.core import *
from pyretic.lib.corelib import *
from pyretic.lib.std import *
def fonk1(sip,dip,path):
    b1 = {}
    b1[sip]={dip:path}
    return b1
class  build_path():
    def fonk2(self,b3,b20,b5,b6,b2 = None):
        self.b3 = b3
        self.b4 = b20
        self.b5 = b5
        self.b6 = b6
        self.b2 = b2
	print "<<<>>>"
	print self.b3
	print self.b4
	print self.b5
	print self.b6
	print self.b2
	print "<<<>>>"
    def fonk3(self):
        b7 = []
        b11, b8 = self.fonk4(self.b3,str(self.b4),self.b2)
        if b11:
            b9 = self.b5
            print "Asal  : Node ", self.b4
            print "Tujuan: Node ", self.b5
            while(b9 != self.b4):
                b7.append(Location(b11[b9],self.b3[b11[b9]][b9][b11[b9]]))
                b9 = b11[b9]
            print "b7 <<b20[b21]>>: "
            for a in reversed(b7):
                print a, "->",
            print Location(self.b5,self.b6)
            b7.append(Location(self.b5,self.b6))
            print "Total cost: ", b8
        return b7
    def fonk4(self,G,source,b2 = None,huge=1e30000):
        b10 = time.time()
        b11 = {}
        b12 = {}
        b13 = {}
        b14 = {}
        b15 = {}
        if b2 = = None:
            a1 = 0
            for a1 in G.edge:
                b13[a1]={}
                for b16 in G.edge:
                    b13[a1][b16]={}
                    b15[b16]={}
                    for b9 in G.edge:
                        if b16 = =a1 and G.has_edge(b16,b9):
                            b15[b16][b9] = 1
                            b15[b16][b16]=0
                        elif b16 = =b9 and b9==a1:
                            b15[b16][b9]=0
                        else:
                            b15[b16][b9]=huge
                        b13[a1][b16][b9]=b15[b16][b9]
                print "table node",a1,": ", b13[a1]
                print " "
            b14 = copy.deepcopy(b13)
        else:
            b13 = copy.deepcopy(b2)
            b14 = copy.deepcopy(b2)
            for a1 in G.edge:
                print "table node",a1,": ", b13[a1]
        for k in G.edge:
            b12[k] = huge
        b17 = False
        while not b17:
            a2 = 0
            for x in G.edge:
                for y in G.edge:
                    for z in G.edge:
                        if G.has_edge(x,y) and (b13[x][x][z] < b13[y][x][z]):
                            b13[y][x][z] = copy.deepcopy(b13[x][x][z])
                            b13[y][y][z] = min(b13[y][y][z],b13[y][y][x]+b13[y][x][z])
                            a2 = a2 + 1
            print "<<<<<<UPDATE>>>>>>>"
            for a1 in G.edge:
                print "table node",a1,": "
                for RT2 in G.edge:
                    print RT2," to ",b13[a1][RT2]
                    print RT2," ke ",b14[a1][RT2]
                    for b18 in G.edge:
                        if b18 = = self.b4 and (b13[a1][RT2][b18] + b14[a1][a1][RT2])<b12[a1] and (a1 != RT2):
                            b11[a1] = RT2
                            b12[a1]=copy.deepcopy(b13[a1][RT2][b18] + b14[a1][a1][RT2])
                        if a1 = = self.b4 and b18 == self.b5 and a1 == RT2:
                            b8 = b13[a1][RT2][b18]
                print " "
            if a2 = = 0: b17 = True
        print b11
        print "Waktu Eksekusi: ",time.time() - b10
        return b11,b8
class class1(DynamicPolicy):
    def fonk5(self,b1, b19 = None):
        self.b19 = b19
        self.b20 = None
        self.b21 = None
        self.b22 = drop
        self.b1 = b1
        self.b3 = drop
        super(class1,self).fonk5()
    def fonk6(self, network):
        if not network is None:
            for sip in self.b1.keys():
                for dip in self.b1[sip].keys():
                    for loc in self.b1[sip][dip]:
                        self.b22 = if_(match(b20 = loc.b20, srcip=sip,dstip=dip),fwd(loc.port_no),self.b22)
            self.b23 = self.b22