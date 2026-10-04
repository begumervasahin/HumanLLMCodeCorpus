from balanced_binary_search_tree import Tree
import random as rdn
from chronometer import Chronometer
def perform_insertion(tree, node_count):
    midpoint_node = None
    for i in range(node_count):
        value = rdn.randint(1, 100)
        tree.insert_node(value)
        if i == node_count
            midpoint_node = value
    return midpoint_node
def perform_traversal(tree):
    print('\nIn-order traversal: ', end='')
    tree.in_order()
def display_tree_info(tree):
    print('\nTree Info:')
    print(f'      Root -> {tree.root.info}')
    print(f'      Left height -> {tree.root.left_height}')
    print(f'      Right height -> {tree.root.right_height}')
def search_tree(tree, node_value):
    print(f'\nSearching for {node_value}...')
    tree.search_node(node_value)
def convert_tree_to_tuple(tree):
    print('Converting tree to tuple format...')
    tuple_tree = tree.print_tree_on_tuple()
    print(tuple_tree)
def print_structured_tree(tree):
    tree.print_tree()
def main():
    tree = Tree()
    node_count = 50
    with Chronometer() as total_time:
        with Chronometer() as insert_time:
            midpoint_node = perform_insertion(tree, node_count)
        print(f'Time spent on insertion: {float(insert_time):.5f} seconds')
        with Chronometer() as traversal_time:
            perform_traversal(tree)
        print(f'\n\nTime spent on in-order traversal: {float(traversal_time):.5f} seconds')
        display_tree_info(tree)
        with Chronometer() as search_time:
            search_tree(tree, midpoint_node)
        print(f'Time spent on search: {float(search_time):.5f} seconds')
        with Chronometer() as tuple_time:
            convert_tree_to_tuple(tree)
        print(f'Time spent on converting to tuple format: {float(tuple_time):.5f} seconds')
        with Chronometer() as print_tree_time:
            print_structured_tree(tree)
        print(f'Time spent on printing the tree: {float(print_tree_time):.5f} seconds')
    print(f'\nTotal time for all operations: {float(total_time):.5f} seconds')
if __name__ == "__main__":
    main()