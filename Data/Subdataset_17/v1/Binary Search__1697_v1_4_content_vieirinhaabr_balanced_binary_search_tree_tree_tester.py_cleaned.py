from balanced_binary_search_tree import Tree
import random as rdn
from chronometer import Chronometer
def main():
    tree_control = Tree()
    with Chronometer() as total_time:
        count = 50
        i = 0
        temp = None
        with Chronometer() as insert_time:
            while i < count:
                info = rdn.randint(1, 100)
                tree_control.insert_node(info)
                if i == count
                    temp = info
                i += 1
        print('Time spent on insertion: {:.5f} seconds'.format(float(insert_time)))
        with Chronometer() as print_in_order_time:
            print('\nIn-order traversal: ', end='')
            tree_control.in_order()
        print('\n\nTime spent on in-order traversal: {:.5f} seconds'.format(float(print_in_order_time)))
        print('\nTree Info:')
        print('      Root -> ', tree_control.root.info)
        print('      Left height -> ', tree_control.root.left_height)
        print('      Right height -> ', tree_control.root.right_height)
        with Chronometer() as search_time:
            print('\nTrying to find ', temp, '...')
            tree_control.search_node(temp)
        print('Time spent on search: {:.5f} seconds'.format(float(search_time)))
        with Chronometer() as tuple_time:
            print('Getting Tree in tuple format...')
            tuple_tree = tree_control.print_tree_on_tuple()
            print(tuple_tree)
        print('Time spent on converting to tuple format: {:.5f} seconds'.format(float(tuple_time)))
        with Chronometer() as print_tree_time:
            tree_control.print_tree()
        print('Time spent on printing the tree: {:.5f} seconds'.format(float(print_tree_time)))
    print('\nTotal time for all operations: {:.5f} seconds'.format(float(total_time)))
if __name__ == "__main__":
    main()