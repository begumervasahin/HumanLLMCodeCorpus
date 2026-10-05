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
    def find(self, data):
        temp = self.__head
        while temp.data != data:
            temp = temp.next
            if temp == self.__head:
                return None
        return temp
    def display(self):
        if self.__head is None:
            print("List is empty")
            return
        printval = self.__head
        while True:
            print("name:", printval.data.name, "ID:", printval.data.ID, "GPA:", printval.data.GPA)
            printval = printval.next
            if printval == self.__head:
                break
        print("----------")
    def append(self, newdata):
        newStudent = Student(newdata.name, newdata.ID, newdata.GPA)
        if self.__head is None:
            newStudent.next = newStudent
            self.__head = newStudent
        else:
            temp = self.__head
            while temp.next != self.__head:
                temp = temp.next
            temp.next = newStudent
            newStudent.next = self.__head
    def appendAfter(self, prevStudent, newStudent):
        prev_Student = self.find(prevStudent)
        if prev_Student is None:
            print("Previous student not found in the list")
            return
        new_Student = Student(newStudent.name, newStudent.ID, newStudent.GPA)
        new_Student.next = prev_Student.next
        prev_Student.next = new_Student
    def delete(self, name, ID):
        if self.__head is None:
            print("List is empty")
            return
        temp = self.__head
        if temp.data.name == name and temp.data.ID == ID:
            while temp.next != self.__head:
                temp = temp.next
            temp.next = self.__head.next
            self.__head = self.__head.next
            return
        prev = None
        while temp.next != self.__head:
            prev = temp
            temp = temp.next
            if temp.data.name == name and temp.data.ID == ID:
                prev.next = temp.next
                return
        if temp.next == self.__head:
            print("Student not found in the list")
    def reverse(self):
        if self.__head is None:
            print("List is empty")
            return
        prev = None
        current = self.__head
        while current.next != self.__head:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        current.next = prev
        self.__head.next = current
        self.__head = current
    def changehead(self, newhead):
        new_head = self.find(newhead)
        if new_head is not None:
            self.__head = new_head
def main():
    student_list = CircularLinkedList()
    st1 = Student("meri", "111", "3.0")
    student_list.append(st1)
    student_list.display()
    student_list.reverse()
    student_list.display()
if __name__ == "__main__":
    main()