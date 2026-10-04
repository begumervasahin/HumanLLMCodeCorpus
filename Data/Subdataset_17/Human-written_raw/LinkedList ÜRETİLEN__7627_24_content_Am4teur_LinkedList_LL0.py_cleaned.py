class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
if(__name__ == "__main__"):
    ll = Node(0)
    ll.next = Node(1)
    ll.next.next = Node(2)
    print(f'value = {ll.value}')
    print(f'value = {ll.next.value}')
    print(f'value = {ll.next.next.value}')