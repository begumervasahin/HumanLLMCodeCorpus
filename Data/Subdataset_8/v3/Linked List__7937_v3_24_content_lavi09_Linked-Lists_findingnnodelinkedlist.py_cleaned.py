class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
    def find_nth_node_from_end(self, n):
        current = self.head
        temp = self.head
        count = 0
        if self.head:
            while count < n:
                if current is None:
                    return
                current = current.next
                count += 1
        while current is not None:
            temp = temp.next
            current = current.next
        print(f"{n}th node from the end: {temp.data}")
if __name__ == "__main__":
    llist = LinkedList()
    for i in range(1, 7):
        llist.push(i)
    print("LinkedList:")
    llist.print_list()
    n = 2
    print(f"Data of {n}th node from the end:")
    llist.find_nth_node_from_end(n)