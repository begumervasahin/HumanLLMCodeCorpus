class Node:
    def __init__(self, val=-1, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class ReturnType:
    def __init__(self, size, head, mins, maxs):
        self.size = size
        self.head = head
        self.mins = mins
        self.maxs = maxs
def process_tree(head):
    if head is None:
        return ReturnType(0, None, 10000, -10000)
    left_subtree_info = process_tree(head.left)
    right_subtree_info = process_tree(head.right)
    include_self = 0
    if (left_subtree_info.head == head.left and right_subtree_info.head == head.right and
        head.val > left_subtree_info.maxs and head.val < right_subtree_info.mins):
        include_self = left_subtree_info.size + 1 + right_subtree_info.size
    p1 = left_subtree_info.size
    p2 = right_subtree_info.size
    max_size = max(max(p1, p2), include_self)
    if p1 > p2:
        max_head = left_subtree_info.head
    else:
        max_head = right_subtree_info.head
    if max_size == include_self:
        max_head = head
    return ReturnType(max_size, max_head, min(min(left_subtree_info.mins, right_subtree_info.mins), head.val),
                      max(max(left_subtree_info.maxs, right_subtree_info.maxs), head.val))
def print_tree(root):
    print("Binary Tree:")
    print_in_order(root, 0, 'H', 17)
def print_in_order(root, height, s, length):
    if root is None:
        return
    print_in_order(root.right, height + 1, 'v', length)
    val = s + str(root.val) + s
    lenM = len(val)
    lenL = (length - lenM)
    lenR = length - lenM - lenL
    val = get_space(lenL) + val + get_space(lenR)
    print(get_space(height * length) + val)
    print_in_order(root.left, height + 1, '^', length)
def get_space(num):
    return ' ' * num
if __name__ == '__main__':
    head = Node(6)
    head.left = Node(1)
    head.left.left = Node(0)
    head.left.right = Node(3)
    head.right = Node(12)
    head.right.left = Node(10)
    head.right.left.left = Node(4)
    head.right.left.left.left = Node(2)
    head.right.left.left.right = Node(5)
    head.right.left.right = Node(14)
    head.right.left.right.left = Node(11)
    head.right.left.right.right = Node(15)
    head.right.right = Node(13)
    head.right.right.left = Node(20)
    head.right.right.right = Node(16)
    result_head = process_tree(head).head
    print("Head value of processed tree:", result_head.val)
    print_tree(head)
    print_tree(result_head)