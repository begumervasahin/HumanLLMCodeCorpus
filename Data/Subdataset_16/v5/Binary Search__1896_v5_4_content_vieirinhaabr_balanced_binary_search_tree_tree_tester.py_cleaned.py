from balanced_binary_search_tree import Tree
import random as rdn
from chronometer import Chronometer
def fonk1(label, function):
    with Chronometer() as elapsed_time:
        function()
    print(f'{label}: {float(elapsed_time):.5f} seconds')
def fonk2(b4, a1):
    b1 = None
    for b3 in range(a1):
        b2 = rdn.randint(1, 100)
        b4.insert_node(b2)
        if b3 = = a1
            b1 = b2
    return b1
def fonk3():
    b4 = Tree()
    a1 = 50
    print("\nInserting nodes...")
    b1 = fonk1('Time spent inserting nodes', lambda: fonk2(b4, a1))
    print("\nPerforming in-order traversal...")
    fonk1('Time spent printing in-order traversal', b4.in_order)
    print('\nTree Info:')
    print(f'    Root: {b4.root.info}')
    print(f'    Left Height: {b4.root.left_height}')
    print(f'    Right Height: {b4.root.right_height}')
    print(f'\nSearching for {b1}...')
    fonk1('Time spent on search', lambda: b4.search_node(b1))
    print('\nGetting b4 in tuple format...')
    fonk1('Time spent on tuple conversion', b4.print_tree_on_tuple)
    print('\nTree structure:')
    fonk1('Time spent printing the b4', b4.print_tree)
if b5 = = "__main__":
    fonk3()