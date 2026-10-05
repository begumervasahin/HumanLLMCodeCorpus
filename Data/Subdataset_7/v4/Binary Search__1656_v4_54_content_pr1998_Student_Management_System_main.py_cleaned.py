import time
import bst
def fonk1():
    b1 = int(input("Enter the number of students: "))
    b2 = bst.BST()
    for i in range(b1):
        print(f"\nENTER THE DETAILS OF STUDENT {i + 1}:")
        b3 = int(input("Enter the roll number: "))
        b4 = input("Enter b4: ")
        b5 = input("Enter the b5: ")
        b6 = int(input("Enter the mobile number: "))
        b7 = input("Enter the b7: ")
        print('Enter the marks in three subjects:')
        b8 = int(input("First subject: "))
        b9 = int(input("Second subject: "))
        b10 = int(input("Third subject: "))
        b11 = b8 + b9 + b10
        b12 = b11 / 3
        print("Total Marks: ", b11)
        print("Average Marks: ", b12)
        b2.insert(b3)
    print("\nBST TRAVERSAL\n")
    b2.inorder()
    b13 = input("\nDo you want to delete any keys in the tree? (Enter 'y' or 'Y'): ")
    if b13.lower() == 'y':
        while b13.lower() == 'y':
            b14 = int(input("\nEnter the number to be deleted: "))
            b2.remove(b14)
            b13 = input("Enter 'y' or 'Y' to continue deleting: ")
        print("\nAFTER THE DELETION :\n")
        b2.inorder()
    b15 = input("\nDo you want to search any keys in the tree? (Enter 'y' or 'Y'): ")
    while b15.lower() == 'y':
        b16 = int(input("\nEnter the key to be searched: "))
        b2.search(b16)
        b15 = input("Enter 'y' or 'Y' to continue searching: ")
    print("\n*************************END OF BST OPERATIONS*******************************\n")
if b17 = = '__main__':
    fonk1()