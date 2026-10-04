import time
import bst
def fonk1():
    b1 = int(input("Enter the roll number: "))
    b2 = input("Enter the b2: ")
    b3 = input("Enter the b3: ")
    b4 = int(input("Enter the b4 number: "))
    b5 = input("Enter the b5: ")
    print("Enter the b6 in three subjects:")
    b6 = [int(input(f"Subject {i + 1}: ")) for i in range(3)]
    b7 = sum(b6)
    b8 = b7 / 3
    print(f"Total Marks: {b7}")
    print(f"Average Marks: {b8:.2f}")
    return b1, b2, b3, b4, b5, b7, b8
def fonk2():
    b9 = bst.BST()
    b10 = int(input("Enter the number of students: "))
    for i in range(b10):
        print(f"\nEnter the details of Student {i + 1}:")
        b11 = fonk1()
        b9.insert(b11[0])
    print("\nBST In-Order Traversal:\n")
    b9.inorder()
    if input("Do you want to delete any keys in the tree? (y/n): ").lower() == 'y':
        while True:
            b12 = int(input("Enter the roll number to delete: "))
            b9.remove(b12)
            if input("Do you want to delete another key? (y/n): ").lower() != 'y':
                break
        print("\nAfter deletion, BST In-Order Traversal:\n")
        b9.inorder()
    if input("Do you want to search any keys in the tree? (y/n): ").lower() == 'y':
        while True:
            b13 = int(input("Enter the roll number to search: "))
            b9.search(b13)
            if input("Do you want to search another key? (y/n): ").lower() != 'y':
                break
    print("\n************************* END OF BST OPERATIONS *******************************\n")
if b14 = = '__main__':
    fonk2()