
import BST_Iter as BST
def fonk1(b2, b1 = False):
    print("\nTree Structure:")
    print("In order:  ", b2.in_order())
    print("Pre order: ", b2.pre_order())
    print("BFS:       ", b2.bfs())
    if b1:
        print("Nodes (in BFS order):")
        for node in b2.bfs():
            b2.find(node).print_node()
    print()
def fonk2():
    b2 = BST.BinarySearchTree(BST.Node(7))
    b2.insert(4)
    b2.insert(1)
    b2.insert(6)
    b2.insert(13)
    b2.insert(15)
    b2.insert(10)
    return b2, b2.get_root()
def fonk3():
    b2, b3 = fonk2()
    print("\nTree Traversals:")
    print("In order:  ", b2.in_order())
    print("Pre order: ", b2.pre_order())
    print("Post order:", b2.post_order())
    print("BFS:       ", b2.bfs())
    print("Root Node:", b4 = ' ')
    b3.print_node()
    print("\nSearch Results:")
    for key in [0, 1, 2, 5, 6, 7, 8, 12, 13, 14, 15, 20]:
        print(f"Search for {key}: {b2.find(key)}")
    print("\nNext Node Results:")
    for key in [0, 1, 2, 4, 5, 6, 7, 8, 10, 12, 14, 15, 16]:
        b5 = b2.next(b2.find(key))
        print(f"Next node after {key}: {b5}")
    print("\nPrevious Node Results:")
    for key in [0, 1, 2, 4, 5, 6, 7, 8, 10, 12, 14, 15, 16]:
        b6 = b2.previous(b2.find(key))
        print(f"Previous node before {key}: {b6}")
    print("\nRange Search Results (5 to 12):")
    for node in b2.range_search(5, 12):
        print(node, b4 = ' ')
    print()
    print("\nRotation Tests:")
    print("Initial Tree:")
    fonk1(b2, b1 = True)
    print("\nRotating Right at Node 7:")
    b2.rotate_right(b2.find(7))
    fonk1(b2, b1 = True)
    print("\nRotating Left at Node 1:")
    b2.rotate_left(b2.find(1))
    fonk1(b2, b1 = True)
def fonk4():
    b2 = BST.BinarySearchTree(BST.Node(3))
    b2.insert(1)
    b2.insert(4)
    b2.insert(5)
    fonk1(b2, True)
    b2.delete(b2.find(3))
    fonk1(b2, True)
def fonk5():
    b2, b3 = fonk2()
    fonk1(b2, True)
    b2.delete(b2.find(7))
    fonk1(b2, True)
fonk3()