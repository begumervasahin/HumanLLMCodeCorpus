class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def k_sum_paths(root, k):
    def find_paths_with_sum(node, path, target_sum):
        if node is None:
            return
        path.append(node.data)
        find_paths_with_sum(node.left, path, target_sum)
        find_paths_with_sum(node.right, path, target_sum)
        current_sum = 0
        for i in range(len(path) - 1, -1, -1):
            current_sum += path[i]
            if current_sum == target_sum:
                print(*path[i:], sep=" ")
        path.pop()
    def find_k_sum_paths_util(node, k, path):
        if node is None:
            return
        path.append(node.data)
        find_paths_with_sum(node, path, k)
        find_k_sum_paths_util(node.left, k, path)
        find_k_sum_paths_util(node.right, k, path)
        path.pop()
    find_k_sum_paths_util(root, k, [])
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