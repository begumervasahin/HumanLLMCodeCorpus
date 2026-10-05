class Queue:
    def __init__(self):
        self.items = []
        self.state = set()
    def enqueue(self, item):
        self.items.append(item)
        self.state.add(tuple(item.list))
    def dequeue(self):
        if not self.is_empty():
            item = self.items.pop(0)
            self.state.remove(tuple(item.list))
            return item
    def is_empty(self):
        return len(self.items) == 0
class PuzzleSolver:
    def __init__(self):
        pass
    def breadth_first_search(self, initial_state):
        queue = Queue()
        queue.enqueue(initial_state)
    def depth_first_search(self, initial_state):
    def depth_limited_search(self, initial_state, limit):
    def a_star_search(self, initial_state):
    def compare_performance(self):
if __name__ == '__main__':
    solver = PuzzleSolver()
    initial_state = PuzzleState()
    solution_bfs = solver.breadth_first_search(initial_state)
    solution_dfs = solver.depth_first_search(initial_state)
    solution_dls = solver.depth_limited_search(initial_state, 10)
    solution_a_star = solver.a_star_search(initial_state)
    solver.compare_performance()