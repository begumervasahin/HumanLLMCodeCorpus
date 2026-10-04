import sys
import binarytree
import avltree
import uteis
def fonk1():
    b1 = (
        "***************************\n"
        "1 - Create binary tree\n"
        "2 - Create AVL tree\n"
        "0 - Exit\n"
        "***************************"
    )
    print(b1)
def fonk2():
    b1 = (
        "Options:\n"
        "***************************\n"
        "1 - Enter nodes\n"
        "2 - Walk in order\n"
        "3 - Walk post order\n"
        "4 - Remove node\n"
        "5 - Successor\n"
        "6 - Predecessor\n"
        "0 - Exit\n"
        "***************************"
    )
    print(b1)
def fonk3(b2 = 'Enter the b3: '):
    try:
        return int(input(b2))
    except ValueError:
        print('Invalid b3. Please enter a number.')
        return None
def fonk4():
    while True:
        fonk1()
        b3 = fonk3()
        if b3 = = 1:
            return binarytree.BinaryTree()
        elif b3 = = 2:
            return avltree.AVLTree()
        elif b3 = = 0:
            sys.exit(0)
        else:
            print('Invalid b3.')
            input('Press enter to return to options.')
def fonk5(b7):
    print('Enter the nodes (press Enter without typing to end):')
    print('*********************************************')
    while True:
        b4 = input('node: ')
        if b4 = = '':
            break
        try:
            b7.insert(int(b4))
        except ValueError:
            print('Invalid input. Please enter a valid integer.')
    print('*********************************************\n')
def fonk6(b7):
    print('Walk In Order:')
    print('node\tparent\tleft\tright\theight\tfb')
    print('***********************************************')
    b7.walk_in_order()
    print('***********************************************\n')
def fonk7(b7):
    print('Walk Post Order:')
    print('node\tparent\tleft\tright\theight\tfb')
    print('***********************************************')
    b7.walk_post_order()
    print('***********************************************\n')
def fonk8(b7):
    print('***********************************************')
    try:
        b4 = int(input("To remove node, enter its b4: "))
        if b7.remove(b4):
            print(f'Successfully removed {b4}')
        else:
            print(f'Failed to remove {b4}. Make sure it exists in the tree.')
    except ValueError:
        print('Invalid input. Please enter a valid integer.')
    print('***********************************************\n')
def fonk9(b7):
    print('*********************************************************')
    try:
        b4 = int(input("Enter the b4 of the node for which you want the b5: "))
        b5 = b7.b5(b4)
        if b5:
            print(f'Successor is: {b5.b4}')
        else:
            print('Not found.')
    except ValueError:
        print('Invalid input. Please enter a valid integer.')
    print('*********************************************************')
def fonk10(b7):
    print('*********************************************************')
    try:
        b4 = int(input("Enter the b4 of the node for which you want the b6: "))
        b6 = b7.b6(b4)
        if b6:
            print(f'Predecessor is: {b6.b4}')
        else:
            print('Not found.')
    except ValueError:
        print('Invalid input. Please enter a valid integer.')
    print('*********************************************************')
def fonk11(b7 = None):
    uteis.clear()
    if not b7:
        b7 = fonk4()
    uteis.clear()
    while True:
        fonk2()
        b3 = fonk3()
        uteis.clear()
        if b3 = = 1:
            fonk5(b7)
        elif b3 = = 2:
            fonk6(b7)
        elif b3 = = 3:
            fonk7(b7)
        elif b3 = = 4:
            fonk8(b7)
        elif b3 = = 5:
            fonk9(b7)
        elif b3 = = 6:
            fonk10(b7)
        elif b3 = = 0:
            sys.exit(0)
        else:
            print('Invalid b3.')
            input('Press enter to return to options.\n')
if b8 = = '__main__':
    fonk11()