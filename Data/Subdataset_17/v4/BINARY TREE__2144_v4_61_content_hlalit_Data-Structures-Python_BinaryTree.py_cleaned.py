class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class Tree:
    def __init__(self):
        self.head = None
        self.data_list = []
    def push(self, data):
        self.data_list.append(data)
    def insert_tree(self, data, address, index):
        if self.head is None:
            self.head = Node(data)
            current = self.head
        else:
            current = address
        lindex = 2 * index + 1
        rindex = 2 * index + 2
        if lindex < len(self.data_list):
            lnode = Node(self.data_list[lindex])
            current.left = lnode
            self.insert_tree(self.data_list[lindex], lnode, lindex)
        if rindex < len(self.data_list):
            rnode = Node(self.data_list[rindex])
            current.right = rnode
            self.insert_tree(self.data_list[rindex], rnode, rindex)
    def inorder(self, current):
        if current:
            self.inorder(current.left)
            print(current.data, end=' ')
            self.inorder(current.right)
    def level_order(self, current):
        if not current:
            return
        queue = [current]
        while queue:
            node = queue.pop(0)
            print(node.data, end=' ')
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    def height(self, current):
        if not current:
            return -1
        lheight = self.height(current.left)
        rheight = self.height(current.right)
        return max(lheight, rheight) + 1
tree = Tree()
nodes = [2, 3, 5, 7, 1, 10, 9, 8]
for node in nodes:
    tree.push(node)
tree.insert_tree(tree.data_list[0], tree.head, 0)
print("In-order Traversal:")
tree.inorder(tree.head)
print()
print("Level-order Traversal:")
tree.level_order(tree.head)
print()
print("Height of the Tree:")
print(tree.height(tree.head))
print()