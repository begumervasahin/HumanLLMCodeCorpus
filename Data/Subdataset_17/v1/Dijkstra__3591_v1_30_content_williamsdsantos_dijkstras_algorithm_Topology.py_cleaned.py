class Topology:
    def __init__(self, file_path):
        self.Nodes = []
        self.Links = []
        with open(file_path, 'r') as topology_data:
            header_lines = [topology_data.readline() for _ in range(3)]
            for line in topology_data:
                data = line.split()
                if len(data) < 3:
                    break
                node_id = data[2]
                self.Nodes.append(node_id)
            header_lines += [topology_data.readline() for _ in range(3)]
            for line in topology_data:
                data = line.split()
                if len(data) < 5:
                    break
                origin = data[2]
                destination = data[3]
                length = data[4]
                elem_link = [origin, destination, length]
                self.Links.append(elem_link)
def main():
    file_path = 'data/topologies/PacificBell'
    topology = Topology(file_path)
    print("Nodes:", topology.Nodes)
    print("Links:", topology.Links)
if __name__ == "__main__":
    main()