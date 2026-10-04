
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
    def printlist(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
    def findnnode(self,n):
        current=self.head
        temp=self.head
        count=0
        if self.head!=None:
            while(count<n):
                if current is None:
                    return
                current=current.next
                count+=1
        while current is not None:
            temp=temp.next
            current=current.next
        print(temp.data)
llist=LinkedList()
llist.push(6)
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)
llist.printlist()
llist.findnnode(2)