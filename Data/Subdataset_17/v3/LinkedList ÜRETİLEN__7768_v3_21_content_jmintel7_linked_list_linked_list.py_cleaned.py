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
        while cur_node.next:
            cur_node = cur_node.next
        cur_node.next = new_node
    def length(self):
        cur_node = self.head
        total = 0
        while cur_node.next:
            cur_node = cur_node.next
            total += 1
        return total
    def display_images(self):
        images = []
        cur_node = self.head
        while cur_node.next:
            cur_node = cur_node.next
            if cur_node.data:
                images.append(cur_node.data[0])
        return images
    def get_student_by_rollno(self, rollno):
        cur_node = self.head
        while cur_node.next:
            cur_node = cur_node.next
            if cur_node.data[1] == rollno:
                return cur_node.data
        print('Student with the roll number does not exist')
        return None
    def erase_by_rollno(self, rollno):
        cur_node = self.head
        while cur_node.next:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_node.data[1] == rollno:
                last_node.next = cur_node.next
                print('Record erased')
                return
        print('Student with the roll number does not exist')
    def get_image_by_index(self, index):
        if index >= self.length():
            print('ERROR: Index out of range')
            return None
        cur_node = self.head
        for _ in range(index + 1):
            cur_node = cur_node.next
        return cur_node.data
    def erase_image_by_index(self, index):
        if index >= self.length():
            print('ERROR: Index out of range')
            return None
        cur_node = self.head
        for _ in range(index + 1):
            last_node = cur_node
            cur_node = cur_node.next
        last_node.next = cur_node.next
if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.append(("image1.jpg", 101))
    linked_list.append(("image2.jpg", 102))
    linked_list.append(("image3.jpg", 103))
    print("List of images:")
    print(linked_list.display_images())
    print("\nGet image by index 1:")
    print(linked_list.get_image_by_index(1))
    print("\nErase image by index 1:")
    linked_list.erase_image_by_index(1)
    print("List of images after erasing:")
    print(linked_list.display_images())
    print("\nErase student by roll number 103:")
    linked_list.erase_by_rollno(103)
    print("List of images after erasing student with roll number 103:")
    print(linked_list.display_images())
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
        while cur_node.next:
            cur_node = cur_node.next
        cur_node.next = new_node
    def length(self):
        cur_node = self.head
        total = 0
        while cur_node.next:
            cur_node = cur_node.next
            total += 1
        return total
    def display_images(self):
        images = []
        cur_node = self.head
        while cur_node.next:
            cur_node = cur_node.next
            if cur_node.data:
                images.append(cur_node.data[0])
        return images
    def get_student_by_rollno(self, rollno):
        cur_node = self.head
        while cur_node.next:
            cur_node = cur_node.next
            if cur_node.data[1] == rollno:
                return cur_node.data
        print('Student with the roll number does not exist')
        return None
    def erase_by_rollno(self, rollno):
        cur_node = self.head
        while cur_node.next:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_node.data[1] == rollno:
                last_node.next = cur_node.next
                print('Record erased')
                return
        print('Student with the roll number does not exist')
    def get_image_by_index(self, index):
        if index >= self.length():
            print('ERROR: Index out of range')
            return None
        cur_node = self.head
        for _ in range(index + 1):
            cur_node = cur_node.next
        return cur_node.data
    def erase_image_by_index(self, index):
        if index >= self.length():
            print('ERROR: Index out of range')
            return None
        cur_node = self.head
        for _ in range(index + 1):
            last_node = cur_node
            cur_node = cur_node.next
        last_node.next = cur_node.next
if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.append(("image1.jpg", 101))
    linked_list.append(("image2.jpg", 102))
    linked_list.append(("image3.jpg", 103))
    print("List of images:")
    print(linked_list.display_images())
    print("\nGet image by index 1:")
    print(linked_list.get_image_by_index(1))
    print("\nErase image by index 1:")
    linked_list.erase_image_by_index(1)
    print("List of images after erasing:")
    print(linked_list.display_images())
    print("\nErase student by roll number 103:")
    linked_list.erase_by_rollno(103)
    print("List of images after erasing student with roll number 103:")
    print(linked_list.display_images())