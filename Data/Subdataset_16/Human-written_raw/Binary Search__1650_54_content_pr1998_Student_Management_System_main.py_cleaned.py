import time
import bst
def fonk1():
    b1 = int(input("ENTER THE NUMBER OF STUDENTS: \b1"))
    b2 = bst.BST()
    for i in range (b1):
        print("\nENTER THE DETAILS OF STUDENT ",i+1,":")
        b3 = int(input("Enter the roll b14:        "))
        b4 = input("Enter b4:        ")
        b5 = input("Enter the address:        ")
        b6 = int(input("Enter the mobile number:        "))
        b7 = input("Enter the b7:        ")
        print('Enter the marks in three subjects:')
        b8 = int(input("First subject:    "))
        b9 = int(input("Second subject:    "))
        b10 = int(input("Third subject:    "))
        b11 = b8+b9+b10
        b12 = b11/3
        print("Total Marks:   ",b11)
        print("Average marks:   ",b12)
        b2.insert(b3)
    print("\nBST TRAVERSAL\b1")
    b2.inorder()
    print("DO YOU  WANT TO DELETE ANY KEYS IN THE TREE ?")
    print("IF YES ENTER y  OR Y\b1")
    b13 = input()
    if b13 = = 'y' or b13 == 'Y':
        while b13 = = 'y' or b13 == 'Y':
            print("\nEnter the number to be deleted\b1")
            b14 = int(input())
            b2.remove(b14)
            print("Enter y or Y to continue:\b1")
            b13 = input()
        print("AFTER THE DELETION :\b1")
        b2.inorder()
    print("\nDO YOU  WANT TO SEARCH ANY KEYS IN THE TREE ? ")
    print("IF YES ENTER y  OR Y\b1")
    b13 = input()
    while b13 = = 'y' or b13 == 'Y':
        print("\nEnter the b3 to be searched :\b1")
        b14 = int(input())
        b2.search(b14)
        print("Enter y or Y to continue:\b1")
        b13 = input()
    print("\b1*************************END OF BST OPERATIONS*******************************\b1")
if b15 = = '__main__':
	fonk1()