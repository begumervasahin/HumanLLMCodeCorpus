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
        while temp:
            if temp.data.name == name and temp.data.ID == ID:
                return temp
            temp = temp.next
            if temp == self.head:
                break
        return None
    def display(self):
        if self.head is None:
            print("List is empty.")
            return
        temp = self.head
        while True:
            print(f"name: {temp.data.name}, ID: {temp.data.ID}, GPA: {temp.data.GPA}")
            temp = temp.next
            if temp == self.head:
                break
        print("----------")
    def append(self, new_student):
        new_node = Node(new_student)
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head
    def append_after(self, prev_student_name, prev_student_ID, new_student):
        new_node = Node(new_student)
        prev_node = self.find(prev_student_name, prev_student_ID)
        if prev_node is None:
            print("This student is not in the list.")
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
                if prev:
                    prev.next = temp.next
                else:
                    cur = self.head
                    while cur.next != self.head:
                        cur = cur.next
                    if self.head == self.head.next:
                        self.head = None
                    else:
                        cur.next = self.head.next
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
        start = self.head
        while True:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            if current == start:
                break
        self.head.next = prev
        self.head = prev
    def change_head(self, name, ID):
        new_head = self.find(name, ID)
        if new_head:
            self.head = new_head
def main():
    student_list = CircularLinkedList()
    st1 = Student("meri", "111", "3.0")
    student_list.append(st1)
    st2 = Student("john", "112", "3.5")
    student_list.append(st2)
    st3 = Student("doe", "113", "3.8")
    student_list.append(st3)
    print("Original List:")
    student_list.display()
    student_list.reverse()
    print("Reversed List:")
    student_list.display()
    st4 = Student("jane", "114", "3.7")
    student_list.append_after("john", "112", st4)
    print("After Appending Jane after John:")
    student_list.display()
    student_list.delete("meri", "111")
    print("After Deleting Meri:")
    student_list.display()
    student_list.change_head("jane", "114")
    print("After Changing Head to Jane:")
    student_list.display()
if __name__ == "__main__":
    main()