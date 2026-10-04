class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class Tree:
    def __init__(self):
        self.head = None
        self.node_list = []
    def push(self, data):
        self.node_list.append(data)
    def insert_tree(self, data, address, index):
        if self.head is None:
            self.head = Node(data)
            current = self.head
        else:
            current = address
        left_index = 2 * index + 1
        right_index = 2 * index + 2
        if left_index < len(self.node_list):
            left_data = self.node_list[left_index]
            left_node = Node(left_data)
            current.left = left_node
            self.insert_tree(left_data, left_node, left_index)
        if right_index < len(self.node_list):
            right_data = self.node_list[right_index]
            right_node = Node(right_data)
            current.right = right_node
            self.insert_tree(right_data, right_node, right_index)
    def inorder(self, current):
        if current:
            self.inorder(current.left)
            print(current.data, end=' ')
            self.inorder(current.right)
    def levelorder(self, current):
        if current is None:
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
        if current is None:
            return -1
        left_height = self.height(current.left)
        right_height = self.height(current.right)
        return max(left_height, right_height) + 1
def main():
    tree = Tree()
    nodes = [2, 3, 5, 7, 1, 10, 9, 8]
    for node in nodes:
        tree.push(node)
    tree.insert_tree(tree.node_list[0], tree.head, 0)
    print("In-order traversal:")
    tree.inorder(tree.head)
    print()
    print("Level-order traversal:")
    tree.levelorder(tree.head)
    print()
    print("Height of the tree:")
    print(tree.height(tree.head))
if __name__ == "__main__":
    main()