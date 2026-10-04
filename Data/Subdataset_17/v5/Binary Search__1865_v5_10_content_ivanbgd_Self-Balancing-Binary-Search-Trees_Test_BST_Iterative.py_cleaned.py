
import BST_Iter as BST
def print_tree(bst, verbose=False):
    print("\nTree Structure:")
    print("In order:  ", bst.in_order())
    print("Pre order: ", bst.pre_order())
    print("BFS:       ", bst.bfs())
    if verbose:
        print("Nodes (in BFS order):")
        for node in bst.bfs():
            bst.find(node).print_node()
    print()
def create_tree():
    bst = BST.BinarySearchTree(BST.Node(7))
    bst.insert(4)
    bst.insert(1)
    bst.insert(6)
    bst.insert(13)
    bst.insert(15)
    bst.insert(10)
    return bst, bst.get_root()
def test_tree():
    bst, root = create_tree()
    print("\nTree Traversals:")
    print("In order:  ", bst.in_order())
    print("Pre order: ", bst.pre_order())
    print("Post order:", bst.post_order())
    print("BFS:       ", bst.bfs())
    print("Root Node:", end=' ')
    root.print_node()
    print("\nSearch Results:")
    for key in [0, 1, 2, 5, 6, 7, 8, 12, 13, 14, 15, 20]:
        print(f"Search for {key}: {bst.find(key)}")
    print("\nNext Node Results:")
    for key in [0, 1, 2, 4, 5, 6, 7, 8, 10, 12, 14, 15, 16]:
        next_node = bst.next(bst.find(key))
        print(f"Next node after {key}: {next_node}")
    print("\nPrevious Node Results:")
    for key in [0, 1, 2, 4, 5, 6, 7, 8, 10, 12, 14, 15, 16]:
        prev_node = bst.previous(bst.find(key))
        print(f"Previous node before {key}: {prev_node}")
    print("\nRange Search Results (5 to 12):")
    for node in bst.range_search(5, 12):
        print(node, end=' ')
    print()
    print("\nRotation Tests:")
    print("Initial Tree:")
    print_tree(bst, verbose=True)
    print("\nRotating Right at Node 7:")
    bst.rotate_right(bst.find(7))
    print_tree(bst, verbose=True)
    print("\nRotating Left at Node 1:")
    bst.rotate_left(bst.find(1))
    print_tree(bst, verbose=True)
def test1():
    bst = BST.BinarySearchTree(BST.Node(3))
    bst.insert(1)
    bst.insert(4)
    bst.insert(5)
    print_tree(bst, True)
    bst.delete(bst.find(3))
    print_tree(bst, True)
def test2():
    bst, root = create_tree()
    print_tree(bst, True)
    bst.delete(bst.find(7))
    print_tree(bst, True)
test_tree()