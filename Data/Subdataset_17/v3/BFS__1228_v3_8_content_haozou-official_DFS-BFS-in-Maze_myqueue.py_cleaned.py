class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        self.items.insert(0, item)
    def dequeue(self):
        return self.items.pop()
    def is_empty(self):
        return not self.items
    def size(self):
        return len(self.items)
class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def is_empty(self):
        return not self.items
    def size(self):
        return len(self.items)
def bfs(graph, start, goal):
    frontier = Queue()
    frontier.enqueue(start)
    came_from = {start: None}
    while not frontier.is_empty():
        current = frontier.dequeue()
        if current == goal:
            return reconstruct_path(came_from, start, goal)
        for next_node in graph[current]:
            if next_node not in came_from:
                frontier.enqueue(next_node)
                came_from[next_node] = current
    return None
def dfs(graph, start, goal):
    frontier = Stack()
    frontier.push(start)
    came_from = {start: None}
    while not frontier.is_empty():
        current = frontier.pop()
        if current == goal:
            return reconstruct_path(came_from, start, goal)
        for next_node in graph[current]:
            if next_node not in came_from:
                frontier.push(next_node)
                came_from[next_node] = current
    return None
def reconstruct_path(came_from, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()
    return path
def main():
    graph = {
        'A': ['B', 'C', 'E'],
        'B': ['A', 'D', 'F'],
        'C': ['A', 'G'],
        'D': ['B'],
        'E': ['A', 'F'],
        'F': ['B', 'E', 'H'],
        'G': ['C', 'H'],
        'H': ['F', 'G']
    }
    start = 'A'
    goal = 'H'
    print(f"BFS Path from {start} to {goal}:")
    bfs_path = bfs(graph, start, goal)
    print(bfs_path)
    print(f"\nDFS Path from {start} to {goal}:")
    dfs_path = dfs(graph, start, goal)
    print(dfs_path)
if __name__ == '__main__':
    main()