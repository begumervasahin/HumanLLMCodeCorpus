from balanced_binary_search_tree import Tree
import random as rdn
from chronometer import Chronometer
def fonk1(b6, a1):
    b1 = None
    for b3 in range(a1):
        b2 = rdn.randint(1, 100)
        b6.insert_node(b2)
        if b3 = = a1
            b1 = b2
    return b1
def fonk2(b6):
    print('\nIn-order traversal: ', b4 = '')
    b6.in_order()
def fonk3(b6):
    print('\nTree Info:')
    print(f'      Root -> {b6.root.info}')
    print(f'      Left height -> {b6.root.left_height}')
    print(f'      Right height -> {b6.root.right_height}')
def fonk4(b6, node_value):
    print(f'\nSearching for {node_value}...')
    b6.search_node(node_value)
def fonk5(b6):
    print('Converting b6 to tuple format...')
    b5 = b6.print_tree_on_tuple()
    print(b5)
def fonk6(b6):
    b6.print_tree()
def fonk7():
    b6 = Tree()
    a1 = 50
    with Chronometer() as total_time:
        with Chronometer() as insert_time:
            b1 = fonk1(b6, a1)
        print(f'Time spent on insertion: {float(insert_time):.5f} seconds')
        with Chronometer() as traversal_time:
            fonk2(b6)
        print(f'\n\nTime spent on in-order traversal: {float(traversal_time):.5f} seconds')
        fonk3(b6)
        with Chronometer() as search_time:
            fonk4(b6, b1)
        print(f'Time spent on search: {float(search_time):.5f} seconds')
        with Chronometer() as tuple_time:
            fonk5(b6)
        print(f'Time spent on converting to tuple format: {float(tuple_time):.5f} seconds')
        with Chronometer() as print_tree_time:
            fonk6(b6)
        print(f'Time spent on printing the b6: {float(print_tree_time):.5f} seconds')
    print(f'\nTotal time for all operations: {float(total_time):.5f} seconds')
if b7 = = "__main__":
    fonk7()