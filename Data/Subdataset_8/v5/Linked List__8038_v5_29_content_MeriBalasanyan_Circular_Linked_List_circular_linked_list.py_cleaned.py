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
        self.__head = None
    def find_node(self, name, ID):
        current = self.__head
        while current is not None and (current.data.name != name or current.data.ID != ID):
            current = current.next
            if current == self.__head:
                return None
        return current
    def display(self):
        current = self.__head
        while True:
            print(f"Name: {current.data.name}, ID: {current.data.ID}, GPA: {current.data.GPA}")
            current = current.next
            if current == self.__head:
                break
        print("----------")
    def append(self, new_student):
        new_node = Node(new_student)
        if self.__head is None:
            new_node.next = new_node
            self.__head = new_node
        else:
            current = self.__head
            while current.next != self.__head:
                current = current.next
            current.next = new_node
            new_node.next = self.__head
    def append_after(self, prev_name, prev_ID, new_student):
        prev_node = self.find_node(prev_name, prev_ID)
        if prev_node is None:
            print("Previous student not found in the list")
            return
        new_node = Node(new_student)
        new_node.next = prev_node.next
        prev_node.next = new_node
    def delete(self, name, ID):
        current = self.__head
        prev = None
        while current is not None and (current.data.name != name or current.data.ID != ID):
            prev = current
            current = current.next
            if current == self.__head:
                break
        if current is None:
            print("Student not found in the list")
            return
        if prev is not None:
            prev.next = current.next
        else:
            while current.next != self.__head:
                current = current.next
            current.next = self.__head.next
            self.__head = self.__head.next
    def reverse(self):
        if self.__head is None:
            return
        prev = None
        current = self.__head
        while True:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            if current == self.__head:
                break
        self.__head = prev
    def change_head(self, name, ID):
        new_head = self.find_node(name, ID)
        if new_head is None:
            print("Student not found in the list")
            return
        self.__head = new_head
def main():
    student_list = CircularLinkedList()
    st1 = Student("Meri", "111", "3.0")
    st2 = Student("John", "222", "3.5")
    student_list.append(st1)
    student_list.append(st2)
    student_list.reverse()
    student_list.append_after("Meri", "111", Student("Alice", "333", "4.0"))
    student_list.delete("John", "222")
    student_list.change_head("Alice", "333")
    student_list.reverse()
    student_list.display()
if __name__ == "__main__":
    main()