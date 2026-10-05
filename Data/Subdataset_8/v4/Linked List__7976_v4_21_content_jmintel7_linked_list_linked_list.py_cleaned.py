class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = Node()
    def append(self, data):
        new_node = Node(data)
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
        cur_node.next = new_node
    def length(self):
        cur_node = self.head
        total = 0
        while cur_node.next is not None:
            cur_node = cur_node.next
            total += 1
        return total
    def display_image(self):
        cur_node = self.head
        images = []
        count = 0
        while cur_node.next is not None:
            if cur_node.data:
                images.append(cur_node.data[0])
            cur_node = cur_node.next
        return images
    def get_rollno(self, rollno):
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
            data = cur_node.data
            if data.rollno == rollno:
                return data
        print('Student with the roll no does not exist')
        return None
    def erase(self, rollno):
        cur_node = self.head
        while cur_node.next is not None:
            last_node = cur_node
            cur_node = cur_node.next
            data = cur_node.data
            if data.rollno == rollno:
                last_node.next = cur_node.next
                print('Record erased')
                return
        print('Student with the roll no does not exist')
    def get_image(self, index):
        if index >= self.length():
            print('ERROR: Index out of range')
            return None
        cur_node = self.head
        for i in range(index + 1):
            cur_node = cur_node.next
        return cur_node.data
    def erase_image(self, index):
        if index >= self.length():
            print('ERROR: Index out of range')
            return None
        cur_node = self.head
        for i in range(index + 1):
            last_node = cur_node
            cur_node = cur_node.next
        last_node.next = cur_node.next