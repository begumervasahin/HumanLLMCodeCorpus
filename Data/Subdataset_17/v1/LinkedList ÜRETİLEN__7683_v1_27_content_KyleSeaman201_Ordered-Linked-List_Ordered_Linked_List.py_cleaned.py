class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    def getValue(self):
        return self.value
    def getNext(self):
        return self.next
    def setValue(self, new_value):
        self.value = new_value
    def setNext(self, new_next):
        self.next = new_next
    def __str__(self):
        return "{}".format(self.value)
    __repr__ = __str__
class OrderedLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def add(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        elif self.head.value > new_node.value:
            new_node.next = self.head
            self.head = new_node
        elif self.tail.value < new_node.value:
            self.tail.next = new_node
            self.tail = new_node
        else:
            temp = self.head
            while temp.next is not None and temp.next.value < new_node.value:
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
            if new_node.next is None:
                self.tail = new_node
    def delete(self, value):
        if self.head is None:
            return
        if self.head.value == value:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return
        temp = self.head
        while temp.next is not None and temp.next.value != value:
            temp = temp.next
        if temp.next is not None:
            temp.next = temp.next.next
            if temp.next is None:
                self.tail = temp
    def search(self, value):
        temp = self.head
        while temp is not None:
            if temp.value == value:
                return True
            temp = temp.next
        return False
    def pop(self):
        if self.head is None:
            return None
        if self.head == self.tail:
            val = self.head.value
            self.head = None
            self.tail = None
            return val
        temp = self.head
        while temp.next != self.tail:
            temp = temp.next
        val = self.tail.value
        self.tail = temp
        self.tail.next = None
        return val
    def isEmpty(self):
        return self.head is None
    def size(self):
        count = 0
        temp = self.head
        while temp is not None:
            count += 1
            temp = temp.next
        return count
    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.getValue(), end=' ')
            temp = temp.getNext()
        print()
if __name__ == "__main__":
    oll = OrderedLinkedList()
    oll.add(3)
    oll.add(1)
    oll.add(4)
    oll.add(2)
    print("List after adding elements:")
    oll.printList()
    print("Size of list:", oll.size())
    oll.delete(3)
    print("List after deleting 3:")
    oll.printList()
    print("Searching for 4:", oll.search(4))
    print("Searching for 3:", oll.search(3))
    print("Popping the last element:", oll.pop())
    print("List after popping the last element:")
    oll.printList()
    print("Is the list empty?", oll.isEmpty())
    print("Size of list:", oll.size())