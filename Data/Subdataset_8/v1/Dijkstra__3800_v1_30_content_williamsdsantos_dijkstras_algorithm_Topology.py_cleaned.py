class Topology:
    def __init__(self, filename):
        self.Nodes = []
        self.Links = []
        with open(filename, 'r') as TopologyData:
            next(TopologyData)
            for line in TopologyData:
                data = line.split()
                if len(data) == 0:
                    break
                node_id = data[2]
                self.Nodes.append(node_id)
            next(TopologyData)
            for line in TopologyData:
                data = line.split()
                if len(data) == 0:
                    break
                origin, destination, length = data[2:5]
                self.Links.append([origin, destination, length])
topology = Topology('data/topologies/PacificBell')
print("Nodes:", topology.Nodes)
print("Links:", topology.Links)