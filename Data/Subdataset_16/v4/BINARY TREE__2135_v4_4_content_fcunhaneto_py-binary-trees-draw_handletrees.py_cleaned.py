import sys
import binarytree
import avltree
import uteis
def fonk1(b1 = None):
    uteis.clear()
    if not b1:
        fonk2()
        b2 = fonk4()
        if b2 = = 1:
            b1 = binarytree.BinaryTree()
        elif b2 = = 2:
            b1 = avltree.AVLTree()
        elif b2 = = 0:
            sys.exit(0)
        else:
            fonk5()
            fonk1()
    uteis.clear()
    while True:
        fonk3()
        b2 = fonk4()
        if b2 = = 1:
            fonk6(b1)
        elif b2 = = 2:
            fonk7(b1)
        elif b2 = = 3:
            fonk8(b1)
        elif b2 = = 4:
            fonk9(b1)
        elif b2 = = 5:
            fonk10(b1)
        elif b2 = = 6:
            fonk11(b1)
        elif b2 = = 0:
            sys.exit(0)
        else:
            fonk5()
def fonk2():
    print('***************************')
    print('1 - Create binary tree')
    print('2 - Create AVL tree')
    print('0 - Exit')
    print('***************************')
def fonk3():
    print('Options:')
    print('***************************')
    print('1 - Enter nodes')
    print('2 - Walk in order')
    print('3 - Walk post order')
    print('4 - Remove node')
    print('5 - Successor')
    print('6 - Predecessor')
    print('0 - Exit')
    print('***************************')
def fonk4():
    try:
        return int(input('Enter the option: '))
    except ValueError:
        return None
def fonk5():
    print('Invalid option.')
    input('Press enter to return to options.\n')
def fonk6(b1):
    print('Enter the nodes (enter none to end):')
    print('*********************************************')
    while True:
        b3 = input('node: ')
        if not b3:
            break
        try:
            b3 = int(b3)
            b1.insert(b3)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    print('*********************************************\n')
def fonk7(b1):
    print('Walk In Order:')
    print('node\tparent\tleft\tright\theight\tfb')
    print('***********************************************')
    b1.fonk7()
    print('***********************************************\n')
def fonk8(b1):
    print('Walk Post Order:')
    print('node\tparent\tleft\tright\theight\tfb')
    print('***********************************************')
    b1.fonk8()
    print('***********************************************\n')
def fonk9(b1):
    print('***********************************************')
    try:
        b3 = int(input("To remove node enter its b3: "))
        if b1.remove(b3):
            print(f'Successfully removed {b3}')
        else:
            print(f'Failed to remove {b3}. Make sure it exists in the tree.')
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
    print('***********************************************\n')
def fonk10(b1):
    print('*********************************************************')
    try:
        b3 = int(input("Enter the b3 of the node you want the b4 of: "))
        b4 = b1.b4(b3)
        if b4:
            print(f'Successor is: {b4.b3}')
        else:
            print('Not found.')
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
    print('*********************************************************')
def fonk11(b1):
    print('*********************************************************')
    try:
        b3 = int(input("Enter the b3 of the node you want the b5 of: "))
        b5 = b1.b5(b3)
        if b5:
            print(f'Predecessor is: {b5.b3}')
        else:
            print('Not found.')
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
    print('*********************************************************')
if b6 = = '__main__':
    fonk1()