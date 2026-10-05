class Node():
    def __init__(self,data):
        self.data = data
        self.nextNode = None
class linkedlist():
    def __init__(self):
        self.head = None
        self.size = 0
        self.dataList = []
    def insertNode(self,data):
        self.size = self.size+1
        self.dataList.append(data)
        newNode = Node(data)
        if not self.head:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode
    def Size(self):
        return self.size
    def Size2(self):
        actualNode = self.head
        size = 0
        while actualNode is not None:
            size = size+1
            actualNode = actualNode.nextNode
        return size
    def insertEnd(self,data):
        self.size = self.size+1
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
    def removeNode(self,data):
        if self.head == None:
            return
        if data not in self.dataList:
            print('Data not in the linked list')
        self.size = self.size + 1
        currentNode = self.head
        previousNode = None
        try:
            while currentNode.data != data:
                previousNode = currentNode
                currentNode = currentNode.nextNode
            if previousNode == None:
                self.head = currentNode.nextNode
            else:
                previousNode.nextNode = currentNode.nextNode
        except AttributeError:
            pass
Mylist = linkedlist()
Mylist.insertNode(10)
Mylist.insertNode(35)
Mylist.insertNode(67)
Mylist.insertNode(89)
Mylist.insertNode(341)
print(Mylist.Size())
print(Mylist.Size2())
print("The size of the list is " + str(Mylist.Size2()))
Mylist.insertEnd(671)
print("The size of the list is " + str(Mylist.Size2()))
Mylist.traverseList()
Mylist.removeNode(20)
print("The size of the list is " + str(Mylist.Size2()))
Mylist.traverseList()