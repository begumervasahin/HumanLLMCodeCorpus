import BST_Iter as BST
def fonk1(b3, b1 = False):
    print()
    print("In order:  ", b3.inOrder())
    print("Pre order: ", b3.preOrder())
    print("BFS:       ", b3.BFS())
    if b1:
        print("Nodes (in BFS order):")
        b2 = b3.BFS()
        for node in b2:
            b3.find(node).printNode()
    print()
def fonk2():
    b3 = BST.BinarySearchTree(BST.Node(7))
    b3.insert(4)
    b3.insert(1)
    b3.insert(6)
    b3.insert(13)
    b3.insert(15)
    b3.insert(10)
    return b3, b3.getRoot()
def fonk3():
    b3, b4 = fonk2()
    print("\nPrint:")
    print("In order:  ", b3.inOrder())
    print("Pre order: ", b3.preOrder())
    print("Post order:", b3.postOrder())
    print("BFS:       ", b3.BFS())
    print("Root:", b5 = ' ')
    b4.printNode()
    print("\nFind:")
    b6 = [0, 1, 2, 5, 6, 7, 8, 12, 13, 14, 15, 20]
    for key in b6:
        print(key, b3.find(key))
    print("\nNext:")
    for key in b6:
        print(key, b3.next(b3.find(key)))
    print("\nPrevious:")
    for key in b6:
        print(key, b3.previous(b3.find(key)))
    print("\nRange search:")
    print("Range: 5 - 12")
    for node in b3.rangeSearch(5, 12):
        print(node, b5 = ' ')
    print("\nRotate right:")
    fonk1(b3, True)
    a1 = 7
    b3.rotateRight(b3.find(a1))
    print("Rotating right", a1)
    fonk1(b3, True)
    b3.find(a1).printNode()
    print("\nRotate left:")
    fonk1(b3, True)
    a1 = 1
    b3.rotateLeft(b3.find(a1))
    print("Rotating left", a1)
    fonk1(b3, True)
    b3.find(a1).printNode()
def fonk4():
    b3 = BST.BinarySearchTree(BST.Node(3))
    b3.insert(1)
    b3.insert(4)
    b3.insert(5)
    fonk1(b3, True)
    b3.delete(b3.find(3))
    fonk1(b3, True)
def fonk5():
    b3, b4 = fonk2()
    fonk1(b3, True)
    b3.delete(b3.find(7))
    fonk1(b3, True)
if b7 = = '__main__':
    fonk3()