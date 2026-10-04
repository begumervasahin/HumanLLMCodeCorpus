
class Node:
    def __init__(self, value):
        self.value = value
        self.parent = self
        self.rank = 0
    def __repr__(self):
        """
        Returns a string representation of the Node object.
        Format: "n value r rank p parent_value"
        """
        return f"n {self.value} r {self.rank} p {self.parent.value}"
if __name__ == "__main__":
    node = Node(5)
    print(node)
