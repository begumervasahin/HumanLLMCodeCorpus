
import random
from balanced_binary_search_tree import Tree
from chronometer import Chronometer
if __name__ == "__main__":
    tree_control = Tree()
    with Chronometer() as time:
        count = 50
        with Chronometer() as t_insert:
            for _ in range(count):
                info = random.randint(1, 100)
                tree_control.insert_node(info)
            print(f'Time taken to insert {count} nodes: {t_insert.elapsed_time:.5f} seconds')
        with Chronometer() as t_inorder:
            print('\nIn order traversal: ', end='')
            tree_control.in_order()
            print(f'\nTime taken to print in order: {t_inorder.elapsed_time:.5f} seconds')
        print('\nTree Info: ')
        print('      Root -> ', tree_control.root.info)
        print('      Left height -> ', tree_control.root.left_height)
        print('      Right height -> ', tree_control.root.right_height)
        temp = random.randint(1, 100)
        with Chronometer() as t_search:
            print(f'\nSearching for {temp}...')
            tree_control.search_node(temp)
            print(f'Time taken to search for {temp}: {t_search.elapsed_time:.5f} seconds')
        with Chronometer() as t_tuple:
            print('\nGetting Tree in tuple format...')
            tuple_tree = tree_control.print_tree_on_tuple()
            print(tuple_tree)
            print(f'Time taken to print tree in tuple format: {t_tuple.elapsed_time:.5f} seconds')
        with Chronometer() as t_visual:
            print('\nPrinting Tree:')
            tree_control.print_tree()
            print(f'Time taken to print tree visually: {t_visual.elapsed_time:.5f} seconds')
    print(f'\n\nTotal time taken to execute all operations: {time.elapsed_time:.5f} seconds')