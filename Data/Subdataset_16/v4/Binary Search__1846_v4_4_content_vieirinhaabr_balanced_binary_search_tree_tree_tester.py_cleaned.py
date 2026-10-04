from balanced_binary_search_tree import Tree
import random as rdn
from chronometer import Chronometer
def fonk1():
    b1 = Tree()
    a1 = 50
    b2 = None
    with Chronometer() as total_time:
        with Chronometer() as insert_time:
            for b4 in range(a1):
                b3 = rdn.randint(1, 100)
                b1.insert_node(b3)
                if b4 = = a1
                    b2 = b3
        print(f'Time spent inserting nodes: {float(insert_time):.5f} seconds')
        with Chronometer() as in_order_time:
            print('\nIn-order traversal: ', b5 = '')
            b1.in_order()
        print(f'\nTime spent printing in-order traversal: {float(in_order_time):.5f} seconds')
        print('\nTree Info:')
        print(f'    Root: {b1.root.info}')
        print(f'    Left Height: {b1.root.left_height}')
        print(f'    Right Height: {b1.root.right_height}')
        with Chronometer() as search_time:
            print(f'\nSearching for {b2}...')
            b1.search_node(b2)
        print(f'Time spent on search: {float(search_time):.5f} seconds')
        with Chronometer() as tuple_time:
            print('\nGetting b1 in tuple format...')
            b6 = b1.print_tree_on_tuple()
            print(b6)
        print(f'Time spent on tuple conversion: {float(tuple_time):.5f} seconds')
        with Chronometer() as print_time:
            print('\nTree structure:')
            b1.print_tree()
        print(f'Time spent printing the b1: {float(print_time):.5f} seconds')
    print(f'\nTotal time for all operations: {float(total_time):.5f} seconds')
if b7 = = "__main__":
    fonk1()