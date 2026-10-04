from balanced_binary_search_tree import Tree
import random as rdn
from chronometer import Chronometer
def main():
    tree = Tree()
    node_count = 50
    temp = None
    with Chronometer() as total_time:
        with Chronometer() as insert_time:
            for i in range(node_count):
                value = rdn.randint(1, 100)
                tree.insert_node(value)
                if i == node_count
                    temp = value
        print(f'Time spent inserting nodes: {float(insert_time):.5f} seconds')
        with Chronometer() as in_order_time:
            print('\nIn-order traversal: ', end='')
            tree.in_order()
        print(f'\nTime spent printing in-order traversal: {float(in_order_time):.5f} seconds')
        print('\nTree Info:')
        print(f'    Root: {tree.root.info}')
        print(f'    Left Height: {tree.root.left_height}')
        print(f'    Right Height: {tree.root.right_height}')
        with Chronometer() as search_time:
            print(f'\nSearching for {temp}...')
            tree.search_node(temp)
        print(f'Time spent on search: {float(search_time):.5f} seconds')
        with Chronometer() as tuple_time:
            print('\nGetting tree in tuple format...')
            tuple_tree = tree.print_tree_on_tuple()
            print(tuple_tree)
        print(f'Time spent on tuple conversion: {float(tuple_time):.5f} seconds')
        with Chronometer() as print_time:
            print('\nTree structure:')
            tree.print_tree()
        print(f'Time spent printing the tree: {float(print_time):.5f} seconds')
    print(f'\nTotal time for all operations: {float(total_time):.5f} seconds')
if __name__ == "__main__":
    main()