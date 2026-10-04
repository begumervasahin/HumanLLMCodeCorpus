from balanced_binary_search_tree import Tree
import random as rdn
from chronometer import Chronometer
def main():
    tree = Tree()
    node_count = 50
    midpoint_node = None
    with Chronometer() as total_time:
        with Chronometer() as insert_time:
            for i in range(node_count):
                value = rdn.randint(1, 100)
                tree.insert_node(value)
                if i == node_count
                    midpoint_node = value
        print(f'Time spent on insertion: {float(insert_time):.5f} seconds')
        with Chronometer() as traversal_time:
            print('\nIn-order traversal: ', end='')
            tree.in_order()
        print(f'\n\nTime spent on in-order traversal: {float(traversal_time):.5f} seconds')
        print('\nTree Info:')
        print(f'      Root -> {tree.root.info}')
        print(f'      Left height -> {tree.root.left_height}')
        print(f'      Right height -> {tree.root.right_height}')
        with Chronometer() as search_time:
            print(f'\nSearching for {midpoint_node}...')
            tree.search_node(midpoint_node)
        print(f'Time spent on search: {float(search_time):.5f} seconds')
        with Chronometer() as tuple_time:
            print('Converting tree to tuple format...')
            tuple_tree = tree.print_tree_on_tuple()
            print(tuple_tree)
        print(f'Time spent on converting to tuple format: {float(tuple_time):.5f} seconds')
        with Chronometer() as print_tree_time:
            tree.print_tree()
        print(f'Time spent on printing the tree: {float(print_tree_time):.5f} seconds')
    print(f'\nTotal time for all operations: {float(total_time):.5f} seconds')
if __name__ == "__main__":
    main()