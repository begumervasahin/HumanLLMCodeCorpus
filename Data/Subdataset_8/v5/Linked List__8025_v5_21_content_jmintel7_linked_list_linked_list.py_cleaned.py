class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = Node()
    def append(self, data):
        new_node = Node(data)
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    def length(self):
        current = self.head
        total = 0
        while current.next:
            current = current.next
            total += 1
        return total
    def display_images(self):
        current = self.head
        images = []
        while current.next:
            if current.data:
                images.append(current.data[0])
            current = current.next
        return images
    def get_student_by_rollno(self, rollno):
        current = self.head
        while current.next:
            current = current.next
            data = current.data
            if data.rollno == rollno:
                return data
        print('Student with the roll number does not exist')
        return None
    def erase_student(self, rollno):
        current = self.head
        while current.next:
            last_node = current
            current = current.next
            data = current.data
            if data.rollno == rollno:
                last_node.next = current.next
                print('Record erased')
                return
        print('Student with the roll number does not exist')
    def get_image(self, index):
        if index >= self.length():
            print('ERROR: Index out of range')
            return None
        current = self.head
        for _ in range(index + 1):
            current = current.next
        return current.data
    def erase_image(self, index):
        if index >= self.length():
            print('ERROR: Index out of range')
            return None
        current = self.head
        for _ in range(index + 1):
            last_node = current
            current = current.next
        last_node.next = current.next