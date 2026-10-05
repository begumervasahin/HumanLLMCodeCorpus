class TreeNode:
    def __init__(self, val=-1, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class SubTreeInfo:
    def __init__(self, size, head, min_val, max_val):
        self.size = size
        self.head = head
        self.min_val = min_val
        self.max_val = max_val
def process_tree(head):
    if head is None:
        return SubTreeInfo(0, None, float('inf'), float('-inf'))
    left_subtree = process_tree(head.left)
    right_subtree = process_tree(head.right)
    include_self = 0
    if (left_subtree.head == head and right_subtree.head == head and
            left_subtree.max_val < head.val < right_subtree.min_val):
        include_self = left_subtree.size + 1 + right_subtree.size
    max_size = max(left_subtree.size, right_subtree.size, include_self)
    max_head = left_subtree.head if left_subtree.size > right_subtree.size else right_subtree.head
    if max_size == include_self:
        max_head = head
    return SubTreeInfo(max_size, max_head, min(left_subtree.min_val, right_subtree.min_val, head.val),
                       max(left_subtree.max_val, right_subtree.max_val, head.val))
def print_tree(root):
    print("Binary Tree:")
    _print_in_order(root, 0, 'H', 17)
def _print_in_order(root, height, s, length):
    if root is None:
        return
    _print_in_order(root.right, height + 1, 'v', length)
    val = s + str(root.val) + s
    len_m = len(val)
    len_l = (length - len_m)
    len_r = length - len_m - len_l
    val = _get_space(len_l) + val + _get_space(len_r)
    print(_get_space(height * length) + val)
    _print_in_order(root.left, height + 1, '^', length)
def _get_space(num):
    return ' ' * num
if __name__ == '__main__':
    head = TreeNode(6)
    head.left = TreeNode(1)
    head.left.left = TreeNode(0)
    head.left.right = TreeNode(3)
    head.right = TreeNode(12)
    head.right.left = TreeNode(10)
    head.right.left.left = TreeNode(4)
    head.right.left.left.left = TreeNode(2)
    head.right.left.left.right = TreeNode(5)
    head.right.left.right = TreeNode(14)
    head.right.left.right.left = TreeNode(11)
    head.right.left.right.right = TreeNode(15)
    head.right.right = TreeNode(13)
    head.right.right.left = TreeNode(20)
    head.right.right.right = TreeNode(16)
    result_head = process_tree(head).head
    print("Head value after processing:", result_head.val)
    print_tree(head)
    print_tree(result_head)