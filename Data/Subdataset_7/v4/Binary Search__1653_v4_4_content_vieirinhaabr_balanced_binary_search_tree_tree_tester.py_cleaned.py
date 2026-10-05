
from balanced_binary_search_tree import Tree
import random as rdn
from chronometer import Chronometer
if b1 = = "__main__":
    b2 = Tree()
    with Chronometer() as time:
        a1 = 0
        a2 = 50
        with Chronometer() as t:
            while a1 < a2:
                b3 = rdn.randint(1, 100)
                b2.insert_node(b3)
                if a1 = = a2 / 2:
                    b4 = b3
                a1 += 1
        print('To insert, it took {:.5f} seconds'.format(float(t)))
        with Chronometer() as t:
            print('\nIn-order traversal: ', b5 = '')
            b2.in_order()
        print('\n\nTo print in-order, it took {:.5f} seconds'.format(float(t)))
        print('\nTree Info: ')
        print('      root -> ', b2.root.b3)
        print('      Left height -> ', b2.root.left_height)
        print('      Right height -> ', b2.root.right_height)
        with Chronometer() as t:
            print('\nTrying to find ', b4, '...')
            b2.search_node(b4)
        print('    Searching took {:.5f} seconds'.format(float(t)))
        print('\n')
        with Chronometer() as t:
            print('Getting Tree in tuple format...')
            b6 = b2.print_tree_on_tuple()
            print(b6)
        print('    Converting to tuple took {:.5f} seconds'.format(float(t)))
        print('\n')
        with Chronometer() as t:
            b2.print_tree()
        print('\nPrinting the tree took {:.5f} seconds'.format(float(t)))
    print('\n\nTotal time taken: {:.5f} seconds'.format(float(time)))