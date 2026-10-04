import pygame
from collections import deque
import sys
CONFIG_FILE = "config.txt"
MAX_NUM_OF_ART_LINKS = 3
ARM_LINKS_WIDTH = [5, 3, 1]
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255,0,0)
BLUE = (0,0,255)
WALL_CHAR = '%'
START_CHAR = 'P'
OBJECTIVE_CHAR = '.'
SPACE_CHAR = ' '
ALPHA = 0
BETA = 1
GAMMA = 2
DEFAULT_FPS = 30
DEFAULT_GRANULARITY = 2
class GameMap:
    def __init__(self, map_file):
        self.map = self.load_map(map_file)
        self.start = None
        self.goal = None
        self.find_start_and_goal()
    def load_map(self, map_file):
        with open(map_file, 'r') as file:
            return [list(line.strip()) for line in file]
    def find_start_and_goal(self):
        for y, row in enumerate(self.map):
            for x, char in enumerate(row):
                if char == START_CHAR:
                    self.start = (x, y)
                elif char == OBJECTIVE_CHAR:
                    self.goal = (x, y)
    def print_map(self):
        for row in self.map:
            print(''.join(row))
def bfs(game_map):
    start = game_map.start
    goal = game_map.goal
    if not start or not goal:
        return None
    queue = deque([start])
    visited = set()
    parent = {start: None}
    while queue:
        current = queue.popleft()
        if current == goal:
            return reconstruct_path(parent, start, goal)
        for neighbor in get_neighbors(current, game_map):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)
    return None
def get_neighbors(pos, game_map):
    x, y = pos
    neighbors = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(game_map.map[0]) and 0 <= ny < len(game_map.map):
            if game_map.map[ny][nx] != WALL_CHAR:
                neighbors.append((nx, ny))
    return neighbors
def reconstruct_path(parent, start, goal):
    path = []
    current = goal
    while current != start:
        path.append(current)
        current = parent[current]
    path.append(start)
    path.reverse()
    return path
def main():
    map_file = 'BasicMap.txt'
    game_map = GameMap(map_file)
    print("Map:")
    game_map.print_map()
    path = bfs(game_map)
    if path:
        print("Path found:")
        for step in path:
            print(step)
    else:
        print("No path found.")
if __name__ == '__main__':
    main()