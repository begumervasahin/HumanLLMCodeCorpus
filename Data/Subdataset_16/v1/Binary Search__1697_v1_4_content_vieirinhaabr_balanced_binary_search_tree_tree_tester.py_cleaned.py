from balanced_binary_search_tree import Tree
import random as rdn
from chronometer import Chronometer
def fonk1():
    b1 = Tree()
    with Chronometer() as total_time:
        a1 = 50
        a2 = 0
        b2 = None
        with Chronometer() as insert_time:
            while a2 < a1:
                b3 = rdn.randint(1, 100)
                b1.insert_node(b3)
                if a2 = = a1
                    b2 = b3
                a2 += 1
        print('Time spent on insertion: {:.5f} seconds'.format(float(insert_time)))
        with Chronometer() as print_in_order_time:
            print('\nIn-order traversal: ', b4 = '')
            b1.in_order()
        print('\n\nTime spent on in-order traversal: {:.5f} seconds'.format(float(print_in_order_time)))
        print('\nTree Info:')
        print('      Root -> ', b1.root.b3)
        print('      Left height -> ', b1.root.left_height)
        print('      Right height -> ', b1.root.right_height)
        with Chronometer() as search_time:
            print('\nTrying to find ', b2, '...')
            b1.search_node(b2)
        print('Time spent on search: {:.5f} seconds'.format(float(search_time)))
        with Chronometer() as tuple_time:
            print('Getting Tree in tuple format...')
            b5 = b1.print_tree_on_tuple()
            print(b5)
        print('Time spent on converting to tuple format: {:.5f} seconds'.format(float(tuple_time)))
        with Chronometer() as print_tree_time:
            b1.print_tree()
        print('Time spent on printing the tree: {:.5f} seconds'.format(float(print_tree_time)))
    print('\nTotal time for all operations: {:.5f} seconds'.format(float(total_time)))
if b6 = = "__main__":
    fonk1()