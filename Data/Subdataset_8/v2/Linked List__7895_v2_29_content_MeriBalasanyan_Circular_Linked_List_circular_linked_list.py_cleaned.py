class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
class Student:
    def __init__(self, name, ID, GPA):
        self.name = name
        self.ID = ID
        self.GPA = GPA
class CircularLinkedList:
    def __init__(self):
        self.head = None
    def find(self, data):
        current = self.head
        while current.data != data:
            current = current.next
            if current == self.head:
                return None
        return current
    def display(self):
        if self.head is None:
            print("List is empty")
            return
        current = self.head
        while True:
            print(f"name: {current.data.name}, ID: {current.data.ID}, GPA: {current.data.GPA}")
            current = current.next
            if current == self.head:
                break
        print("----------")
    def append(self, new_data):
        new_student = Student(new_data.name, new_data.ID, new_data.GPA)
        if self.head is None:
            new_student.next = new_student
            self.head = new_student
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_student
            new_student.next = self.head
    def append_after(self, prev_data, new_data):
        prev_student = self.find(prev_data)
        if prev_student is None:
            print("Previous student not found in the list")
            return
        new_student = Student(new_data.name, new_data.ID, new_data.GPA)
        new_student.next = prev_student.next
        prev_student.next = new_student
    def delete(self, name, ID):
        if self.head is None:
            print("List is empty")
            return
        current = self.head
        if current.data.name == name and current.data.ID == ID:
            while current.next != self.head:
                current = current.next
            current.next = self.head.next
            self.head = self.head.next
            return
        prev = None
        while current.next != self.head:
            prev = current
            current = current.next
            if current.data.name == name and current.data.ID == ID:
                prev.next = current.next
                return
        if current.next == self.head:
            print("Student not found in the list")
    def reverse(self):
        if self.head is None:
            print("List is empty")
            return
        prev = None
        current = self.head
        while current.next != self.head:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        current.next = prev
        self.head.next = current
        self.head = current
    def change_head(self, new_head):
        new_head_node = self.find(new_head)
        if new_head_node is not None:
            self.head = new_head_node
def main():
    student_list = CircularLinkedList()
    st1 = Student("meri", "111", "3.0")
    student_list.append(st1)
    student_list.display()
    student_list.reverse()
    student_list.display()
if __name__ == "__main__":
    main()