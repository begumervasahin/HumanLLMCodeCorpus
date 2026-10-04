
__author__ = "Gonzalo Chacaltana Buleje"
__email__ = "gchacaltanab@gmail.com"
from Node import Node
class UninformedSearchAlgorithm:
    def __init__(self, list_nodes, target):
        self.list_nodes = list_nodes
        self.target = target
        self.create_queue()
    def create_queue(self):
        self.queue = [self.list_nodes[0]]
    def add_to_queue(self, node):
        pass
    def read_from_queue(self):
        return self.queue.pop(0)
    def get_queue_length(self):
        return len(self.queue)
    def get_node_by_name(self, name):
        for node in self.list_nodes:
            if node.name == name:
                return node
        return None
    def validate_queue_length(self):
        if self.get_queue_length() == 0:
            raise Exception("The queue is empty")
    def check_if_target(self, node_name):
        if node_name == self.target:
            raise Exception(f"Target city found: {node_name}")
    def search(self):
        pass
    def insert_children_into_queue(self, node):
        children = node.get_children()
        for child in children:
            child_node = self.get_node_by_name(child.name)
            if isinstance(child_node, Node):
                self.add_to_queue(child_node)
if __name__ == "__main__":
    nodes = [...]
    target_city = "Arequipa"
    search_algorithm = UninformedSearchAlgorithm(nodes, target_city)
    try:
        search_algorithm.search()
    except Exception as e:
        print(e)