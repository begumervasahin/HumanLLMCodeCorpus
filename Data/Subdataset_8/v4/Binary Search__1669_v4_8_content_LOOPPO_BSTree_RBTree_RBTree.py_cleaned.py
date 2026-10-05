class NodeRB:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.color = "Red"
    def get_key(self):
        return self.key
    def set_key(self, key):
        self.key = key
    def set_color(self, color):
        self.color = color
    def get_children(self):
        children = []
        if self.left:
            children.append(self.left)
        if self.right:
            children.append(self.right)
        return children
    def get_color(self):
        return self.color
class RedBlackTree:
    def __init__(self):
        self.nil = NodeRB(None)
        self.nil.set_color("Black")
        self.root = self.nil
    def set_root(self, key):
        self.root = NodeRB(key)
        self.root.set_color("Black")
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
        if self.root is self.nil:
            self.set_root(key)
        else:
            self._insert_node(NodeRB(key))
    def _insert_node(self, z):
        y = self.nil
        x = self.root
        while x != self.nil:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if z.key < y.key:
            y.left = z
        else:
            y.right = z
        z.left = self.nil
        z.right = self.nil
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
    def _find_node(self, current_node, key):
        if current_node == self.nil:
            return False
        elif key == current_node.key:
            return True
        elif key < current_node.key:
            return self._find_node(current_node.left, key)
        else:
            return self._find_node(current_node.right, key)
    def inorder(self):
        def _inorder(v):
            if v is self.nil:
                return
            if v.left is not self.nil:
                _inorder(v.left)
            print(str(v.key) + " " + v.color)
            if v.right is not self.nil:
                _inorder(v.right)
        _inorder(self.root)
if __name__ == "__main__":
    rbt = RedBlackTree()
    rbt.insert(10)
    rbt.insert(20)
    rbt.insert(30)
    rbt.insert(15)
    rbt.inorder()