class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def k_sum_paths(root, k):
    def print_paths(root, path, k):
        if root is None:
            return
        path.append(root.data)
        print_paths(root.left, path, k)
        print_paths(root.right, path, k)
        temp_sum = 0
        for j in range(len(path) - 1, -1, -1):
            temp_sum += path[j]
            if temp_sum == k:
                print(*path[j:], sep=" ")
        path.pop()
    def k_sum_paths_util(root, k, path):
        if root is None:
            return
        path.append(root.data)
        print_paths(root, path, k)
        k_sum_paths_util(root.left, k, path)
        k_sum_paths_util(root.right, k, path)
        path.pop()
    k_sum_paths_util(root, k, [])
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
print("Paths with sum 5:")
k_sum_paths(root, 5)