
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
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    def add_left(self, node):
        self.left = node
    def add_right(self, node):
        self.right = node
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
    if not (root.left or root.right):
        print("Up")
def tree_search(root, val):
    if root.value == val:
        print("Found")
    else:
        if root.left:
            tree_search(root.left, val)
        if root.right:
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
        if left[i] > right[j]:
            result.append(right[j])
            j += 1
        else:
            result.append(left[i])
            i += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
if __name__ == "__main__":
    print("Countdown from 5:")
    countdown(5)
    print("Factorial of 5:", factorial(5))
    print("Tail-recursive factorial of 5:", tail_factorial(5))
    print("Tree traversal:")
    tree_traverse(root_node)
    print("Tree search for value 4:")
    tree_search(root_node, 4)
    unsorted_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print("Sorted list:", merge_sort(unsorted_list))