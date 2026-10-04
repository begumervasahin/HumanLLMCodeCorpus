class NodeRB:
    def __init__(self, key, color="Red"):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.color = color
    def get(self):
        return self.key
    def set(self, key):
        self.key = key
    def set_color(self, color):
        self.color = color
    def get_color(self):
        return self.color
    def get_children(self):
        children = []
        if self.left is not None:
            children.append(self.left)
        if self.right is not None:
            children.append(self.right)
        return children
class RBT:
    def __init__(self):
        self.nil = NodeRB(None, color="Black")
        self.root = self.nil
    def set_root(self, key):
        self.root = NodeRB(key, color="Black")
        self.root.parent = self.nil
        self.root.left = self.nil
        self.root.right = self.nil
    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == self.nil:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y
    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.nil:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == self.nil:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.right = x
        x.parent = y
    def insert(self, key):
        new_node = NodeRB(key)
        self._insert_node(new_node)
    def _insert_node(self, z):
        y = self.nil
        current_node = self.root
        while current_node != self.nil:
            y = current_node
            if z.key < current_node.key:
                current_node = current_node.left
            else:
                current_node = current_node.right
        z.parent = y
        if y == self.nil:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        z.left = self.nil
        z.right = self.nil
        z.color = "Red"
        self._insert_fixup(z)
    def _insert_fixup(self, z):
        while z.parent.color == "Red":
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == "Red":
                    z.parent.color = "Black"
                    y.color = "Black"
                    z.parent.parent.color = "Red"
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.left_rotate(z)
                    z.parent.color = "Black"
                    z.parent.parent.color = "Red"
                    self.right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == "Red":
                    z.parent.color = "Black"
                    y.color = "Black"
                    z.parent.parent.color = "Red"
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.right_rotate(z)
                    z.parent.color = "Black"
                    z.parent.parent.color = "Red"
                    self.left_rotate(z.parent.parent)
        self.root.color = "Black"
    def find(self, key):
        return self._find_node(self.root, key)
    def _find_node(self, node, key):
        if node == self.nil or key == node.key:
            return node != self.nil
        elif key < node.key:
            return self._find_node(node.left, key)
        else:
            return self._find_node(node.right, key)
    def inorder(self):
        def _inorder(node):
            if node != self.nil:
                _inorder(node.left)
                print(f"{node.key} {node.color}")
                _inorder(node.right)
        _inorder(self.root)