class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
        self.dataList = []
    def insert_node(self, data):
        self.size += 1
        self.dataList.append(data)
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            new_node.nextNode = self.head
            self.head = new_node
    def get_size(self):
        return self.size
    def calculate_size(self):
        actual_node = self.head
        size = 0
        while actual_node:
            size += 1
            actual_node = actual_node.nextNode
        return size
    def insert_end(self, data):
        self.size += 1
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        actual_node = self.head
        while actual_node.nextNode:
            actual_node = actual_node.nextNode
        actual_node.nextNode = new_node
    def traverse_list(self):
        actual_node = self.head
        while actual_node:
            print(f"{actual_node.data}")
            actual_node = actual_node.nextNode
    def remove_node(self, data):
        if not self.head:
            return
        if data not in self.dataList:
            print('Data not in the linked list')
            return
        self.size -= 1
        self.dataList.remove(data)
        current_node = self.head
        previous_node = None
        while current_node:
            if current_node.data == data:
                if not previous_node:
                    self.head = current_node.nextNode
                else:
                    previous_node.nextNode = current_node.nextNode
                return
            previous_node = current_node
            current_node = current_node.nextNode
def main():
    my_list = LinkedList()
    my_list.insert_node(10)
    my_list.insert_node(35)
    my_list.insert_node(67)
    my_list.insert_node(89)
    my_list.insert_node(341)
    print("Initial size of the list:", my_list.get_size())
    print("Calculated size of the list:", my_list.calculate_size())
    my_list.insert_end(671)
    print("Size of the list after inserting at the end:", my_list.calculate_size())
    print("Traversing the list:")
    my_list.traverse_list()
    my_list.remove_node(20)
    print("Size of the list after attempting to remove 20:", my_list.calculate_size())
    print("Traversing the list after removal attempt:")
    my_list.traverse_list()
if __name__ == "__main__":
    main()