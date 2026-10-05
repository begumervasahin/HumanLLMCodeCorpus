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
        b = file.read()
    b = b.split('\n')
    b = b[:-1]
    board = []
    for i, e1 in enumerate(b):
        line = []
        j = 0
        for e2 in e1:
            line.append(SearchNode(State(j, len(b) - i - 1, e2), cost(e2)))
            if e2 == 'A':
                start = (j, len(b) - i - 1)
            elif e2 == 'B':
                end = (j, len(b) - i - 1)
            j += 1
        board.append(line)
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
    if s.x < (len(board[s.y]) - 1):
        successors.append(board[s.y][s.x + 1])
    if s.y > 0:
        successors.append(board[s.y - 1][s.x])
    if s.y < (len(board) - 1):
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
    if terrain == 'w':
        return 100
    elif terrain == 'm':
        return 50
    elif terrain == 'f':
        return 10
    elif terrain == 'g':
        return 5
    elif terrain == 'r':
        return 1
    else:
        return 1
def color(n):
    if n.status.terrain == 'w':
        return (73, 216, 245)
    elif n.status.terrain == 'm':
        return (99, 99, 99)
    elif n.status.terrain == 'f':
        return (3, 82, 0)
    elif n.status.terrain == 'g':
        return (50, 200, 50)
    elif n.status.terrain == 'r':
        return (114, 80, 41)
    elif n.status.terrain == 'A':
        return (90, 180, 90)
    elif n.status.terrain == 'B':
        return (255, 90, 90)
def visualization(ni, nf, board, name):
    X = nf
    path = []
    path.append(nf)
    while X != ni:
        X = X.parent
        path.append(X)
    board.reverse()
    draw_image(board, path, name)
    representation = ''
    for X in path[1:-1]:
        X.status.terrain = 'O'
    for line in board:
        for e in line:
            representation += e.status.terrain
        representation += '\n'
    print(representation)
def draw_image(board, path, name):
    img = Image.new('RGB', (len(board[0]) * 20, len(board) * 20), "white")
    idraw = ImageDraw.Draw(img)
    for y in range(0, len(board)):
        for x in range(0, len(board[0])):
            c = color(board[y][x])
            idraw.rectangle([(x * 20, y * 20), (x * 20 + 20, y * 20 + 20)], fill=c, outline=(0, 0, 0))
            if board[y][x] in path:
                c = (107, 97, 255)
                idraw.rectangle([(x * 20 + 6, y * 20 + 6), (x * 20 + 14, y * 20 + 14)], fill=c, outline=(0, 0, 0))
    name_image = "assignment3_images/part2_" + name + ".png"
    img.save(name_image, "PNG")
def best_first_search(start, end, board, name):
    closed = []
    open = []
    ni = board[start[1]][start[0]]
    nf = board[end[1]][end[0]]
    ni.g = 0
    h = heuristic(ni.status, nf.status)
    ni.h = h
    ni.f = h
    open.append(ni)
    while open:
        X = open.pop()
        closed.append(X)
        if solution(X.status, nf.status):
            visualization(ni, nf, board, name)
            return 'SUCCEED'
        successors = generate_all_successors(X.status, board)
        for s in successors:
            X.kids.append(s)
            if s not in open and s not in closed:
                attach_and_eval(s, X, nf.status)
                open.append(s)
                open.sort(key=lambda e: e.f, reverse=True)
            elif X.g + s.cost < s.g:
                attach_and_eval(s, X, nf.status)
                if s in closed:
                    propagate_path_improvement(s)
    return 'FAIL'
start, end, board = read_board('boards/board-2-1.txt')
board = best_first_search(start, end, board, 'board-2-1')
start, end, board = read_board('boards/board-2-2.txt')
board = best_first_search(start, end, board, 'board-2-2')
start, end, board = read_board('boards/board-2-3.txt')
board = best_first_search(start, end, board, 'board-2-3')
start, end, board = read_board('boards/board-2-4.txt')
board = best_first_search(start, end, board, 'board-2-4')