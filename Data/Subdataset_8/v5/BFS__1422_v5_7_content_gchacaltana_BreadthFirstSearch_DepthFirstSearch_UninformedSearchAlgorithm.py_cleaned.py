from Node import Node
class UninformedSearchAlgorithm:
    def __init__(self, listNodes, searched):
        self.listNodes = listNodes
        self.searched = searched
        self.create_queue()
    def create_queue(self):
        self.queue = [self.listNodes[0]]
    def read_queue(self):
        return self.queue.pop(0)
    def get_queue_len(self):
        return len(self.queue)
    def get_node_from_list(self, name):
        for node in self.listNodes:
            if node.name == name:
                return node
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