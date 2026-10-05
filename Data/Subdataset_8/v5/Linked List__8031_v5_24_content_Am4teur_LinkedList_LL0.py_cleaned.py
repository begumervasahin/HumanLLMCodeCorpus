class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
if __name__ == "__main__":
    linked_list = Node(0)
    linked_list.next = Node(1)
    linked_list.next.next = Node(2)
    print(f'value = {linked_list.value}')
    print(f'value = {linked_list.next.value}')
    print(f'value = {linked_list.next.next.value}')