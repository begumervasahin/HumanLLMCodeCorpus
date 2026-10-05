from pyretic.modules.routebellman import *
from pyretic.lib.corelib import *
from pyretic.lib.std import *
from pyretic.lib.b5 import *
from pyretic.modules.wG_bellfordCost import *
class class1(DynamicPolicy):
    def fonk1(self):
        super(class1,self).fonk1()
        self.b1 = {}
        self.b2 = None
        self.b3 = {}
        self.b4 = None
        self.fonk2()
    def fonk2(self):
        self.b5 = packets(1,['srcip'])
        self.b5.register_callback(self.buildflow)
        self.b6 = drop
        self.fonk4()
    def fonk3(self,network):
        if self.b2 and self.b2 = =network.b2:
            pass
        else:
            self.b2 = network.b2
        self.b4 = abileneCostList(self.b2)
        self.fonk2()
    def fonk4(self):
        self.b7 = self.b6 + self.b5
    def fonk5(self,pkt):
        if pkt['dstip']==IPAddr("10.0.0.1"):
            b8 = build_path(self.b2,1,pkt['switch'],pkt['inport'],self.b4)
            b9 = b8.bellford_routing()
            print b9
            b10 = build_dic(IPAddr("10.0.0.1"),pkt['srcip'],b9)
            if self.b3.has_key(IPAddr("10.0.0.1")):
                self.b3[IPAddr("10.0.0.1")].update(b10[IPAddr("10.0.0.1")])
            else:
                self.b3.update(b10)
            b11 = build_path(self.b2,pkt['switch'],1,1,self.b4)
            b12 = b11.bellford_routing()
            b10 = build_dic(pkt['srcip'],IPAddr("10.0.0.1"),b12)
            if self.b3.has_key(pkt['srcip']):
                self.b3[pkt['srcip']].update(b10[pkt['srcip']])
            else:
                self.b3.update(b10)
            self.b6 = build_flowtable(self.b3)
        self.fonk4()
def fonk6():
    return class1()