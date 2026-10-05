from collections import deque
class Queue(deque):
    def enqueue(self, items):
        self.extend(items)
    def dequeue(self):
        return self.popleft()
class Stack(deque):
    def push(self, items):
        self.extend(items)
    def pop(self):
        return self.pop()
def search(structure, root):
    while True:
        yield root
        structure.enqueue(root.children)
        if not structure:
            break
        root = structure.dequeue()
def bfs(tree):
    return search(Queue(), tree)
def dfs(tree):
    return search(Stack(), tree)
if __name__ == "__main__":
    class Node:
        def __init__(self, value, *children):
            self.value = value
            self.children = list(children)
        def __repr__(self):
            return f"Node({self.value})"
    tree = Node(
        0,
        Node(1, Node(3), Node(4, Node(6), Node(7), Node(8))),
        Node(2, Node(5))
    )
    bfs_result = [node.value for node in bfs(tree)]
    dfs_result = [node.value for node in dfs(tree)]
    print("BFS traversal:", bfs_result)
    print("DFS traversal:", dfs_result)