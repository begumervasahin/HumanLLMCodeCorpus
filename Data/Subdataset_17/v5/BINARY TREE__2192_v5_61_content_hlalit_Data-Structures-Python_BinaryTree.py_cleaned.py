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
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end=' ')
            self.inorder(node.right)
    def level_order(self, node):
        if not node:
            return
        queue = [node]
        while queue:
            current = queue.pop(0)
            print(current.data, end=' ')
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
    def height(self, node):
        if not node:
            return -1
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return max(left_height, right_height) + 1
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