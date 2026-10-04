class Topology:
    def __init__(self, file_path='data/topologies/PacificBell'):
        self.nodes = []
        self.links = []
        self._read_topology_file(file_path)
    def _read_topology_file(self, file_path):
        with open(file_path, 'r') as file:
            self._skip_lines(file, 3)
            self._read_nodes(file)
            self._skip_lines(file, 3)
            self._read_links(file)
    def _skip_lines(self, file, num_lines):
        for _ in range(num_lines):
            next(file)
    def _read_nodes(self, file):
        for line in file:
            data = line.split()
            if len(data) < 3:
                break
            node_id = data[2]
            self.nodes.append(node_id)
    def _read_links(self, file):
        for line in file:
            data = line.split()
            if len(data) < 5:
                break
            origin = data[2]
            destination = data[3]
            length = data[4]
            self.links.append([origin, destination, length])
def main():
    topology = Topology()
    print("Nodes:", topology.nodes)
    print("Links:", topology.links)
if __name__ == "__main__":
    main()