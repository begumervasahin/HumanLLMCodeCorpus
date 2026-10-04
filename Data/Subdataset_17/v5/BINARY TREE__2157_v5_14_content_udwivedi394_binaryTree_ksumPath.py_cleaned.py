class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def print_path(path_stack, start_index):
    for i in range(start_index, len(path_stack)):
        print(path_stack[i].data, end=' ')
    print()
def find_k_sum_paths(root, k):
    stack = []
    path_stack = []
    current_node = root
    while True:
        while current_node:
            stack.append(current_node)
            if not path_stack:
                path_stack.append((current_node, current_node.data))
            else:
                top_node, top_sum = path_stack[-1]
                path_stack.append((current_node, top_sum + current_node.data))
            current_node = current_node.left
        while current_node is None and stack:
            current_node = stack.pop()
            top_node, top_sum = path_stack.pop()
            temp_sum = top_sum
            for i in range(len(path_stack)):
                if temp_sum == k:
                    print_path(path_stack, i)
                temp_sum -= path_stack[i][0].data
            if temp_sum == k:
                print_path(path_stack, 0)
            if path_stack:
                top_node, top_sum = path_stack[-1]
            path_stack.append((current_node, top_sum))
            current_node = current_node.right
        if current_node is None and not stack:
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
find_k_sum_paths(root, 5)