import sys
import binarytree
import avltree
import uteis
def handle_trees(bt=None):
    uteis.clear()
    if not bt:
        bt = create_tree()
        if not bt:
            return
    uteis.clear()
    while True:
        display_tree_menu()
        op = get_option()
        if op == 1:
            enter_nodes(bt)
        elif op == 2:
            walk_in_order(bt)
        elif op == 3:
            walk_post_order(bt)
        elif op == 4:
            remove_node(bt)
        elif op == 5:
            find_successor(bt)
        elif op == 6:
            find_predecessor(bt)
        elif op == 0:
            sys.exit(0)
        else:
            invalid_option()
def create_tree():
    display_initial_menu()
    op = get_option()
    if op == 1:
        return binarytree.BinaryTree()
    elif op == 2:
        return avltree.AVLTree()
    elif op == 0:
        sys.exit(0)
    else:
        invalid_option()
        return create_tree()
def display_initial_menu():
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
def get_option():
    try:
        return int(input('Enter the option: '))
    except ValueError:
        return None
def invalid_option():
    print('Invalid option.')
    input('Press enter to return to options.\n')
def enter_nodes(bt):
    print('Enter the nodes (enter none to end):')
    print('*********************************************')
    while True:
        key = input('Node: ').strip()
        if not key:
            break
        try:
            key = int(key)
            bt.insert(key)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    print('*********************************************\n')
def walk_in_order(bt):
    print('Walk In Order:')
    print('Node\tParent\tLeft\tRight\tHeight\tFB')
    print('***********************************************')
    bt.walk_in_order()
    print('***********************************************\n')
def walk_post_order(bt):
    print('Walk Post Order:')
    print('Node\tParent\tLeft\tRight\tHeight\tFB')
    print('***********************************************')
    bt.walk_post_order()
    print('***********************************************\n')
def remove_node(bt):
    print('***********************************************')
    try:
        key = int(input("To remove node, enter its key: "))
        if bt.remove(key):
            print(f'Successfully removed {key}')
        else:
            print(f'Failed to remove {key}. Make sure it exists in the tree.')
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
    print('***********************************************\n')
def find_successor(bt):
    print('*********************************************************')
    try:
        key = int(input("Enter the key of the node you want the successor of: "))
        successor = bt.successor(key)
        if successor:
            print(f'Successor is: {successor.key}')
        else:
            print('Not found.')
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
    print('*********************************************************')
def find_predecessor(bt):
    print('*********************************************************')
    try:
        key = int(input("Enter the key of the node you want the predecessor of: "))
        predecessor = bt.predecessor(key)
        if predecessor:
            print(f'Predecessor is: {predecessor.key}')
        else:
            print('Not found.')
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
    print('*********************************************************')
if __name__ == '__main__':
    handle_trees()