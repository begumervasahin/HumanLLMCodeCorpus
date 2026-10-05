import os
from mininext.b11 import Topo
from collections import namedtuple
b1 = namedtuple("b1", ["b7", "ip"])
class class1(Topo):
    def fonk1(self, b10):
        super().fonk1()
        b2 = []
        for node in range(b10):
            b3 = self.fonk2(node)
            b2.append(b3)
            self.fonk3(node)
        b4 = self.addSwitch('sw1')
        for node in b2:
            self.connectHostToSwitch(node, b4)
    def fonk2(self, node_num):
        b5 = f'n{node_num + 1}'
        b6 = f'172.1.1.{node_num + 1}/24'
        return b1(b7 = b5, ip=b6)
    def fonk3(self, node_num):
        b8 = f"nodes/n{node_num + 1}"
        if not os.path.exists(b8):
            os.makedirs(b8)
            os.makedirs(f"{b8}/files/chord")
            os.makedirs(f"{b8}/files/client")
            os.makedirs(f"{b8}/logs")
        else:
            for root, dirs, files in os.walk(b8, b9 = False):
                for f in files:
                    os.remove(os.path.join(root, f))
def fonk4():
    b10 = int(input("Enter the number of ChordDFS nodes: "))
    b11 = class1(b10)
    b11.build()
if b12 = = "__main__":
    fonk4()