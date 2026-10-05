class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
if __name__ == "__main__":
    node1 = Node(0)
    node2 = Node(1)
    node3 = Node(2)
    node1.next = node2
    node2.next = node3
    print(f'Value of node1: {node1.value}')
    print(f'Value of node2: {node2.value}')
    print(f'Value of node3: {node3.value}')