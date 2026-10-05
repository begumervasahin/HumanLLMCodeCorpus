class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    def getValue(self):
        return self.value
    def getNext(self):
        return self.next
    def setValue(self,new_value):
        self.value = new_value
    def setNext(self,new_next):
        self.next = new_next
    def __str__(self):
        return ("{}".format(self.value))
    __repr__ = __str__
class OrderedLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.count=0
    def add(self, value):
        new_node= Node(value)
        if self.head== None:
            self.head= new_node
            self.tail= new_node
        elif self.head.value > new_node.value:
            new_node.next= self.head
            self.head= new_node
        elif self.tail.value < new_node.value:
            self.tail.next= new_node
            self.tail= new_node
        else:
            temp= self.head
            while temp.value < new_node.value:
                prev= temp
                temp= temp.next
            prev.next= new_node
            new_node.next= temp
    def delete(self, value):
        if self.head.value== value:
            self.head= self.head.next
        elif self.tail.value== value:
            temp= self.head
            while temp.next!= self.tail:
                temp= temp.next
            self.tail= temp
            self.tail.next= None
        else:
            temp= self.head
            while temp.value!= value:
                prev= temp
                temp= temp.next
            prev.next= temp.next
            temp.next= None
    def search(self,value):
        temp= self.head
        while temp != None:
            if temp.value == value:
                return True
            temp= temp.next
        return False
    def pop(self):
        val= self.tail.value
        temp= self.head
        while temp.next!= self.tail:
            temp= temp.next
        self.tail= temp
        self.tail.next= None
        return val
    def isEmpty(self):
        if self.head== None:
            return True
        else:
            return False
    def size(self):
        count= 0
        temp= self.head
        while temp!= None:
            count+=1
            temp= temp.next
        return count
    def printList(self):
        temp=self.head
        while temp:
            print(temp.getValue(), end=' ')
            temp=temp.getNext()