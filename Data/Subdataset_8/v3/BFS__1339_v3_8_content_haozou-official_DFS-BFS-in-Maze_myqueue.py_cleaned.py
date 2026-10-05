class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        self.items.insert(0, item)
    def dequeue(self):
        return self.items.pop()
    def is_empty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)
def bfs_queue(graph, start, came_from):
    frontier = Queue()
    frontier.enqueue(start)
    came_from[start] = None
    while not frontier.is_empty():
        current_vertex = frontier.dequeue()
        if current_vertex == "GOAL":
            return current_vertex
        for next_vertex in graph[current_vertex]:
            if next_vertex not in came_from:
                frontier.enqueue(next_vertex)
                came_from[next_vertex] = current_vertex
    return None
def main():
    graph = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F"],
        "D": [],
        "E": ["GOAL"],
        "F": ["GOAL"]
    }
    came_from = {}
    result = bfs_queue(graph, "A", came_from)
    if result:
        print("Path found!")
    else:
        print("No path found.")
    print("Came from:", came_from)
if __name__ == "__main__":
    main()