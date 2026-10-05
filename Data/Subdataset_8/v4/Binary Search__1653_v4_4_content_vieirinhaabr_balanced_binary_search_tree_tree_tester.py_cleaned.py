
from balanced_binary_search_tree import Tree
import random as rdn
from chronometer import Chronometer
if __name__ == "__main__":
    tree_control = Tree()
    with Chronometer() as time:
        i = 0
        count = 50
        with Chronometer() as t:
            while i < count:
                info = rdn.randint(1, 100)
                tree_control.insert_node(info)
                if i == count / 2:
                    temp = info
                i += 1
        print('To insert, it took {:.5f} seconds'.format(float(t)))
        with Chronometer() as t:
            print('\nIn-order traversal: ', end='')
            tree_control.in_order()
        print('\n\nTo print in-order, it took {:.5f} seconds'.format(float(t)))
        print('\nTree Info: ')
        print('      root -> ', tree_control.root.info)
        print('      Left height -> ', tree_control.root.left_height)
        print('      Right height -> ', tree_control.root.right_height)
        with Chronometer() as t:
            print('\nTrying to find ', temp, '...')
            tree_control.search_node(temp)
        print('    Searching took {:.5f} seconds'.format(float(t)))
        print('\n')
        with Chronometer() as t:
            print('Getting Tree in tuple format...')
            tuple_tree = tree_control.print_tree_on_tuple()
            print(tuple_tree)
        print('    Converting to tuple took {:.5f} seconds'.format(float(t)))
        print('\n')
        with Chronometer() as t:
            tree_control.print_tree()
        print('\nPrinting the tree took {:.5f} seconds'.format(float(t)))
    print('\n\nTotal time taken: {:.5f} seconds'.format(float(time)))