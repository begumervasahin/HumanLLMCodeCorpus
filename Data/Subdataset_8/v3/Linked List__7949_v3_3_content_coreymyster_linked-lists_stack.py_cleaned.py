class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class UnorderedList:
    def __init__(self):
        self.head = None
    def is_empty(self):
        return self.head is None
    def push(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node
    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
    def search(self, item):
        current = self.head
        while current:
            if current.data == item:
                return True
            current = current.next
        return False
    def pop(self):
        if self.head:
            item = self.head.data
            self.head = self.head.next
            return item
        else:
            raise IndexError("Pop from an empty list")
if __name__ == "__main__":
    my_list = UnorderedList()
    my_list.push(80)
    print("Size:", my_list.size())
    my_list.push(3)
    my_list.push(67)
    my_list.push(15)
    print("Size:", my_list.size())
    print("Search for 15:", my_list.search(15))
    my_list.pop()
    print("Size after pop:", my_list.size())
    print("Search for 15 after pop:", my_list.search(15))
    my_list.push(15)
    print("Size after pushing 15 again:", my_list.size())