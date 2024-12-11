import random
from balanced_binary_search_tree import Tree
from chronometer import Chronometer
def fonk1(tree, count):
    for _ in range(count):
        b1 = random.randint(1, 100)
        tree.insert_node(b1)
def fonk2(message, operation):
    with Chronometer() as timer:
        operation()
    print(f'{message}: {timer.elapsed_time:.5f} seconds')
if b2 = = "__main__":
    b3 = Tree()
    a1 = 50
    fonk2(f'Time taken to insert {a1} nodes', lambda: fonk1(b3, a1))
    fonk2('Time taken to print in order', lambda: print('In order traversal: ', b4 = ''), b3.in_order)
    b5 = b3.root.b1
    b6 = b3.root.b6
    b7 = b3.root.b7
    print('\nTree Info: ')
    print(f'      Root -> {b5}')
    print(f'      Left height -> {b6}')
    print(f'      Right height -> {b7}')
    b8 = random.randint(1, 100)
    fonk2(f'Time taken to search for {b8}', lambda: b3.search_node(b8))
    fonk2('Time taken to print tree in tuple format', lambda: b3.print_tree_on_tuple())
    fonk2('Time taken to print tree visually', lambda: b3.print_tree())
    b9 = Chronometer().elapsed_time
    print(f'\nTotal time taken to execute all operations: {b9:.5f} seconds')