from balanced_binary_search_tree import Tree
import random as rdn
from chronometer import Chronometer
if b1 = = "__main__":
    b2 = Tree()
    with Chronometer() as total_time:
        a1 = 50
        with Chronometer() as insert_time:
            for _ in range(a1):
                b3 = rdn.randint(1, 100)
                b2.insert_node(b3)
        print(f'Time taken to insert {a1} nodes: {insert_time.elapsed_time:.5f} seconds')
        with Chronometer() as traversal_time:
            print('\nIn-order traversal: ', b4 = '')
            b2.in_order()
        print(f'\nTime taken for in-order traversal: {traversal_time.elapsed_time:.5f} seconds')
        print('\nTree Info:')
        print('      Root ->', b2.root.b3)
        print('      Left height ->', b2.root.left_height)
        print('      Right height ->', b2.root.right_height)
        b5 = b2.root.left.right.b3
        with Chronometer() as search_time:
            print(f'\nSearching for value {b5}...')
            b2.search_node(b5)
        print(f'Searching took {search_time.elapsed_time:.5f} seconds')
        with Chronometer() as convert_time:
            print('Getting Tree in tuple format...')
            b6 = b2.print_tree_on_tuple()
            print(b6)
        print(f'Converting to tuple took {convert_time.elapsed_time:.5f} seconds')
        with Chronometer() as print_tree_time:
            b2.print_tree()
        print(f'\nPrinting the tree took {print_tree_time.elapsed_time:.5f} seconds')
    print(f'\nTotal time taken for all operations: {total_time.elapsed_time:.5f} seconds')