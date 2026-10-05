from Node import Node
class UninformedSearchAlgorithm:
    def __init__(self, list_nodes, searched):
        self.list_nodes = list_nodes
        self.searched = searched
        self.create_queue()
    def create_queue(self):
        self.queue = []
        self.queue.append(self.list_nodes[0])
    def read_queue(self):
        return self.queue.pop(0)
    def get_queue_len(self):
        return len(self.queue)
    def get_node_from_list(self, name):
        for node in self.list_nodes:
            if node.name == name:
                return node
    def validate_queue_length(self):
        if self.get_queue_len() == 0:
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
if __name__ == "__main__":
    Tumbes = Node("Tumbes")
    Trujillo = Node("Trujillo")
    Moyobamba = Node("Moyobamba")
    Iquitos = Node("Iquitos")
    Lima = Node("Lima")
    Huancayo = Node("Huancayo")
    Nazca = Node("Nazca")
    Puno = Node("Puno")
    Cusco = Node("Cusco")
    Arequipa = Node("Arequipa")
    Tumbes.add_child(Trujillo)
    Tumbes.add_child(Moyobamba)
    Tumbes.add_child(Iquitos)
    Trujillo.add_child(Lima)
    Trujillo.add_child(Huancayo)
    Moyobamba.add_child(Huancayo)
    Iquitos.add_child(Huancayo)
    Iquitos.add_child(Cusco)
    Lima.add_child(Nazca)
    Huancayo.add_child(Arequipa)
    Huancayo.add_child(Puno)
    Nazca.add_child(Arequipa)
    Puno.add_child(Arequipa)
    Cusco.add_child(Arequipa)
    search_algorithm = UninformedSearchAlgorithm([Tumbes, Trujillo, Moyobamba, Iquitos, Lima, Huancayo, Nazca, Puno, Cusco, Arequipa], "Arequipa")
    try:
        search_algorithm.search()
    except Exception as e:
        print(e)