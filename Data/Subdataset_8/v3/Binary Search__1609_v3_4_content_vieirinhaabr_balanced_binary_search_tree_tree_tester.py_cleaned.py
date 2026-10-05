import random
from balanced_binary_search_tree import Tree
from chronometer import Chronometer
def insert_random_nodes(tree, count):
    for _ in range(count):
        info = random.randint(1, 100)
        tree.insert_node(info)
def measure_time_and_print(message, operation):
    with Chronometer() as timer:
        operation()
    print(f'{message}: {timer.elapsed_time:.5f} seconds')
if __name__ == "__main__":
    tree_control = Tree()
    insert_count = 50
    measure_time_and_print(f'Time taken to insert {insert_count} nodes', lambda: insert_random_nodes(tree_control, insert_count))
    measure_time_and_print('Time taken to print in order', lambda: print('In order traversal: ', end=''), tree_control.in_order)
    root_info = tree_control.root.info
    left_height = tree_control.root.left_height
    right_height = tree_control.root.right_height
    print('\nTree Info: ')
    print(f'      Root -> {root_info}')
    print(f'      Left height -> {left_height}')
    print(f'      Right height -> {right_height}')
    search_value = random.randint(1, 100)
    measure_time_and_print(f'Time taken to search for {search_value}', lambda: tree_control.search_node(search_value))
    measure_time_and_print('Time taken to print tree in tuple format', lambda: tree_control.print_tree_on_tuple())
    measure_time_and_print('Time taken to print tree visually', lambda: tree_control.print_tree())
    total_time = Chronometer().elapsed_time
    print(f'\nTotal time taken to execute all operations: {total_time:.5f} seconds')