import os
from mininext.topo import Topo
from mininext.services.quagga import QuaggaService
from collections import namedtuple
ChordDFSHost = namedtuple("ChordDFSHost", "name ip")
net = None
class ChordDFSTopo(Topo):
    def __init__(self, num_nodes):
        Topo.__init__(self)
        chordDFS_hosts = []
        for node in range(num_nodes):
            host = self.addHost(name=f'n{node+1}', ip=f'172.1.1.{node+1}/24')
            chordDFS_hosts.append(host)
            node_dir = f"nodes/n{node+1}"
            if not os.path.exists(node_dir):
                os.makedirs(node_dir)
                os.makedirs(f"{node_dir}/files/chord")
                os.makedirs(f"{node_dir}/files/client")
                os.makedirs(f"{node_dir}/logs")
            else:
                for root, dirs, files in os.walk(node_dir, topdown=False):
                    for f in files:
                        os.remove(os.path.join(root, f))
        ixpfabric = self.addSwitch('sw1')
        for node in chordDFS_hosts:
            self.addLink(node, ixpfabric)
def main():
    num_nodes = int(input("Enter the number of ChordDFS nodes: "))
    topo = ChordDFSTopo(num_nodes)
    topo.build()
if __name__ == "__main__":
    main()