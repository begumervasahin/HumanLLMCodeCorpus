class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self, newdata):
        self.data = newdata
    def setNext(self, newnext):
        self.next = newnext
class UnorderedList:
    def __init__(self):
        self.head = None
    def isEmpty(self):
        return self.head == None
    def push(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count
    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found
    def pop(self):
        current = self.head
        previous = None
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
mylist = UnorderedList()
mylist.push(80)
print(mylist.size())
mylist.push(3)
mylist.push(67)
mylist.push(15)
print(mylist.size())
print(mylist.search(15))
mylist.pop()
print(mylist.size())
print(mylist.search(15))
mylist.push(15)
print(mylist.size())