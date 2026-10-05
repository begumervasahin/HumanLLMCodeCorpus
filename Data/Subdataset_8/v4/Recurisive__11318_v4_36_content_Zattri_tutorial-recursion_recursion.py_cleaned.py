import binary
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
root_node = binary.Node(0)
node1 = binary.Node(1)
node2 = binary.Node(2)
node3 = binary.Node(3)
node4 = binary.Node(4)
node5 = binary.Node(5)
root_node.add_left(node1)
root_node.add_right(node2)
node1.add_left(node3)
node2.add_left(node4)
node2.add_right(node5)
def tree_traverse(root):
    print(root.value)
    if root.left or root.right:
        if root.left:
            print("Left")
            tree_traverse(root.left)
        if root.right:
            print("Right")
            tree_traverse(root.right)
    else:
        print("Up")
def tree_search(root, val):
    if root.value == val:
        print("Found")
    else:
        if root.left or root.right:
            if root.left:
                tree_search(root.left, val)
            if root.right:
                tree_search(root.right, val)
def merge_sort(x):
    result = []
    if len(x) < 2:
        return x
    mid = len(x)
    y = merge_sort(x[:mid])
    z = merge_sort(x[mid:])
    i = 0
    j = 0
    while i < len(y) and j < len(z):
        if y[i] > z[j]:
            result.append(z[j])
            j += 1
        else:
            result.append(y[i])
            i += 1
    result += y[i:]
    result += z[j:]
    return result