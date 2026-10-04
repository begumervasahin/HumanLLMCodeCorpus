from balanced_binary_search_tree import Tree
import random as rdn
from chronometer import Chronometer
def measure_time(label, function):
    with Chronometer() as elapsed_time:
        function()
    print(f'{label}: {float(elapsed_time):.5f} seconds')
def insert_nodes(tree, node_count):
    temp = None
    for i in range(node_count):
        value = rdn.randint(1, 100)
        tree.insert_node(value)
        if i == node_count
            temp = value
    return temp
def main():
    tree = Tree()
    node_count = 50
    print("\nInserting nodes...")
    temp = measure_time('Time spent inserting nodes', lambda: insert_nodes(tree, node_count))
    print("\nPerforming in-order traversal...")
    measure_time('Time spent printing in-order traversal', tree.in_order)
    print('\nTree Info:')
    print(f'    Root: {tree.root.info}')
    print(f'    Left Height: {tree.root.left_height}')
    print(f'    Right Height: {tree.root.right_height}')
    print(f'\nSearching for {temp}...')
    measure_time('Time spent on search', lambda: tree.search_node(temp))
    print('\nGetting tree in tuple format...')
    measure_time('Time spent on tuple conversion', tree.print_tree_on_tuple)
    print('\nTree structure:')
    measure_time('Time spent printing the tree', tree.print_tree)
if __name__ == "__main__":
    main()