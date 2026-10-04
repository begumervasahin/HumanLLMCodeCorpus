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
        if self.head is not None:
            while count < n:
                if current is None:
                    return
                current = current.next
                count += 1
        while current is not None:
            temp = temp.next
            current = current.next
        if temp is not None:
            print(temp.data)
if __name__ == "__main__":
    llist = LinkedList()
    llist.push(6)
    llist.push(5)
    llist.push(4)
    llist.push(3)
    llist.push(2)
    llist.push(1)
    print("The linked list is:")
    llist.print_list()
    print("\nThe 2nd node from the end is:")
    llist.find_nth_node_from_end(2)