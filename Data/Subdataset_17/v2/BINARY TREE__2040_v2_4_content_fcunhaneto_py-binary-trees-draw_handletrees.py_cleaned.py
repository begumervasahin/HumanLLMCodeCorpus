import sys
import binarytree
import avltree
import uteis
def display_main_menu():
    print('***************************')
    print('1 - Create binary tree')
    print('2 - Create AVL tree')
    print('0 - Exit')
    print('***************************')
def display_tree_menu():
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
def get_user_option():
    try:
        return int(input('Enter the option: '))
    except ValueError:
        print('Invalid option. Please enter a number.')
        return None
def create_tree():
    while True:
        display_main_menu()
        option = get_user_option()
        if option == 1:
            return binarytree.BinaryTree()
        elif option == 2:
            return avltree.AVLTree()
        elif option == 0:
            sys.exit(0)
        else:
            print('Invalid option.')
            input('Press enter to return to options.')
def handle_node_insertion(bt):
    print('Enter the nodes (enter none to end):')
    print('*********************************************')
    while True:
        key = input('node: ')
        if key == '':
            break
        try:
            bt.insert(int(key))
        except ValueError:
            print('Invalid input. Please enter a valid integer.')
    print('*********************************************\n')
def handle_in_order_walk(bt):
    print('Walk In Order:')
    print('node\tparent\tleft\tright\theight\tfb')
    print('***********************************************')
    bt.walk_in_order()
    print('***********************************************\n')
def handle_post_order_walk(bt):
    print('Walk Post Order:')
    print('node\tparent\tleft\tright\theight\tfb')
    print('***********************************************')
    bt.walk_post_order()
    print('***********************************************\n')
def handle_node_removal(bt):
    print('***********************************************')
    try:
        key = int(input("To remove node, enter its key: "))
        if bt.remove(key):
            print(f'Successfully removed {key}')
        else:
            print(f'Failed to remove {key}. Make sure it exists in the tree.')
    except ValueError:
        print('Invalid input. Please enter a valid integer.')
    print('***********************************************\n')
def handle_successor(bt):
    print('*********************************************************')
    try:
        key = int(input("Enter the key of the node for which you want the successor: "))
        successor = bt.successor(key)
        if successor:
            print(f'Successor is: {successor.key}')
        else:
            print('Not found.')
    except ValueError:
        print('Invalid input. Please enter a valid integer.')
    print('*********************************************************')
def handle_predecessor(bt):
    print('*********************************************************')
    try:
        key = int(input("Enter the key of the node for which you want the predecessor: "))
        predecessor = bt.predecessor(key)
        if predecessor:
            print(f'Predecessor is: {predecessor.key}')
        else:
            print('Not found.')
    except ValueError:
        print('Invalid input. Please enter a valid integer.')
    print('*********************************************************')
def handle_trees(bt=None):
    uteis.clear()
    if not bt:
        bt = create_tree()
    uteis.clear()
    while True:
        display_tree_menu()
        option = get_user_option()
        uteis.clear()
        if option == 1:
            handle_node_insertion(bt)
        elif option == 2:
            handle_in_order_walk(bt)
        elif option == 3:
            handle_post_order_walk(bt)
        elif option == 4:
            handle_node_removal(bt)
        elif option == 5:
            handle_successor(bt)
        elif option == 6:
            handle_predecessor(bt)
        elif option == 0:
            sys.exit(0)
        else:
            print('Invalid option.')
            input('Press enter to return to options.\n')
if __name__ == '__main__':
    handle_trees()