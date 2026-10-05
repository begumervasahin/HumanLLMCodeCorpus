class Topology:
    def __init__(self):
        self.nodes = []
        self.links = []
        with open('data/topologies/PacificBell', 'r') as topology_data:
            for _ in range(3):
                next(topology_data)
            for line in topology_data:
                data = line.split()
                if not data:
                    break
                try:
                    node_id = data[2]
                    self.nodes.append(node_id)
                except IndexError:
                    break
            for _ in range(3):
                next(topology_data)
            for line in topology_data:
                data = line.split()
                if not data:
                    break
                try:
                    origin = data[2]
                    destination = data[3]
                    length = data[4]
                    elem_link = [origin, destination, length]
                    self.links.append(elem_link)
                except IndexError:
                    break
