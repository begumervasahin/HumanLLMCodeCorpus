class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
if __name__ == "__main__":
    head = Node(0)
    head.next = Node(1)
    head.next.next = Node(2)
    current_node = head
    while current_node is not None:
        print(f'value = {current_node.value}')
        current_node = current_node.next