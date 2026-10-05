class ListBinaryTree:
    DATA = 0
    LEFT = 1
    RIGHT = 2
    def __init__(self, root_value, left=None, right=None):
        self.node = [root_value, left, right]
    @classmethod
    def create_tree(cls, a_list):
        return cls(a_list[0], a_list[1], a_list[2])
    def insert_value_left(self, value):
        self.node[self.LEFT] = ListBinaryTree(value, self.node[self.LEFT], None)
    def insert_value_right(self, value):
        self.node[self.RIGHT] = ListBinaryTree(value, None, self.node[self.RIGHT])
    def insert_tree_left(self, tree):
        self.node[self.LEFT] = tree
    def insert_tree_right(self, tree):
        self.node[self.RIGHT] = tree
    def set_value(self, new_value):
        self.node[self.DATA] = new_value
    def get_value(self):
        return self.node[self.DATA]
    def get_left_subtree(self):
        return self.node[self.LEFT]
    def get_right_subtree(self):
        return self.node[self.RIGHT]
    def __str__(self):
        return f'[{self.node[self.DATA]}, {self.node[self.LEFT]}, {self.node[self.RIGHT]}]'
def construct_tree(inorder, preorder, start, end):
    if start > end:
        return None
    root_value = preorder[construct_tree.preIndex]
    construct_tree.preIndex += 1
    tree = ListBinaryTree(root_value)
    if start == end:
        return tree
    inorder_node_index = inorder.index(root_value)
    left_subtree = construct_tree(inorder, preorder, start, inorder_node_index - 1)
    right_subtree = construct_tree(inorder, preorder, inorder_node_index + 1, end)
    tree.insert_tree_left(left_subtree)
    tree.insert_tree_right(right_subtree)
    return tree
def main():
    print("Binary Tree reconstructed by gsoa420:")
    inorder = input("Please enter the inorder sequence: ").split()
    preorder = input("Please enter the preorder sequence: ").split()
    construct_tree.preIndex = 0
    tree = construct_tree(inorder, preorder, 0, len(preorder) - 1)
    print(tree)
if __name__ == "__main__":
    main()