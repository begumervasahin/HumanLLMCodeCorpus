import os
from mininext.b9 import Topo
from mininext.services.quagga import QuaggaService
from collections import namedtuple
b1 = namedtuple("b1", "name ip")
b2 = None
class class1(Topo):
    def fonk1(self, b8):
        Topo.fonk1(self)
        b3 = []
        for node in range(b8):
            b4 = self.addHost(name=f'n{node+1}', ip=f'172.1.1.{node+1}/24')
            b3.append(b4)
            b5 = f"nodes/n{node+1}"
            if not os.path.exists(b5):
                os.makedirs(b5)
                os.makedirs(f"{b5}/files/chord")
                os.makedirs(f"{b5}/files/client")
                os.makedirs(f"{b5}/logs")
            else:
                for root, dirs, files in os.walk(b5, b6 = False):
                    for f in files:
                        os.remove(os.path.join(root, f))
        b7 = self.addSwitch('sw1')
        for node in b3:
            self.addLink(node, b7)
def fonk2():
    b8 = int(input("Enter the number of ChordDFS nodes: "))
    b9 = class1(b8)
    b9.build()
if b10 = = "__main__":
    fonk2()