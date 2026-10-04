import collections
import heapq
class PriorityQueue:
    def __init__(self):
        self.elements = []
    def is_empty(self) -> bool:
        return not self.elements
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    def get(self):
        return heapq.heappop(self.elements)[1]
    def __len__(self) -> int:
        return len(self.elements)
class Queue:
    def __init__(self):
        self.elements = collections.deque()
    def is_empty(self) -> bool:
        return not self.elements
    def put(self, item):
        self.elements.append(item)
    def get(self):
        return self.elements.popleft()
    def __len__(self) -> int:
        return len(self.elements)
def bfs(start, end):
    frontier = Queue()
    frontier.put(start)
    came_from = {start: None}
    while not frontier.is_empty():
        current = frontier.get()
        current.visit()
        if current == end:
            print("WE MADE IT!!!")
            break
        for next_tile in current.neighbours:
            if next_tile not in came_from:
                frontier.put(next_tile)
                came_from[next_tile] = current
    return came_from
class Tile:
    def __init__(self, name):
        self.name = name
        self.neighbours = []
    def add_neighbour(self, neighbour):
        self.neighbours.append(neighbour)
    def visit(self):
        print(f"Visiting {self.name}")
def create_demo_tiles():
    tile_A = Tile('A')
    tile_B = Tile('B')
    tile_C = Tile('C')
    tile_D = Tile('D')
    tile_A.add_neighbour(tile_B)
    tile_B.add_neighbour(tile_C)
    tile_C.add_neighbour(tile_D)
    return tile_A, tile_D
def print_path(came_from, end):
    print("\nPath taken:")
    current = end
    while current is not None:
        print(current.name)
        current = came_from[current]
if __name__ == "__main__":
    start_tile, end_tile = create_demo_tiles()
    came_from = bfs(start_tile, end_tile)
    print_path(came_from, end_tile)