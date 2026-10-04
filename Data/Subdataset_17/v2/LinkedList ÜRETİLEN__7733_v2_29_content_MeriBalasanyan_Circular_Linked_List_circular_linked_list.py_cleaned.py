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
    def find(self, name, ID):
        temp = self.head
        while True:
            if temp.data.name == name and temp.data.ID == ID:
                return temp
            temp = temp.next
            if temp == self.head:
                break
        return None
    def display(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        while True:
            print(f"Name: {temp.data.name}, ID: {temp.data.ID}, GPA: {temp.data.GPA}")
            temp = temp.next
            if temp == self.head:
                break
        print("----------")
    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head
    def append_after(self, prev_name, prev_ID, new_data):
        new_node = Node(new_data)
        prev_node = self.find(prev_name, prev_ID)
        if prev_node is None:
            print("This student is not in the list")
            return
        new_node.next = prev_node.next
        prev_node.next = new_node
    def delete(self, name, ID):
        if self.head is None:
            return
        temp = self.head
        prev = None
        while True:
            if temp.data.name == name and temp.data.ID == ID:
                if prev is not None:
                    prev.next = temp.next
                else:
                    while temp.next != self.head:
                        temp = temp.next
                    temp.next = self.head.next
                    self.head = self.head.next
                return
            prev = temp
            temp = temp.next
            if temp == self.head:
                break
    def reverse(self):
        if self.head is None:
            return
        prev = None
        current = self.head
        next_node = current.next
        while True:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            if current == self.head:
                break
        self.head.next = prev
        self.head = prev
    def change_head(self, new_head_name, new_head_ID):
        new_head = self.find(new_head_name, new_head_ID)
        if new_head is not None:
            self.head = new_head
def main():
    student_list = CircularLinkedList()
    st1 = Student("Meri", "111", "3.0")
    st2 = Student("John", "112", "3.5")
    st3 = Student("Anna", "113", "3.8")
    student_list.append(st1)
    student_list.append(st2)
    student_list.append(st3)
    print("Original list:")
    student_list.display()
    student_list.reverse()
    print("Reversed list:")
    student_list.display()
    st4 = Student("Mike", "114", "3.2")
    student_list.append_after("John", "112", st4)
    print("List after appending Mike after John:")
    student_list.display()
    student_list.delete("Anna", "113")
    print("List after deleting Anna:")
    student_list.display()
    student_list.change_head("Mike", "114")
    print("List after changing head to Mike:")
    student_list.display()
if __name__ == "__main__":
    main()