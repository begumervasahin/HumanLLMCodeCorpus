import binary
def countdown(x):
    print(x)
    if x > 0:
        countdown(x - 1)
def factorial(x):
    if x == 0:
        return 1
    return x * factorial(x - 1)
def tail_factorial(x, acc=1):
    if x == 0:
        return acc
    return tail_factorial(x - 1, acc * x)
root_node = binary.Node(0)
node1 = binary.Node(1)
node2 = binary.Node(2)
node3 = binary.Node(3)
node4 = binary.Node(4)
node5 = binary.Node(5)
root_node.addLeft(node1)
root_node.addRight(node2)
node1.addLeft(node3)
node2.addLeft(node4)
node2.addRight(node5)
def tree_traverse(root):
    print(root.v)
    if root.l or root.r:
        if root.l:
            print("Left")
            tree_traverse(root.l)
        if root.r:
            print("Right")
            tree_traverse(root.r)
    else:
        print("Up")
def tree_search(root, val):
    if root.v == val:
        print("Found")
        return
    if root.l:
        tree_search(root.l, val)
    if root.r:
        tree_search(root.r, val)
def merge_sort(x):
    if len(x) < 2:
        return x
    mid = len(x)
    left = merge_sort(x[:mid])
    right = merge_sort(x[mid:])
    return merge(left, right)
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