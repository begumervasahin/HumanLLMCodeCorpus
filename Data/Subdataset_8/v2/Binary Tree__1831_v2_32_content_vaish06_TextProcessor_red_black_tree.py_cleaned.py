from binary_search_tree import TreeMap
class RedBlackTreeMap(TreeMap):
    class _Node(TreeMap._Node):
        __slots__ = '_red'
        def __init__(self, element, parent=None, left=None, right=None):
            super().__init__(element, parent, left, right)
            self._red = True
    def _set_red(self, node):
        node._node._red = True
    def _set_black(self, node):
        node._node._red = False
    def _is_red(self, node):
        return node is not None and node._node._red
    def _resolve_red(self, node):
        if self.is_root(node):
            self._set_black(node)
        else:
            parent = self.parent(node)
            if self._is_red(parent):
                uncle = self.sibling(parent)
                if not self._is_red(uncle):
                    middle = self._restructure(node)
                    self._set_black(middle)
                    self._set_red(self.left(middle))
                    self._set_red(self.right(middle))
                else:
                    grand = self.parent(parent)
                    self._set_red(grand)
                    self._set_black(self.left(grand))
                    self._set_black(self.right(grand))
                    self._resolve_red(grand)
    def _rebalance_delete(self, node):
        if len(self) == 1:
            self._set_black(self.root())
        elif node is not None:
            num_children = self.num_children(node)
            if num_children == 1:
                child = next(self.children(node))
                if not self._is_red_leaf(child):
                    self._fix_deficit(node, child)
            elif num_children == 2:
                if self._is_red_leaf(self.left(node)):
                    self._set_black(self.left(node))
                else:
                    self._set_black(self.right(node))
    def _fix_deficit(self, z, y):
        if not self._is_red(y):
            x = self._get_red_child(y)
            if x is not None:
                old_color = self._is_red(z)
                middle = self._restructure(x)
                self._set_color(middle, old_color)
                self._set_black(self.left(middle))
                self._set_black(self.right(middle))
            else:
                self._set_red(y)
                if self._is_red(z):
                    self._set_black(z)
                elif not self.is_root(z):
                    self._fix_deficit(self.parent(z), self.sibling(z))
        else:
            self._rotate(y)
            self._set_black(y)
            self._set_red(z)
            if z == self.right(y):
                self._fix_deficit(z, self.left(z))
            else:
                self._fix_deficit(z, self.right(z))