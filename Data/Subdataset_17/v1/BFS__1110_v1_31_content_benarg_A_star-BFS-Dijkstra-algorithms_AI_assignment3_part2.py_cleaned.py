import os
from PIL import Image, ImageDraw
class State:
    def __init__(self, x, y, terrain):
        self.x = x
        self.y = y
        self.terrain = terrain
class SearchNode:
    def __init__(self, status, cost):
        self.status = status
        self.cost = cost
        self.g = None
        self.h = None
        self.f = None
        self.parent = None
        self.kids = []
def read_board(filename):
    with open(filename, 'r') as file:
        b = file.read().strip().split('\n')
    board = []
    for i, line in enumerate(b):
        row = []
        for j, char in enumerate(line):
            row.append(SearchNode(State(j, len(b) - i - 1, char), cost(char)))
            if char == 'A':
                start = (j, len(b) - i - 1)
            elif char == 'B':
                end = (j, len(b) - i - 1)
        board.append(row)
    board.reverse()
    return start, end, board
def heuristic(s1, s2):
    return abs(s2.x - s1.x) + abs(s2.y - s1.y)
def solution(s1, sf):
    return s1.x == sf.x and s1.y == sf.y
def generate_all_successors(s, board):
    successors = []
    if s.x > 0:
        successors.append(board[s.y][s.x - 1])
    if s.x < len(board[s.y]) - 1:
        successors.append(board[s.y][s.x + 1])
    if s.y > 0:
        successors.append(board[s.y - 1][s.x])
    if s.y < len(board) - 1:
        successors.append(board[s.y + 1][s.x])
    return successors
def attach_and_eval(C, P, sf):
    C.parent = P
    C.g = P.g + C.cost
    h = heuristic(C.status, sf)
    C.h = h
    C.f = h + C.g
def propagate_path_improvement(P):
    for c in P.kids:
        if P.g + c.cost < c.g:
            c.parent = P
            c.g = P.g + c.cost
            c.f = c.g + c.h
            propagate_path_improvement(c)
def cost(terrain):
    terrain_costs = {'w': 100, 'm': 50, 'f': 10, 'g': 5, 'r': 1, 'A': 1, 'B': 1}
    return terrain_costs.get(terrain, 1)
def color(n):
    terrain_colors = {
        'w': (73, 216, 245), 'm': (99, 99, 99), 'f': (3, 82, 0),
        'g': (50, 200, 50), 'r': (114, 80, 41), 'A': (90, 180, 90), 'B': (255, 90, 90)
    }
    return terrain_colors.get(n.status.terrain, (255, 255, 255))
def draw_image(board, path, name):
    img = Image.new('RGB', (len(board[0]) * 20, len(board) * 20), "white")
    idraw = ImageDraw.Draw(img)
    for y in range(len(board)):
        for x in range(len(board[0])):
            c = color(board[y][x])
            idraw.rectangle([(x * 20, y * 20), (x * 20 + 20, y * 20 + 20)], fill=c, outline=(0, 0, 0))
            if board[y][x] in path:
                c = (107, 97, 255)
                idraw.rectangle([(x * 20 + 6, y * 20 + 6), (x * 20 + 14, y * 20 + 14)], fill=c, outline=(0, 0, 0))
    img.save(name, "PNG")
def visualize_path(ni, nf, board, name):
    path = []
    current = nf
    while current != ni:
        path.append(current)
        current = current.parent
    path.append(ni)
    path.reverse()
    draw_image(board, path, name)
def best_first_search(start, end, board, name):
    open_list = []
    closed_list = []
    ni = board[start[1]][start[0]]
    nf = board[end[1]][end[0]]
    ni.g = 0
    ni.h = heuristic(ni.status, nf.status)
    ni.f = ni.h
    open_list.append(ni)
    while open_list:
        open_list.sort(key=lambda node: node.f)
        X = open_list.pop(0)
        closed_list.append(X)
        if solution(X.status, nf.status):
            visualize_path(ni, nf, board, name)
            return 'SUCCEED'
        successors = generate_all_successors(X.status, board)
        for s in successors:
            X.kids.append(s)
            if s not in open_list and s not in closed_list:
                attach_and_eval(s, X, nf.status)
                open_list.append(s)
            elif X.g + s.cost < s.g:
                attach_and_eval(s, X, nf.status)
                if s in closed_list:
                    propagate_path_improvement(s)
    return 'FAIL'
if __name__ == "__main__":
    os.makedirs("assignment3_images", exist_ok=True)
    boards = ['board-2-1.txt', 'board-2-2.txt', 'board-2-3.txt', 'board-2-4.txt']
    for board_file in boards:
        start, end, board = read_board(f'boards/{board_file}')
        best_first_search(start, end, board, f'assignment3_images/part2_{board_file}')