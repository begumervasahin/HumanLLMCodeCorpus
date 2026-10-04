class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setNext(self, new_next):
        self.next = new_next
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def isEmpty(self):
        return self.head is None
    def append(self, item):
        temp = Node(item)
        temp.next = self.head
        if self.head is None:
            self.tail = temp
        self.head = temp
        self.size += 1
    def appendSort(self, temp):
        temp.next = None
        current = self.tail
        previous = None
        var = temp.data
        while current is not None:
            if current.data > var:
                break
            else:
                previous = current
                current = current.getNext()
        if previous is None:
            temp.next = self.tail
            self.tail = temp
        else:
            temp.next = current
            previous.next = temp
    def length(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.getNext()
        return count
    def search(self, item):
        current = self.head
        while current is not None:
            if current.getData() == item:
                return True
            current = current.getNext()
        return False
    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
        self.size -= 1
if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)
    print("Search for 20:", linked_list.search(20))
    print("Search for 40:", linked_list.search(40))
    linked_list.remove(20)
    print("Search for 20 after removal:", linked_list.search(20))
    print("Length of the list:", linked_list.length())
