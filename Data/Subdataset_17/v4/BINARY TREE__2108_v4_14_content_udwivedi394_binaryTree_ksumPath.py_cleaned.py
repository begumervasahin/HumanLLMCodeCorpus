class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def ksum_paths(root, k):
    stack = []
    path_stack = []
    temp = root
    while True:
        while temp:
            stack.append(temp)
            if not path_stack:
                path_stack.append(temp)
                top_sum = 0
            else:
                top_sum = path_stack.pop()
                path_stack.append(temp)
            path_stack.append(temp.data + top_sum)
            temp = temp.left
        while temp is None and stack:
            temp = stack.pop()
            top_sum = path_stack.pop()
            while path_stack and path_stack[-1] != temp:
                top_sum -= path_stack.pop().data
            temp_sum = top_sum
            i = 0
            while i < len(path_stack):
                if temp_sum == k:
                    for j in range(i, len(path_stack)):
                        print(path_stack[j].data, end=' ')
                    print()
                temp_sum -= path_stack[i].data
                i += 1
            path_stack.append(top_sum)
            temp = temp.right
        if temp is None and not stack:
            break
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
ksum_paths(root, 5)