class Topology:
    def __init__(self, filename):
        self.nodes = []
        self.links = []
        with open(filename, 'r') as topology_file:
            self._skip_header(topology_file, 3)
            self._read_nodes(topology_file)
            self._skip_header(topology_file, 3)
            self._read_links(topology_file)
    def _skip_header(self, file_obj, num_lines):
        for _ in range(num_lines):
            next(file_obj)
    def _read_nodes(self, file_obj):
        for line in file_obj:
            data = line.split()
            if not data:
                break
            try:
                node_id = data[2]
                self.nodes.append(node_id)
            except IndexError:
                break
    def _read_links(self, file_obj):
        for line in file_obj:
            data = line.split()
            if not data:
                break
            try:
                origin, destination, length = data[2:5]
                elem_link = [origin, destination, length]
                self.links.append(elem_link)
            except IndexError:
                break
