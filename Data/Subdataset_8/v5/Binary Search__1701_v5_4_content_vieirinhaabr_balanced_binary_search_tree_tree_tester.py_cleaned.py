from balanced_binary_search_tree import Tree
import random as rdn
from chronometer import Chronometer
if __name__ == "__main__":
    tree_control = Tree()
    with Chronometer() as total_time:
        count = 50
        with Chronometer() as insert_time:
            for _ in range(count):
                info = rdn.randint(1, 100)
                tree_control.insert_node(info)
        print(f'Time taken to insert {count} nodes: {insert_time.elapsed_time:.5f} seconds')
        with Chronometer() as traversal_time:
            print('\nIn-order traversal: ', end='')
            tree_control.in_order()
        print(f'\nTime taken for in-order traversal: {traversal_time.elapsed_time:.5f} seconds')
        print('\nTree Info:')
        print('      Root ->', tree_control.root.info)
        print('      Left height ->', tree_control.root.left_height)
        print('      Right height ->', tree_control.root.right_height)
        search_value = tree_control.root.left.right.info
        with Chronometer() as search_time:
            print(f'\nSearching for value {search_value}...')
            tree_control.search_node(search_value)
        print(f'Searching took {search_time.elapsed_time:.5f} seconds')
        with Chronometer() as convert_time:
            print('Getting Tree in tuple format...')
            tuple_tree = tree_control.print_tree_on_tuple()
            print(tuple_tree)
        print(f'Converting to tuple took {convert_time.elapsed_time:.5f} seconds')
        with Chronometer() as print_tree_time:
            tree_control.print_tree()
        print(f'\nPrinting the tree took {print_tree_time.elapsed_time:.5f} seconds')
    print(f'\nTotal time taken for all operations: {total_time.elapsed_time:.5f} seconds')