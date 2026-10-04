import time
from bst import BST
class Student:
    def __init__(self, roll_num, name, address, mobile, course, marks):
        self.roll_num = roll_num
        self.name = name
        self.address = address
        self.mobile = mobile
        self.course = course
        self.marks = marks
        self.total = sum(marks)
        self.percent = self.total / len(marks)
    def __str__(self):
        return (f"Roll Number: {self.roll_num}, Name: {self.name}, Address: {self.address}, "
                f"Mobile: {self.mobile}, Course: {self.course}, Total Marks: {self.total}, "
                f"Percentage: {self.percent:.2f}%")
def main():
    n = int(input("Enter the number of students: "))
    bst = BST()
    for i in range(n):
        print(f"\nEnter the details of student {i + 1}:")
        roll_num = int(input("Enter the roll number: "))
        name = input("Enter the name: ")
        address = input("Enter the address: ")
        mobile = input("Enter the mobile number: ")
        course = input("Enter the course: ")
        print('Enter the marks in three subjects:')
        marks = [int(input(f"Subject {j + 1}: ")) for j in range(3)]
        student = Student(roll_num, name, address, mobile, course, marks)
        print(f"Total Marks: {student.total}")
        print(f"Average Marks: {student.percent:.2f}%")
        bst.insert(roll_num, student)
    print("\nBST Traversal:\n")
    bst.inorder()
    delete_choice = input("Do you want to delete any keys in the tree? (y/n): ").strip().lower()
    while delete_choice == 'y':
        num = int(input("Enter the roll number to be deleted: "))
        bst.remove(num)
        delete_choice = input("Delete another key? (y/n): ").strip().lower()
    print("\nAfter Deletion:\n")
    bst.inorder()
    search_choice = input("\nDo you want to search for any keys in the tree? (y/n): ").strip().lower()
    while search_choice == 'y':
        num = int(input("Enter the roll number to search: "))
        student = bst.search(num)
        if student:
            print(f"Student found:\n{student}")
        else:
            print("Student not found.")
        search_choice = input("Search for another key? (y/n): ").strip().lower()
    print("\n************************* End of BST Operations *************************\n")
if __name__ == '__main__':
    main()