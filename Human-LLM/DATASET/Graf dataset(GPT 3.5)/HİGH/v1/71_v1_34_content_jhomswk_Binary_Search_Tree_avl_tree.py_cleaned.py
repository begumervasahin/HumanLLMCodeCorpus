from binary_search_tree import AVL_Tree
b1 = AVL_Tree()
b2 = [10, 5, 15, 3, 7, 12, 17]
for key in b2:
    b1.insert(key)
print("AVL Tree after insertions:")
b1.print_tree()
b3 = [5, 15]
for key in b3:
    b1.delete(key)
print("AVL Tree after deletions:")
b1.print_tree()
