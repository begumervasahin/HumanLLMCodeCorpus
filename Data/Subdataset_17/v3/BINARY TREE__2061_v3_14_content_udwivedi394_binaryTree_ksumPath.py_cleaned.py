class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def ksumPaths(root, k):
    if not root:
        return
    stack = []
    path_stack = []
    temp = root
    while True:
        while temp:
            stack.append(temp)
            if path_stack:
                top_sum = path_stack[-1] + temp.data
            else:
                top_sum = temp.data
            path_stack.append(top_sum)
            temp = temp.left
        while temp is None and stack:
            temp = stack.pop()
            top_sum = path_stack.pop()
            temp_sum = top_sum
            path_length = len(path_stack)
            for i in range(path_length - 1, -1, -1):
                if temp_sum == k:
                    print_path(stack, i + 1)
                temp_sum -= stack[i].data
            temp = temp.right
        if temp is None and not stack:
            break
def print_path(stack, length):
    for i in range(len(stack) - length, len(stack)):
        print(stack[i].data, end=" ")
    print()
root = Node(1)
root.left = Node(3)
root.left.left = Node(2)
root.left.right = Node(1)
root.left.right.left = Node(1)
root.right = Node(-1)
root.right.left = Node(4)
root.right.left.left = Node(1)
root.right.left.right = Node(2)
root.right.right = Node(5)
root.right.right.right = Node(6)
ksumPaths(root, 5)