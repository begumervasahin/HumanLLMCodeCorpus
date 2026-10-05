import time
import bst
def fonk1(student_number):
    print(f"\nENTER THE DETAILS OF STUDENT {student_number}:")
    b1 = int(input("Enter the roll number: "))
    b2 = input("Enter b2: ")
    b3 = input("Enter the b3: ")
    b4 = int(input("Enter the mobile number: "))
    b5 = input("Enter the b5: ")
    print('Enter the marks in three subjects:')
    b6 = int(input("First subject: "))
    b7 = int(input("Second subject: "))
    b8 = int(input("Third subject: "))
    b9 = b6 + b7 + b8
    b10 = b9 / 3
    print("Total Marks: ", b9)
    print("Average Marks: ", b10)
    return b1
def fonk2():
    b11 = int(input("Enter the number of students: "))
    b12 = bst.BST()
    for i in range(1, b11 + 1):
        b1 = fonk1(i)
        b12.insert(b1)
    print("\nBST TRAVERSAL\n")
    b12.inorder()
    b13 = input("\nDo you want to delete any keys in the tree? (Enter 'y' or 'Y'): ")
    if b13.lower() == 'y':
        while b13.lower() == 'y':
            b14 = int(input("\nEnter the number to be deleted: "))
            b12.remove(b14)
            b13 = input("Enter 'y' or 'Y' to continue deleting: ")
        print("\nAFTER THE DELETION :\n")
        b12.inorder()
    b15 = input("\nDo you want to search any keys in the tree? (Enter 'y' or 'Y'): ")
    while b15.lower() == 'y':
        b16 = int(input("\nEnter the key to be searched: "))
        b12.search(b16)
        b15 = input("Enter 'y' or 'Y' to continue searching: ")
    print("\n*************************END OF BST OPERATIONS*******************************\n")
if b17 = = '__main__':
    fonk2()