class Topology:
    def __init__(self, filename):
        self.nodes = []
        self.links = []
        with open(filename, 'r') as topology_file:
            for _ in range(3):
                next(topology_file)
            for line in topology_file:
                data = line.split()
                if not data:
                    break
                node_id = data[2]
                self.nodes.append(node_id)
            for _ in range(3):
                next(topology_file)
            for line in topology_file:
                data = line.split()
                if not data:
                    break
                origin, destination, length = data[2:5]
                self.links.append([origin, destination, length])
topology = Topology('data/topologies/PacificBell')
print("Nodes:", topology.nodes)
print("Links:", topology.links)