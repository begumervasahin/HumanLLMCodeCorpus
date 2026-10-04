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
    return {
        "b1": b1,
        "b2": b2,
        "b3": b3,
        "b4": b4,
        "b5": b5,
        "b7": b7,
        "b8": b8
    }
def fonk2(b12, b13):
    for i in range(b13):
        print(f"\nEnter the details of Student {i + 1}:")
        b9 = fonk1()
        b12.insert(b9["b1"])
def fonk3(b12):
    while True:
        b10 = int(input("Enter the roll number to delete: "))
        b12.remove(b10)
        if input("Do you want to delete another key? (y/n): ").lower() != 'y':
            break
    print("\nAfter deletion, BST In-Order Traversal:\n")
    b12.inorder()
def fonk4(b12):
    while True:
        b11 = int(input("Enter the roll number to search: "))
        b12.search(b11)
        if input("Do you want to search another key? (y/n): ").lower() != 'y':
            break
def fonk5():
    b12 = bst.BST()
    b13 = int(input("Enter the number of students: "))
    fonk2(b12, b13)
    print("\nBST In-Order Traversal:\n")
    b12.inorder()
    if input("Do you want to delete any keys in the tree? (y/n): ").lower() == 'y':
        fonk3(b12)
    if input("Do you want to search any keys in the tree? (y/n): ").lower() == 'y':
        fonk4(b12)
    print("\n************************* END OF BST OPERATIONS *******************************\n")
if b14 = = '__main__':
    fonk5()