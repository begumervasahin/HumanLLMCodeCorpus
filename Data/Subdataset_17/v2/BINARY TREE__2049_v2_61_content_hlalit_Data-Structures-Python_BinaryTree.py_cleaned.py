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
            left_node = Node(self.node_list[left_index])
            current.left = left_node
            self.insert_tree(self.node_list[left_index], left_node, left_index)
        if right_index < len(self.node_list):
            right_node = Node(self.node_list[right_index])
            current.right = right_node
            self.insert_tree(self.node_list[right_index], right_node, right_index)
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
    tree.push(2)
    tree.push(3)
    tree.push(5)
    tree.push(7)
    tree.push(1)
    tree.push(10)
    tree.push(9)
    tree.push(8)
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