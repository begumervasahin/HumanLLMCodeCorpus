
import random
from balanced_binary_search_tree import Tree
from chronometer import Chronometer
if b1 = = "__main__":
    b2 = Tree()
    with Chronometer() as time:
        a1 = 50
        with Chronometer() as t_insert:
            for _ in range(a1):
                b3 = random.randint(1, 100)
                b2.insert_node(b3)
            print(f'Time taken to insert {a1} nodes: {t_insert.elapsed_time:.5f} seconds')
        with Chronometer() as t_inorder:
            print('\nIn order traversal: ', b4 = '')
            b2.in_order()
            print(f'\nTime taken to print in order: {t_inorder.elapsed_time:.5f} seconds')
        print('\nTree Info: ')
        print('      Root -> ', b2.root.b3)
        print('      Left height -> ', b2.root.left_height)
        print('      Right height -> ', b2.root.right_height)
        b5 = random.randint(1, 100)
        with Chronometer() as t_search:
            print(f'\nSearching for {b5}...')
            b2.search_node(b5)
            print(f'Time taken to search for {b5}: {t_search.elapsed_time:.5f} seconds')
        with Chronometer() as t_tuple:
            print('\nGetting Tree in tuple format...')
            b6 = b2.print_tree_on_tuple()
            print(b6)
            print(f'Time taken to print tree in tuple format: {t_tuple.elapsed_time:.5f} seconds')
        with Chronometer() as t_visual:
            print('\nPrinting Tree:')
            b2.print_tree()
            print(f'Time taken to print tree visually: {t_visual.elapsed_time:.5f} seconds')
    print(f'\n\nTotal time taken to execute all operations: {time.elapsed_time:.5f} seconds')