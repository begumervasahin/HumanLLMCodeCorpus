import time
from bst import BST
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
    b9 = int(input("ENTER THE NUMBER OF STUDENTS: \b9"))
    b10 = BST()
    for i in range(b9):
        print(f"\nENTER THE DETAILS OF STUDENT {i+1}:")
        b1 = int(input("Enter the roll number: "))
        b2 = input("Enter b2: ")
        b3 = input("Enter the b3: ")
        b4 = int(input("Enter the b4 number: "))
        b5 = input("Enter the b5: ")
        print('Enter the b6 in three subjects:')
        b6 = []
        b6.append(int(input("First subject: ")))
        b6.append(int(input("Second subject: ")))
        b6.append(int(input("Third subject: ")))
        b11 = class1(b1, b2, b3, b4, b5, b6)
        print("Total Marks: ", b11.b7)
        print("Average b6: ", b11.b8)
        b10.insert(b1, b11)
    print("\nBST TRAVERSAL\b9")
    b10.inorder()
    print("DO YOU WANT TO DELETE ANY KEYS IN THE TREE?")
    b12 = input("IF YES, ENTER y OR Y: ")
    if b12.lower() == 'y':
        while b12.lower() == 'y':
            b13 = int(input("Enter the number to be deleted: "))
            b10.remove(b13)
            b12 = input("Enter y or Y to continue: ")
        print("AFTER THE DELETION:\b9")
        b10.inorder()
    print("\nDO YOU WANT TO SEARCH ANY KEYS IN THE TREE?")
    b12 = input("IF YES, ENTER y OR Y: ")
    while b12.lower() == 'y':
        b13 = int(input("Enter the key to be searched: "))
        b14 = b10.search(b13)
        if b14:
            print(f"class1 found: {b14}")
        else:
            print("class1 not found.")
        b12 = input("Enter y or Y to continue: ")
    print("\b9*************************END OF BST OPERATIONS*******************************\b9")
if b15 = = '__main__':
    fonk3()