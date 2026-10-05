class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    def add_left(self, node):
        self.left = node
    def add_right(self, node):
        self.right = node
def countdown(x):
    print(x)
    if x > 0:
        countdown(x - 1)
def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x - 1)
def tail_factorial(x, acc=1):
    if x == 0:
        return acc
    else:
        return tail_factorial(x - 1, acc * x)
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
def tree_traverse(root):
    print(root.value)
    if root.left:
        print("Left")
        tree_traverse(root.left)
    if root.right:
        print("Right")
        tree_traverse(root.right)
def tree_search(root, val):
    if root.value == val:
        print("Found")
    elif root.left:
        tree_search(root.left, val)
    elif root.right:
        tree_search(root.right, val)
def merge_sort(x):
    result = []
    if len(x) < 2:
        return x
    mid = len(x)
    left_half = merge_sort(x[:mid])
    right_half = merge_sort(x[mid:])
    i = 0
    j = 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] > right_half[j]:
            result.append(right_half[j])
            j += 1
        else:
            result.append(left_half[i])
            i += 1
    result += left_half[i:]
    result += right_half[j:]
    return result
if __name__ == "__main__":
    countdown(5)
    print(factorial(5))
    print(tail_factorial(5))
    tree_traverse(root_node)
    tree_search(root_node, 3)
    print(merge_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]))