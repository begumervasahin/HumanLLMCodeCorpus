import sys
import binarytree
import avltree
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
            input('Press enter to return to options.\n')
            handle_trees()
        if op == 1:
            bt = binarytree.BinaryTree()
        elif op == 2:
            bt = avltree.AVLTree()
        elif op == 0:
            exit(0)
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
        print('3 - Walk post order')
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
            input('Press enter to return to options.\n')
            handle_trees(bt)
        uteis.clear()
        if op == 1:
            print('Enter the nodes (enter none to end):')
            print('*********************************************')
            key = input('node: ')
            while key:
                try:
                    key = int(key)
                    bt.insert(key)
                except ValueError:
                    print('Invalid input. Please enter a valid integer.')
                key = input('node: ')
            print('*********************************************\n')
        elif op == 2:
            print('Walk In Order:')
            print('node\tparent\tleft\tright\theight\tfb')
            print('***********************************************')
            bt.walk_in_order()
            print('***********************************************\n')
        elif op == 3:
            print('Walk Post Order:')
            print('node\tparent\tleft\tright\theight\tfb')
            print('***********************************************')
            bt.walk_post_order()
            print('***********************************************\n')
        elif op == 4:
            print('***********************************************')
            try:
                key = int(input("To remove node, enter its key: "))
                if bt.remove(key):
                    print('Successfully removed {0}'.format(key))
                else:
                    print('Failed to remove {0}. Make sure it exists in the tree.'.format(key))
            except ValueError:
                print('Invalid input. Please enter a valid integer.')
            print('***********************************************\n')
        elif op == 5:
            print('*********************************************************')
            try:
                key = int(input("Enter the key of the node for which you want the successor: "))
                successor = bt.successor(key)
                if successor:
                    print('Successor is: {0}'.format(successor.key))
                else:
                    print('Not found.')
            except ValueError:
                print('Invalid input. Please enter a valid integer.')
            print('*********************************************************')
        elif op == 6:
            print('*********************************************************')
            try:
                key = int(input("Enter the key of the node for which you want the predecessor: "))
                predecessor = bt.predecessor(key)
                if predecessor:
                    print('Predecessor is: {0}'.format(predecessor.key))
                else:
                    print('Not found.')
            except ValueError:
                print('Invalid input. Please enter a valid integer.')
            print('*********************************************************')
        elif op == 0:
            sys.exit(0)
        else:
            print('Invalid option.')
            input('Press enter to return to options.\n')
if __name__ == '__main__':
    handle_trees()