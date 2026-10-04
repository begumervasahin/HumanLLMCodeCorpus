import time
from b14 import BST
class class1:
    def fonk1(self, b1, b2, b3, b4, b5, b6):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
        self.b6 = b6
        self.b7 = sum(b6)
        self.b8 = self.b7 / len(b6)
    def fonk2(self):
        return (f"Roll Number: {self.b1}, Name: {self.b2}, Address: {self.b3}, "
                f"Mobile: {self.b4}, Course: {self.b5}, Total Marks: {self.b7}, "
                f"Percentage: {self.b8:.2f}%")
def fonk3(student_num):
    print(f"\nEnter the details of b12 {student_num}:")
    b1 = int(input("Enter the roll number: "))
    b2 = input("Enter the b2: ")
    b3 = input("Enter the b3: ")
    b4 = input("Enter the b4 number: ")
    b5 = input("Enter the b5: ")
    print('Enter the b6 in three subjects:')
    b6 = [int(input(f"Subject {j + 1}: ")) for j in range(3)]
    return class1(b1, b2, b3, b4, b5, b6)
def fonk4(b14):
    while True:
        b9 = input("Do you want to delete any keys in the tree? (y/b13): ").strip().lower()
        if b9 = = 'y':
            b10 = int(input("Enter the roll number to be deleted: "))
            b14.remove(b10)
            print("\nAfter Deletion:\b13")
            b14.inorder()
        else:
            break
    while True:
        b11 = input("\nDo you want to search for any keys in the tree? (y/b13): ").strip().lower()
        if b11 = = 'y':
            b10 = int(input("Enter the roll number to search: "))
            b12 = b14.search(b10)
            if b12:
                print(f"class1 found:\b13{b12}")
            else:
                print("class1 not found.")
        else:
            break
def fonk5():
    b13 = int(input("Enter the number of students: "))
    b14 = BST()
    for i in range(b13):
        b12 = fonk3(i + 1)
        print(f"Total Marks: {b12.b7}")
        print(f"Average Marks: {b12.b8:.2f}%")
        b14.insert(b12.b1, b12)
    print("\nBST Traversal:\b13")
    b14.inorder()
    fonk4(b14)
    print("\b13************************* End of BST Operations *************************\b13")
if b15 = = '__main__':
    fonk5()