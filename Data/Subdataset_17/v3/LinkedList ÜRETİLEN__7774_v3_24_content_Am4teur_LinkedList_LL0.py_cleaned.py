class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
if __name__ == "__main__":
    head = Node(0)
    second_node = Node(1)
    third_node = Node(2)
    head.next = second_node
    second_node.next = third_node
    current_node = head
    while current_node is not None:
        print(f'value = {current_node.value}')
        current_node = current_node.next