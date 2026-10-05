from Node import Node
class UninformedSearchAlgorithm:
    def __init__(self, list_nodes, searched):
        self.list_nodes = list_nodes
        self.searched = searched
        self.create_queue()
    def create_queue(self):
        self.queue = [self.list_nodes[0]]
    def read_queue(self):
        return self.queue.pop(0)
    def get_queue_len(self):
        return len(self.queue)
    def get_node_from_list(self, name):
        for node in self.list_nodes:
            if node.name == name:
                return node
    def validate_queue_length(self):
        if not self.queue:
            raise Exception("The queue is empty")
    def match_searched(self, node_name):
        if node_name == self.searched:
            raise Exception("City found: %s" % node_name)
    def search(self):
        pass
    def insert_node_child_queue(self, node):
        children_nodes = node.get_children_nodes()
        for child in children_nodes:
            child_node = self.get_node_from_list(child.name)
            if isinstance(child_node, Node):
                self.add_queue(child_node)
    def add_queue(self, node):
        self.queue.append(node)
if __name__ == "__main__":
    nodes = {
        "Tumbes": Node("Tumbes"),
        "Trujillo": Node("Trujillo"),
        "Moyobamba": Node("Moyobamba"),
        "Iquitos": Node("Iquitos"),
        "Lima": Node("Lima"),
        "Huancayo": Node("Huancayo"),
        "Nazca": Node("Nazca"),
        "Puno": Node("Puno"),
        "Cusco": Node("Cusco"),
        "Arequipa": Node("Arequipa")
    }
    nodes["Tumbes"].add_child(nodes["Trujillo"])
    nodes["Tumbes"].add_child(nodes["Moyobamba"])
    nodes["Tumbes"].add_child(nodes["Iquitos"])
    nodes["Trujillo"].add_child(nodes["Lima"])
    nodes["Trujillo"].add_child(nodes["Huancayo"])
    nodes["Moyobamba"].add_child(nodes["Huancayo"])
    nodes["Iquitos"].add_child(nodes["Huancayo"])
    nodes["Iquitos"].add_child(nodes["Cusco"])
    nodes["Lima"].add_child(nodes["Nazca"])
    nodes["Huancayo"].add_child(nodes["Arequipa"])
    nodes["Huancayo"].add_child(nodes["Puno"])
    nodes["Nazca"].add_child(nodes["Arequipa"])
    nodes["Puno"].add_child(nodes["Arequipa"])
    nodes["Cusco"].add_child(nodes["Arequipa"])
    search_algorithm = UninformedSearchAlgorithm(nodes.values(), "Arequipa")
    try:
        search_algorithm.search()
    except Exception as e:
        print(e)