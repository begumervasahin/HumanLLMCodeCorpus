import sys
import binarytree
import avltree
import uteis
def fonk1():
    print('***************************')
    print('1 - Create binary tree')
    print('2 - Create AVL tree')
    print('0 - Exit')
    print('***************************')
def fonk2():
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
def fonk3():
    try:
        return int(input('Enter the b1: '))
    except ValueError:
        print('Invalid b1. Please enter a number.')
        return None
def fonk4():
    while True:
        fonk1()
        b1 = fonk3()
        if b1 = = 1:
            return binarytree.BinaryTree()
        elif b1 = = 2:
            return avltree.AVLTree()
        elif b1 = = 0:
            sys.exit(0)
        else:
            print('Invalid b1.')
            input('Press enter to return to options.')
def fonk5(b5):
    print('Enter the nodes (enter none to end):')
    print('*********************************************')
    while True:
        b2 = input('node: ')
        if b2 = = '':
            break
        try:
            b5.insert(int(b2))
        except ValueError:
            print('Invalid input. Please enter a valid integer.')
    print('*********************************************\n')
def fonk6(b5):
    print('Walk In Order:')
    print('node\tparent\tleft\tright\theight\tfb')
    print('***********************************************')
    b5.walk_in_order()
    print('***********************************************\n')
def fonk7(b5):
    print('Walk Post Order:')
    print('node\tparent\tleft\tright\theight\tfb')
    print('***********************************************')
    b5.walk_post_order()
    print('***********************************************\n')
def fonk8(b5):
    print('***********************************************')
    try:
        b2 = int(input("To remove node, enter its b2: "))
        if b5.remove(b2):
            print(f'Successfully removed {b2}')
        else:
            print(f'Failed to remove {b2}. Make sure it exists in the tree.')
    except ValueError:
        print('Invalid input. Please enter a valid integer.')
    print('***********************************************\n')
def fonk9(b5):
    print('*********************************************************')
    try:
        b2 = int(input("Enter the b2 of the node for which you want the b3: "))
        b3 = b5.b3(b2)
        if b3:
            print(f'Successor is: {b3.b2}')
        else:
            print('Not found.')
    except ValueError:
        print('Invalid input. Please enter a valid integer.')
    print('*********************************************************')
def fonk10(b5):
    print('*********************************************************')
    try:
        b2 = int(input("Enter the b2 of the node for which you want the b4: "))
        b4 = b5.b4(b2)
        if b4:
            print(f'Predecessor is: {b4.b2}')
        else:
            print('Not found.')
    except ValueError:
        print('Invalid input. Please enter a valid integer.')
    print('*********************************************************')
def fonk11(b5 = None):
    uteis.clear()
    if not b5:
        b5 = fonk4()
    uteis.clear()
    while True:
        fonk2()
        b1 = fonk3()
        uteis.clear()
        if b1 = = 1:
            fonk5(b5)
        elif b1 = = 2:
            fonk6(b5)
        elif b1 = = 3:
            fonk7(b5)
        elif b1 = = 4:
            fonk8(b5)
        elif b1 = = 5:
            fonk9(b5)
        elif b1 = = 6:
            fonk10(b5)
        elif b1 = = 0:
            sys.exit(0)
        else:
            print('Invalid b1.')
            input('Press enter to return to options.\n')
if b6 = = '__main__':
    fonk11()