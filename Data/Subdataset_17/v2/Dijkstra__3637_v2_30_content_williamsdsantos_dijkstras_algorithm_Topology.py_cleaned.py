class Topology:
    def __init__(self, file_path):
        self.nodes = []
        self.links = []
        self._read_topology_file(file_path)
    def _read_topology_file(self, file_path):
        with open(file_path, 'r') as topology_data:
            for _ in range(3):
                next(topology_data)
            self._read_nodes(topology_data)
            for _ in range(3):
                next(topology_data)
            self._read_links(topology_data)
    def _read_nodes(self, topology_data):
        for line in topology_data:
            data = line.split()
            if len(data) < 3:
                break
            node_id = data[2]
            self.nodes.append(node_id)
    def _read_links(self, topology_data):
        for line in topology_data:
            data = line.split()
            if len(data) < 5:
                break
            origin = data[2]
            destination = data[3]
            length = data[4]
            elem_link = [origin, destination, length]
            self.links.append(elem_link)
def main():
    file_path = 'data/topologies/PacificBell'
    topology = Topology(file_path)
    print("Nodes:", topology.nodes)
    print("Links:", topology.links)
if __name__ == "__main__":
    main()