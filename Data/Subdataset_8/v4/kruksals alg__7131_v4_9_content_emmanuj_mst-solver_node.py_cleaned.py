class Node:
    def __init__(self, value):
        self.value = value
        self.parent = self
        self.rank = 0
    def __repr__(self):
        return f"Node(value={self.value}, rank={self.rank}, parent={self.parent.value})"