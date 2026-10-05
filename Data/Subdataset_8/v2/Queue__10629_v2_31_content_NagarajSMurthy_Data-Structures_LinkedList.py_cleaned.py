class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
        self.dataList = []
    def insertNode(self, data):
        self.size += 1
        self.dataList.append(data)
        newNode = Node(data)
        if not self.head:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode
    def size(self):
        return self.size
    def size2(self):
        actualNode = self.head
        size = 0
        while actualNode is not None:
            size += 1
            actualNode = actualNode.nextNode
        return size
    def insertEnd(self, data):
        self.size += 1
        newNode = Node(data)
        actualNode = self.head
        while actualNode.nextNode is not None:
            actualNode = actualNode.nextNode
        actualNode.nextNode = newNode
    def traverseList(self):
        actualNode = self.head
        while actualNode is not None:
            print("%d\n" % actualNode.data)
            actualNode = actualNode.nextNode
    def removeNode(self, data):
        if self.head is None:
            return
        if data not in self.dataList:
            print('Data not in the linked list')
            return
        self.size -= 1
        currentNode = self.head
        previousNode = None
        try:
            while currentNode.data != data:
                previousNode = currentNode
                currentNode = currentNode.nextNode
            if previousNode is None:
                self.head = currentNode.nextNode
            else:
                previousNode.nextNode = currentNode.nextNode
        except AttributeError:
            pass
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