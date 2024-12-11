import sys
from binarytree import BinaryTree
from avltree import AVLTree
import uteis
def fonk1(b1 = None):
    uteis.clear()
    if not b1:
        print('***************************')
        print('1 - Create binary b1')
        print('2 - Create AVL b1')
        print('0 - Exit')
        print('***************************')
        b2 = input('Enter your choice: ')
        try:
            b2 = int(b2)
        except ValueError:
            print('Invalid b2. Please try again.')
            input('Press Enter to return to the options.\n')
            fonk1()
        if b2 = = 1:
            b1 = BinaryTree()
        elif b2 = = 2:
            b1 = AVLTree()
        elif b2 = = 0:
            sys.exit(0)
        else:
            print('Invalid b2. Please try again.')
            input('Press Enter to continue.')
            fonk1()
    uteis.clear()
    while True:
        print('Options:')
        print('***************************')
        print('1 - Insert nodes')
        print('2 - Walk in order')
        print('3 - Walk in post order')
        print('4 - Remove node')
        print('5 - Successor')
        print('6 - Predecessor')
        print('0 - Exit')
        print('***************************')
        print()
        b2 = input('Enter your choice: ')
        try:
            b2 = int(b2)
        except ValueError:
            print('Invalid b2. Please try again.')
            input('Press Enter to return to the options.\n')
            continue
        uteis.clear()
        if b2 = = 1:
            print('Enter the nodes (enter "none" to end):')
            print('*********************************************')
            while True:
                b3 = input('Node: ')
                if b3.lower() == 'none':
                    break
                try:
                    b3 = int(b3)
                except ValueError:
                    print('Invalid input. Please enter an integer.')
                    continue
                b1.insert(b3)
            print('*********************************************\n')
        elif b2 = = 2:
            print('Walk In Order:')
            print('Node\tParent\tLeft\tRight\tHeight\tFB')
            print('***********************************************')
            b1.walk_in_order()
            print('***********************************************\n')
        elif b2 = = 3:
            print('Walk In Post Order:')
            print('Node\tParent\tLeft\tRight\tHeight\tFB')
            print('***********************************************')
            b1.walk_pos_order()
            print('***********************************************\n')
        elif b2 = = 4:
            print('***********************************************')
            b3 = input("Enter the b3 of the node to remove: ")
            try:
                b3 = int(b3)
            except ValueError:
                print('Invalid input. Please enter an integer.')
                continue
            if b1.remove(b3):
                print('Successfully removed node with b3 {0}'.format(b3))
            else:
                print('Failed to remove node with b3 {0}. Make sure it exists in the b1'.format(b3))
            print('***********************************************\n')
        elif b2 = = 5:
            print('*********************************************************')
            b3 = input("Enter the b3 of the node you want to find the b4 for: ")
            try:
                b3 = int(b3)
            except ValueError:
                print('Invalid input. Please enter an integer.')
                continue
            b4 = b1.b4(b3)
            if b4:
                print('Successor node b3: {0}'.format(b4.b3))
            else:
                print('Successor not found.')
            print('*********************************************************')
        elif b2 = = 6:
            print('*********************************************************')
            b3 = input("Enter the b3 of the node you want to find the b5 for: ")
            try:
                b3 = int(b3)
            except ValueError:
                print('Invalid input. Please enter an integer.')
                continue
            b5 = b1.b5(b3)
            if b5:
                print('Predecessor node b3: {0}'.format(b5.b3))
            else:
                print('Predecessor not found.')
            print('*********************************************************')
        elif b2 = = 0:
            sys.exit(0)
        else:
            print('Invalid b2. Please try again.')
if b6 = = '__main__':
    fonk1()