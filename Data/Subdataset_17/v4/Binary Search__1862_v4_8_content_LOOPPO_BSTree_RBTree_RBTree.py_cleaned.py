class NodeRB:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.p = None
        self.color = "Red"
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
        self.nil = NodeRB(None)
        self.nil.set_color("Black")
        self.root = self.nil
    def set_root(self, key):
        self.root = NodeRB(key)
        self.root.set_color("Black")
        self.root.p = self.nil
        self.root.left = self.nil
        self.root.right = self.nil
    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.p = x
        y.p = x.p
        if x.p == self.nil:
            self.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        y.left = x
        x.p = y
    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.nil:
            y.right.p = x
        y.p = x.p
        if x.p == self.nil:
            self.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        y.right = x
        x.p = y
    def insert(self, key):
        if self.root is self.nil:
            self.set_root(key)
        else:
            self._insert_node(NodeRB(key))
    def _insert_node(self, z):
        y = self.nil
        current_node = self.root
        while current_node != self.nil:
            y = current_node
            if z.key < current_node.key:
                current_node = current_node.left
            else:
                current_node = current_node.right
        z.p = y
        if z.key < y.key:
            y.left = z
        else:
            y.right = z
        z.left = self.nil
        z.right = self.nil
        self._insert_fixup(z)
    def _insert_fixup(self, z):
        while z.p.color == "Red":
            if z.p == z.p.p.left:
                y = z.p.p.right
                if y.color == "Red":
                    z.p.color = "Black"
                    y.color = "Black"
                    z.p.p.color = "Red"
                    z = z.p.p
                else:
                    if z == z.p.right:
                        z = z.p
                        self.left_rotate(z)
                    z.p.color = "Black"
                    z.p.p.color = "Red"
                    self.right_rotate(z.p.p)
            else:
                y = z.p.p.left
                if y.color == "Red":
                    z.p.color = "Black"
                    y.color = "Black"
                    z.p.p.color = "Red"
                    z = z.p.p
                else:
                    if z == z.p.left:
                        z = z.p
                        self.right_rotate(z)
                    z.p.color = "Black"
                    z.p.p.color = "Red"
                    self.left_rotate(z.p.p)
        self.root.color = "Black"
    def find(self, key):
        return self._find_node(self.root, key)
    def _find_node(self, current_node, key):
        if current_node is self.nil:
            return False
        elif key == current_node.key:
            return True
        elif key < current_node.key:
            return self._find_node(current_node.left, key)
        else:
            return self._find_node(current_node.right, key)
    def inorder(self):
        def _inorder(node):
            if node is self.nil:
                return
            _inorder(node.left)
            print(f"{node.key} {node.color}")
            _inorder(node.right)
        _inorder(self.root)