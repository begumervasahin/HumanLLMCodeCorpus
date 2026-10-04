
from PIL import Image, ImageDraw
class State:
    def __init__(self, x, y, terrain):
        self.x = x
        self.y = y
        self.terrain = terrain
class SearchNode:
    def __init__(self, state, cost):
        self.state = state
        self.cost = cost
        self.g = None
        self.h = None
        self.f = None
        self.parent = None
        self.kids = []
def read_board(filename):
    with open(filename, 'r') as file:
        lines = file.read().strip().split('\n')
    board = []
    for i, line in enumerate(lines):
        board_line = []
        for j, char in enumerate(line):
            node = SearchNode(State(j, len(lines) - i - 1, char), terrain_cost(char))
            board_line.append(node)
            if char == 'A':
                start = (j, len(lines) - i - 1)
            elif char == 'B':
                end = (j, len(lines) - i - 1)
        board.append(board_line)
    board.reverse()
    return start, end, board
def heuristic(s1, s2):
    return abs(s2.x - s1.x) + abs(s2.y - s1.y)
def is_solution(s1, sf):
    return s1.x == sf.x and s1.y == sf.y
def generate_all_successors(s, board):
    successors = []
    if s.x > 0:
        successors.append(board[s.y][s.x-1])
    if s.x < (len(board[s.y]) - 1):
        successors.append(board[s.y][s.x+1])
    if s.y > 0:
        successors.append(board[s.y-1][s.x])
    if s.y < (len(board) - 1):
        successors.append(board[s.y+1][s.x])
    return successors
def attach_and_eval(C, P, sf):
    C.parent = P
    C.g = P.g + C.cost
    C.h = heuristic(C.state, sf)
    C.f = C.g + C.h
def propagate_path_improvement(P):
    for c in P.kids:
        if P.g + c.cost < c.g:
            c.parent = P
            c.g = P.g + c.cost
            c.f = c.g + c.h
            propagate_path_improvement(c)
def terrain_cost(terrain):
    return {
        'w': 100,
        'm': 50,
        'f': 10,
        'g': 5,
        'r': 1,
    }.get(terrain, 1)
def terrain_color(n):
    return {
        'w': (73, 216, 245),
        'm': (99, 99, 99),
        'f': (3, 82, 0),
        'g': (50, 200, 50),
        'r': (114, 80, 41),
        'A': (90, 180, 90),
        'B': (255, 90, 90),
    }[n.state.terrain]
def visualize_path(ni, nf, board, name):
    X = nf
    path = [nf]
    while X != ni:
        X = X.parent
        path.append(X)
    board.reverse()
    draw_image(board, path, name)
    for X in path[1:-1]:
        X.state.terrain = 'O'
    representation = '\n'.join(''.join(e.state.terrain for e in line) for line in board)
    print(representation)
def draw_image(board, path, name):
    img = Image.new('RGB', (len(board[0]) * 20, len(board) * 20), "white")
    draw = ImageDraw.Draw(img)
    for y, row in enumerate(board):
        for x, node in enumerate(row):
            c = terrain_color(node)
            draw.rectangle([(x * 20, y * 20), (x * 20 + 20, y * 20 + 20)], fill=c, outline=(0, 0, 0))
            if node in path:
                draw.rectangle([(x * 20 + 6, y * 20 + 6), (x * 20 + 14, y * 20 + 14)], fill=(107, 97, 255), outline=(0, 0, 0))
    img.save(f"assignment3_images/part2_{name}.png", "PNG")
def best_first_search(start, end, board, name):
    closed = []
    open_list = []
    ni = board[start[1]][start[0]]
    nf = board[end[1]][end[0]]
    ni.g = 0
    ni.h = heuristic(ni.state, nf.state)
    ni.f = ni.g + ni.h
    open_list.append(ni)
    while open_list:
        X = open_list.pop()
        closed.append(X)
        if is_solution(X.state, nf.state):
            visualize_path(ni, nf, board, name)
            return 'SUCCEED'
        successors = generate_all_successors(X.state, board)
        for s in successors:
            X.kids.append(s)
            if s not in open_list and s not in closed:
                attach_and_eval(s, X, nf.state)
                open_list.append(s)
                open_list.sort(key=lambda e: e.f, reverse=True)
            elif X.g + s.cost < s.g:
                attach_and_eval(s, X, nf.state)
                if s in closed:
                    propagate_path_improvement(s)
    return 'FAIL'
if __name__ == "__main__":
    start, end, board = read_board('boards/board-2-1.txt')
    best_first_search(start, end, board, 'board-2-1')
    start, end, board = read_board('boards/board-2-2.txt')
    best_first_search(start, end, board, 'board-2-2')
    start, end, board = read_board('boards/board-2-3.txt')
    best_first_search(start, end, board, 'board-2-3')
    start, end, board = read_board('boards/board-2-4.txt')
    best_first_search(start, end, board, 'board-2-4')