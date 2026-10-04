import sys
import binarytree
import avltree
import uteis
def fonk1(b1 = None):
    uteis.clear()
    if not b1:
        print('***************************')
        print('1 - Create binary tree')
        print('2 - Create avl tree')
        print('0 - Exit')
        print('***************************')
        b2 = input('Enter the option: ')
        try:
            b2 = int(b2)
        except ValueError:
            print('Invalid option.')
            input('Press enter to return to options.\n')
            fonk1()
        if b2 = = 1:
            b1 = binarytree.BinaryTree()
        elif b2 = = 2:
            b1 = avltree.AVLTree()
        elif b2 = = 0:
            exit(0)
        else:
            print('Invalid option.')
            input('Press enter to continue.')
            fonk1()
    uteis.clear()
    while True:
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
        print()
        b2 = input('Enter the option: ')
        try:
            b2 = int(b2)
        except ValueError:
            print('Invalid option.')
            input('Press enter to return to options.\n')
            fonk1(b1)
        uteis.clear()
        if b2 = = 1:
            print('Enter the nodes (enter none to end):')
            print('*********************************************')
            b3 = input('node: ')
            while b3:
                try:
                    b3 = int(b3)
                    b1.insert(b3)
                except ValueError:
                    print('Invalid input. Please enter a valid integer.')
                b3 = input('node: ')
            print('*********************************************\n')
        elif b2 = = 2:
            print('Walk In Order:')
            print('node\tparent\tleft\tright\theight\tfb')
            print('***********************************************')
            b1.walk_in_order()
            print('***********************************************\n')
        elif b2 = = 3:
            print('Walk Post Order:')
            print('node\tparent\tleft\tright\theight\tfb')
            print('***********************************************')
            b1.walk_post_order()
            print('***********************************************\n')
        elif b2 = = 4:
            print('***********************************************')
            try:
                b3 = int(input("To remove node, enter its b3: "))
                if b1.remove(b3):
                    print('Successfully removed {0}'.format(b3))
                else:
                    print('Failed to remove {0}. Make sure it exists in the tree.'.format(b3))
            except ValueError:
                print('Invalid input. Please enter a valid integer.')
            print('***********************************************\n')
        elif b2 = = 5:
            print('*********************************************************')
            try:
                b3 = int(input("Enter the b3 of the node for which you want the b4: "))
                b4 = b1.b4(b3)
                if b4:
                    print('Successor is: {0}'.format(b4.b3))
                else:
                    print('Not found.')
            except ValueError:
                print('Invalid input. Please enter a valid integer.')
            print('*********************************************************')
        elif b2 = = 6:
            print('*********************************************************')
            try:
                b3 = int(input("Enter the b3 of the node for which you want the b5: "))
                b5 = b1.b5(b3)
                if b5:
                    print('Predecessor is: {0}'.format(b5.b3))
                else:
                    print('Not found.')
            except ValueError:
                print('Invalid input. Please enter a valid integer.')
            print('*********************************************************')
        elif b2 = = 0:
            sys.exit(0)
        else:
            print('Invalid option.')
            input('Press enter to return to options.\n')
if b6 = = '__main__':
    fonk1()