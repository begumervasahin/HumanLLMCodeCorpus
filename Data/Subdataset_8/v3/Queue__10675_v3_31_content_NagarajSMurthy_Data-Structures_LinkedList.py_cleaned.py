class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    def insertNode(self, data):
        new_node = Node(data)
        new_node.nextNode = self.head
        self.head = new_node
        self.size += 1
    def size(self):
        return self.size
    def size2(self):
        current_node = self.head
        size = 0
        while current_node is not None:
            size += 1
            current_node = current_node.nextNode
        return size
    def insertEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.nextNode is not None:
            current_node = current_node.nextNode
        current_node.nextNode = new_node
        self.size += 1
    def traverseList(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.nextNode
    def removeNode(self, data):
        if self.head is None:
            return
        current_node = self.head
        previous_node = None
        while current_node is not None:
            if current_node.data == data:
                if previous_node is None:
                    self.head = current_node.nextNode
                else:
                    previous_node.nextNode = current_node.nextNode
                self.size -= 1
                return
            previous_node = current_node
            current_node = current_node.nextNode
        print('Data not in the linked list')
my_list = LinkedList()
my_list.insertNode(10)
my_list.insertNode(35)
my_list.insertNode(67)
my_list.insertNode(89)
my_list.insertNode(341)
print("The size of the list is " + str(my_list.size()))
print("The size of the list is " + str(my_list.size2()))
my_list.insertEnd(671)
print("The size of the list is " + str(my_list.size2()))
my_list.traverseList()
my_list.removeNode(35)
print("The size of the list is " + str(my_list.size2()))
my_list.traverseList()