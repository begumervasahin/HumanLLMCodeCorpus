import os
from mininext.topo import Topo
from collections import namedtuple
ChordDFSHost = namedtuple("ChordDFSHost", ["name", "ip"])
class ChordDFSTopo(Topo):
    def __init__(self, num_nodes):
        super().__init__()
        chordDFS_hosts = []
        for node_num in range(num_nodes):
            host = self.add_chord_dfs_host(node_num)
            chordDFS_hosts.append(host)
            self.create_node_directories(node_num)
        ixpfabric = self.addSwitch('sw1')
        for node in chordDFS_hosts:
            self.connect_host_to_switch(node, ixpfabric)
    def add_chord_dfs_host(self, node_num):
        host_name = f'n{node_num + 1}'
        host_ip = f'172.1.1.{node_num + 1}/24'
        return ChordDFSHost(name=host_name, ip=host_ip)
    def create_node_directories(self, node_num):
        node_dir = f"nodes/n{node_num + 1}"
        if not os.path.exists(node_dir):
            os.makedirs(node_dir)
            os.makedirs(f"{node_dir}/files/chord")
            os.makedirs(f"{node_dir}/files/client")
            os.makedirs(f"{node_dir}/logs")
        else:
            for root, dirs, files in os.walk(node_dir, topdown=False):
                for f in files:
                    os.remove(os.path.join(root, f))
def main():
    num_nodes = int(input("Enter the number of ChordDFS nodes: "))
    topo = ChordDFSTopo(num_nodes)
    topo.build()
if __name__ == "__main__":
    main()