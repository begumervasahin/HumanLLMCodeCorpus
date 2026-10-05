class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    def add_left(self, node):
        self.left = node
    def add_right(self, node):
        self.right = node
def countdown_recursive(x):
    print(x)
    if x > 0:
        countdown_recursive(x - 1)
def factorial_recursive(x):
    if x == 0:
        return 1
    else:
        return x * factorial_recursive(x - 1)
def factorial_tail_recursive(x, acc=1):
    if x == 0:
        return acc
    else:
        return factorial_tail_recursive(x - 1, acc * x)
def build_binary_tree():
    root_node = Node(0)
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    root_node.add_left(node1)
    root_node.add_right(node2)
    node1.add_left(node3)
    node2.add_left(node4)
    node2.add_right(node5)
    return root_node
def tree_traverse_pre_order(root):
    print(root.value)
    if root.left:
        print("Left")
        tree_traverse_pre_order(root.left)
    if root.right:
        print("Right")
        tree_traverse_pre_order(root.right)
def tree_search(root, val):
    if root is None:
        return
    if root.value == val:
        print("Found")
    else:
        tree_search(root.left, val)
        tree_search(root.right, val)
def merge_sort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr)
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    return merge(left_half, right_half)
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
if __name__ == "__main__":
    countdown_recursive(5)
    print(factorial_recursive(5))
    print(factorial_tail_recursive(5))
    root_node = build_binary_tree()
    tree_traverse_pre_order(root_node)
    tree_search(root_node, 3)
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(merge_sort(arr))