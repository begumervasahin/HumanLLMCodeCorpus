import sys
from binarytree import BinaryTree
from avltree import AVLTree
import uteis
def handle_trees(tree=None):
    uteis.clear()
    if not tree:
        print('***************************')
        print('1 - Create binary tree')
        print('2 - Create AVL tree')
        print('0 - Exit')
        print('***************************')
        option = input('Enter your choice: ')
        try:
            option = int(option)
        except ValueError:
            print('Invalid option. Please try again.')
            input('Press Enter to return to the options.\n')
            handle_trees()
        if option == 1:
            tree = BinaryTree()
        elif option == 2:
            tree = AVLTree()
        elif option == 0:
            sys.exit(0)
        else:
            print('Invalid option. Please try again.')
            input('Press Enter to continue.')
            handle_trees()
    uteis.clear()
    while True:
        print_options()
        option = get_option()
        if option == 1:
            insert_nodes(tree)
        elif option == 2:
            walk_in_order(tree)
        elif option == 3:
            walk_in_post_order(tree)
        elif option == 4:
            remove_node(tree)
        elif option == 5:
            find_successor(tree)
        elif option == 6:
            find_predecessor(tree)
        elif option == 0:
            sys.exit(0)
        else:
            print('Invalid option. Please try again.')
def print_options():
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
def get_option():
    while True:
        try:
            option = int(input('Enter your choice: '))
            return option
        except ValueError:
            print('Invalid option. Please try again.')
            input('Press Enter to return to the options.\n')
def insert_nodes(tree):
    print('Enter the nodes (enter "none" to end):')
    print('*********************************************')
    while True:
        key = input('Node: ')
        if key.lower() == 'none':
            break
        try:
            key = int(key)
            tree.insert(key)
        except ValueError:
            print('Invalid input. Please enter an integer.')
    print('*********************************************\n')
def walk_in_order(tree):
    print('Walk In Order:')
    print('Node\tParent\tLeft\tRight\tHeight\tFB')
    print('***********************************************')
    tree.walk_in_order()
    print('***********************************************\n')
def walk_in_post_order(tree):
    print('Walk In Post Order:')
    print('Node\tParent\tLeft\tRight\tHeight\tFB')
    print('***********************************************')
    tree.walk_pos_order()
    print('***********************************************\n')
def remove_node(tree):
    print('***********************************************')
    key = input("Enter the key of the node to remove: ")
    try:
        key = int(key)
        if tree.remove(key):
            print('Successfully removed node with key {0}'.format(key))
        else:
            print('Failed to remove node with key {0}. Make sure it exists in the tree'.format(key))
    except ValueError:
        print('Invalid input. Please enter an integer.')
    print('***********************************************\n')
def find_successor(tree):
    print('*********************************************************')
    key = input("Enter the key of the node you want to find the successor for: ")
    try:
        key = int(key)
        successor = tree.successor(key)
        if successor:
            print('Successor node key: {0}'.format(successor.key))
        else:
            print('Successor not found.')
    except ValueError:
        print('Invalid input. Please enter an integer.')
    print('*********************************************************')
def find_predecessor(tree):
    print('*********************************************************')
    key = input("Enter the key of the node you want to find the predecessor for: ")
    try:
        key = int(key)
        predecessor = tree.predecessor(key)
        if predecessor:
            print('Predecessor node key: {0}'.format(predecessor.key))
        else:
            print('Predecessor not found.')
    except ValueError:
        print('Invalid input. Please enter an integer.')
    print('*********************************************************')
if __name__ == '__main__':
    handle_trees()