import sys
from binarytree import BinaryTree
from avltree import AVLTree
import uteis
def handle_trees(bt=None):
    uteis.clear()
    if not bt:
        print('***************************')
        print('1 - Create binary tree')
        print('2 - Create avl tree')
        print('0 - Exit')
        print('***************************')
        op = input('Enter the option: ')
        try:
            op = int(op)
        except ValueError:
            print('Invalid option.')
            input('Press enter to return for options.\n')
            handle_trees()
        if op == 1:
            bt = BinaryTree()
        elif op == 2:
            bt = AVLTree()
        elif op == 0:
            sys.exit(0)
        else:
            print('Invalid option.')
            input('Press enter to continue.')
            handle_trees()
    uteis.clear()
    while True:
        print('Options:')
        print('***************************')
        print('1 - Enter nodes')
        print('2 - Walk in order')
        print('3 - Walk pos order')
        print('4 - Remove node')
        print('5 - Successor')
        print('6 - Predecessor')
        print('0 - Exit')
        print('***************************')
        print()
        op = input('Enter the option: ')
        try:
            op = int(op)
        except ValueError:
            print('Invalid option.')
            input('Press enter to return for options.\n')
            continue
        uteis.clear()
        if op == 1:
            print('Enter the nodes (enter none to end):')
            print('*********************************************')
            while True:
                key = input('node: ')
                if key.lower() == 'none':
                    break
                try:
                    key = int(key)
                except ValueError:
                    print('Invalid input. Please enter an integer.')
                    continue
                bt.insert(key)
            print('*********************************************\n')
        elif op == 2:
            print('Walk In Order:')
            print('node\tparent\tleft\tright\theight\tfb')
            print('***********************************************')
            bt.walk_in_order()
            print('***********************************************\n')
        elif op == 3:
            print('Walk In Order:')
            print('node\tparent\tleft\tright\theight\tfb')
            print('***********************************************')
            bt.walk_pos_order()
            print('***********************************************\n')
        elif op == 4:
            print('***********************************************')
            key = input("To remove node enter its key: ")
            try:
                key = int(key)
            except ValueError:
                print('Invalid input. Please enter an integer.')
                continue
            if bt.remove(key):
                print('Successfully removed {0}'.format(key))
            else:
                print('Failed to remove {0}. Make sure it exists on the tree'.format(key))
            print('***********************************************\n')
        elif op == 5:
            print('*********************************************************')
            key = input("Enter the key of the node you want the successor: ")
            try:
                key = int(key)
            except ValueError:
                print('Invalid input. Please enter an integer.')
                continue
            successor = bt.successor(key)
            if successor:
                print('Successor is: {0}'.format(successor.key))
            else:
                print('Not found.')
            print('*********************************************************')
        elif op == 6:
            print('*********************************************************')
            key = input("Enter the key of the node you want the predecessor: ")
            try:
                key = int(key)
            except ValueError:
                print('Invalid input. Please enter an integer.')
                continue
            predecessor = bt.predecessor(key)
            if predecessor:
                print('Predecessor is: {0}'.format(predecessor.key))
            else:
                print('Not found.')
            print('*********************************************************')
        elif op == 0:
            sys.exit(0)
        else:
            print('Invalid option.')
if __name__ == '__main__':
    handle_trees()