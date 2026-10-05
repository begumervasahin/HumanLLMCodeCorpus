
from binary_search_tree import AVL_Tree
avl_tree = AVL_Tree()
keys_to_insert = [10, 5, 15, 3, 7, 12, 17]
for key in keys_to_insert:
    avl_tree.insert(key)
print("AVL Tree after insertions:")
avl_tree.print_tree()
keys_to_delete = [5, 15]
for key in keys_to_delete:
    avl_tree.delete(key)
print("AVL Tree after deletions:")
avl_tree.print_tree()
