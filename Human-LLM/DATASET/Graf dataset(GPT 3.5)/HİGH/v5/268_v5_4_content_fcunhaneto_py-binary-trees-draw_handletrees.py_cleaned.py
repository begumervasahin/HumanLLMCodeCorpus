import sys
import binarytree
import avltree
import uteis
b1 = {
    1: "Create binary tree",
    2: "Create AVL tree",
    0: "Exit"
}
b2 = {
    1: "Enter nodes",
    2: "Walk in order",
    3: "Walk pos order",
    4: "Remove node",
    5: "Successor",
    6: "Predecessor",
    0: "Exit"
}
def fonk1(options):
    print("Options:")
    print("***************************")
    for b5, value in options.items():
        print(f"{b5} - {value}")
    print("***************************")
def fonk2(options):
    while True:
        try:
            b3 = int(input("Enter the option: "))
            if b3 in options:
                return b3
            else:
                print("Invalid option. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")
def fonk3(b4 = None):
    uteis.clear()
    if not b4:
        fonk1(b1)
        b3 = fonk2(b1)
        if b3 = = 1:
            b4 = binarytree.BinaryTree()
        elif b3 = = 2:
            b4 = avltree.AVLTree()
        elif b3 = = 0:
            sys.exit(0)
    uteis.clear()
    b3 = None
    while b3 != 0:
        fonk1(b2)
        b3 = fonk2(b2)
        uteis.clear()
        if b3 = = 1:
            fonk4(b4)
        elif b3 = = 2:
            fonk5(b4)
        elif b3 = = 3:
            fonk6(b4)
        elif b3 = = 4:
            fonk7(b4)
        elif b3 = = 5:
            fonk8(b4)
        elif b3 = = 6:
            fonk9(b4)
        elif b3 = = 0:
            sys.exit(0)
def fonk4(b4):
    print("Enter the nodes (enter none to end):")
    print("*********************************************")
    b5 = input("node: ")
    while b5:
        try:
            b5 = int(b5)
            b4.insert(b5)
            b5 = input("node: ")
        except ValueError:
            print("Invalid input. Please enter an integer.")
    print("*********************************************\n")
def fonk5(b4):
    print("Walk In Order:")
    print("node\tparent\tleft\tright\theight\tfb")
    print("***********************************************")
    b4.fonk5()
    print("***********************************************\n")
def fonk6(b4):
    print("Walk In Order:")
    print("node\tparent\tleft\tright\theight\tfb")
    print("***********************************************")
    b4.fonk6()
    print("***********************************************\n")
def fonk7(b4):
    print("***********************************************")
    b5 = input("To remove node enter it's b5: ")
    try:
        b5 = int(b5)
        if b4.remove(b5):
            print(f"Successfully removed {b5}")
        else:
            print(f"Failed to remove {b5}. Make sure it exists on the tree")
    except ValueError:
        print("Invalid input. Please enter an integer.")
    print("***********************************************\n")
def fonk8(b4):
    print("*********************************************************")
    b5 = input("Enter the b5 of the node you want the b6: ")
    try:
        b5 = int(b5)
        b6 = b4.b6(b5)
        if b6:
            print(f"Successor is: {b6.b5}")
        else:
            print("Not found.")
    except ValueError:
        print("Invalid input. Please enter an integer.")
    print("*********************************************************")
def fonk9(b4):
    print("*********************************************************")
    b5 = input("Enter the b5 of the node you want the b7: ")
    try:
        b5 = int(b5)
        b7 = b4.b7(b5)
        if b7:
            print(f"Predecessor is: {b7.b5}")
        else:
            print("Not found.")
    except ValueError:
        print("Invalid input. Please enter an integer.")
    print("*********************************************************")
if b8 = = '__main__':
    fonk3()