class Node:
    def __init__(self, key, value, _parent=None):
        self.value = value
        self.key = key
        self._left = None
        self._right = None
        self._parent = _parent
    def remove_child(self, child_to_remove):
        if child_to_remove == self._left:
            self._left = None
        elif child_to_remove == self._right:
            self._right = None
    def print_info(self):
        _left_str = "        " if self._left is None else "_left: " + str(self._left.value)
        _right_str = "         " if self._right is None else "_right: " + str(self._right.value)
        _parent_str = "   ROOT" if self._parent is None else "   _parent " + str(self._parent.value)
        print(f"Node({self.value})  {_left_str}  {_right_str} {_parent_str}")
    def is_leaf(self):
        return self._left is None and self._right is None
    def is_root(self):
        return self._parent is None
    def set_right(self, child_node):
        self._right = child_node
        child_node._parent = self
    def set_left(self, child_node):
        self._left = child_node
        child_node._parent = self
    def replace_child(self, old_child, new_child):
        if old_child == self._left:
            self.set_left(new_child)
        elif old_child == self._right:
            self.set_right(new_child)
        else:
            raise Exception("old_child node not found")
        old_child._parent = None
class TreePrinter:
    def __init__(self, bst):
        self.bst = bst
    def print_preorder(self, nice_print=False):
        self.preorder(self.bst.root, nice_print)
    def preorder(self, traverse_node, nice_print):
        if traverse_node is None:
            raise Exception("Passing None as node to preorder print is not expected.")
        if nice_print:
            traverse_node.print_info()
        else:
            print(f"{traverse_node.value} ", end="")
        if traverse_node._left is not None:
            self.preorder(traverse_node._left, nice_print)
        if traverse_node._right is not None:
            self.preorder(traverse_node._right, nice_print)
class BstByLinkedList:
    def __init__(self):
        self.root = None
    def count_nodes(self):
        return self.__count_nodes(self.root)
    def __count_nodes(self, subtree_root):
        if subtree_root is not None:
            return 1 + self.__count_nodes(subtree_root._left) + self.__count_nodes(subtree_root._right)
        else:
            return 0
    def insert(self, key, value):
        if key is None or value is None:
            raise Exception("Insert key or value is null.")
        elif self.root is None:
            self.root = Node(key, value, _parent=None)
        else:
            self.__insert(self.root, key, value)
    def __insert(self, subtree_root, key, value):
        if subtree_root.key == key:
            raise Exception(f"Duplicate key {key}")
        else:
            if key < subtree_root.key:
                if subtree_root._left is None:
                    subtree_root.set_left(Node(key, value))
                else:
                    self.__insert(subtree_root._left, key, value)
            else:
                if subtree_root._right is None:
                    subtree_root.set_right(Node(key, value))
                else:
                    self.__insert(subtree_root._right, key, value)
    def __search(self, subtree_root, search_key):
        if subtree_root is None:
            return None
        if subtree_root.key == search_key:
            return subtree_root
        elif search_key < subtree_root.key:
            return self.__search(subtree_root._left, search_key)
        else:
            return self.__search(subtree_root._right, search_key)
    def search(self, search_key):
        node = self.__search(self.root, search_key)
        return node.value if node is not None else None
    def find_biggest_node_in_subtree(self, subtree_root):
        if subtree_root._right is None:
            return subtree_root
        else:
            return self.find_biggest_node_in_subtree(subtree_root._right)
    def delete(self, key_delete):
        node_to_delete = self.__search(self.root, key_delete)
        if node_to_delete is None:
            raise Exception(f"Can't delete node with key {key_delete} because it was not found in the tree.")
        deleted_value = node_to_delete.value
        if node_to_delete.is_leaf():
            if node_to_delete.is_root():
                self.root = None
            else:
                node_to_delete._parent.remove_child(node_to_delete)
        elif node_to_delete._left is None:
            node_to_delete._parent.replace_child(node_to_delete, node_to_delete._right)
        else:
            replacement_node = self.find_biggest_node_in_subtree(node_to_delete._left)
            if replacement_node._left is not None:
                replacement_node._parent.replace_child(replacement_node, replacement_node._left)
            else:
                replacement_node._parent.remove_child(replacement_node)
            node_to_delete.key = replacement_node.key
            node_to_delete.value = replacement_node.value
        return deleted_value
if __name__ == "__main__":
    bst = BstByLinkedList()
    bst.insert(10, "ten")
    bst.insert(5, "five")
    bst.insert(15, "fifteen")
    bst.insert(7, "seven")
    bst.insert(3, "three")
    printer = TreePrinter(bst)
    printer.print_preorder(nice_print=True)
    print(f"Search for 7: {bst.search(7)}")
    bst.delete(5)
    printer.print_preorder(nice_print=True)
    print(f"Number of nodes: {bst.count_nodes()}")