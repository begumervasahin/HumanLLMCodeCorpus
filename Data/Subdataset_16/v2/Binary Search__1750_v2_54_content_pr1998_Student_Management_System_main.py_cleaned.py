import time
from b10 import BST
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
def fonk3():
    b9 = int(input("Enter the number of students: "))
    b10 = BST()
    for i in range(b9):
        print(f"\nEnter the details of b11 {i + 1}:")
        b1 = int(input("Enter the roll number: "))
        b2 = input("Enter the b2: ")
        b3 = input("Enter the b3: ")
        b4 = input("Enter the b4 number: ")
        b5 = input("Enter the b5: ")
        print('Enter the b6 in three subjects:')
        b6 = [int(input(f"Subject {j + 1}: ")) for j in range(3)]
        b11 = class1(b1, b2, b3, b4, b5, b6)
        print(f"Total Marks: {b11.b7}")
        print(f"Average Marks: {b11.b8:.2f}%")
        b10.insert(b1, b11)
    print("\nBST Traversal:\b9")
    b10.inorder()
    b12 = input("Do you want to delete any keys in the tree? (y/b9): ").strip().lower()
    while b12 = = 'y':
        b13 = int(input("Enter the roll number to be deleted: "))
        b10.remove(b13)
        b12 = input("Delete another key? (y/b9): ").strip().lower()
    print("\nAfter Deletion:\b9")
    b10.inorder()
    b14 = input("\nDo you want to search for any keys in the tree? (y/b9): ").strip().lower()
    while b14 = = 'y':
        b13 = int(input("Enter the roll number to search: "))
        b11 = b10.search(b13)
        if b11:
            print(f"class1 found:\b9{b11}")
        else:
            print("class1 not found.")
        b14 = input("Search for another key? (y/b9): ").strip().lower()
    print("\b9************************* End of BST Operations *************************\b9")
if b15 = = '__main__':
    fonk3()