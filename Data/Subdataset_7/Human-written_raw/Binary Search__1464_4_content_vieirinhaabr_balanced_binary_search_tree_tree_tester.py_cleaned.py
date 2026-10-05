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
                b3 = rdn.randint(1,100)
                b2.insert_node(b3)
                if a1 = = a2/2:
                    b4 = b3
                a1 = a1 + 1
        print('To insert spend {:.5f} seconds'.format(float(t)))
        with Chronometer() as t:
            print('\nin order: ', b5 = '')
            b2.in_order()
        print('\n\nTo print spend {:.5f} seconds'.format(float(t)))
        print('\nTree Info: ')
        print('      root -> ', b2.root.b3)
        print('      Left height -> ', b2.root.left_height)
        print('      Right height -> ', b2.root.right_height)
        with Chronometer() as t:
            print('\nTrying to find ', b4, '...')
            b2.search_node(b4)
        print('    Was spend {:.5f} seconds on this search'.format(float(t)))
        print('\n')
        with Chronometer() as t:
            print('Getting Tree on tuple format...')
            b6 = b2.print_tree_on_tuple()
            print(b6)
        print('    Was spend {:.5f} seconds in this operation'.format(float(t)))
        print('\n')
        with Chronometer() as t:
            b2.print_tree()
        print('\nWas spend {:.5f} seconds in this operation'.format(float(t)))
    print('\n\nWas spend {:.5f} seconds to execute all operations/commands'.format(float(time)))