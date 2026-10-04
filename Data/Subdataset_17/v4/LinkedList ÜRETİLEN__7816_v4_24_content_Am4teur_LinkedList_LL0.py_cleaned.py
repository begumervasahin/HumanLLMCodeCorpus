class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
def main():
    ll = Node(0)
    ll.next = Node(1)
    ll.next.next = Node(2)
    current_node = ll
    while current_node:
        print(f'value = {current_node.value}')
        current_node = current_node.next
if __name__ == "__main__":
    main()