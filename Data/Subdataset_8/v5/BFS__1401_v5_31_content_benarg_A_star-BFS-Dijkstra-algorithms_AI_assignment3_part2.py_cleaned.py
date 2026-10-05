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
        lines = file.readlines()
    board = []
    start, end = None, None
    for i, line in enumerate(lines):
        nodes = []
        for j, terrain in enumerate(line.strip()):
            node = SearchNode(State(j, len(lines) - i - 1, terrain), calculate_cost(terrain))
            nodes.append(node)
            if terrain == 'A':
                start = (j, len(lines) - i - 1)
            elif terrain == 'B':
                end = (j, len(lines) - i - 1)
        board.append(nodes)
    board.reverse()
    return start, end, board
def calculate_cost(terrain):
    terrain_costs = {'w': 100, 'm': 50, 'f': 10, 'g': 5, 'r': 1}
    return terrain_costs.get(terrain, 1)
def heuristic(s1, s2):
    return abs(s2.x - s1.x) + abs(s2.y - s1.y)
def is_solution(s1, sf):
    return s1.x == sf.x and s1.y == sf.y
def generate_successors(s, board):
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
def attach_and_evaluate(child, parent, end_state):
    child.parent = parent
    child.g = parent.g + child.cost
    h = heuristic(child.status, end_state)
    child.h = h
    child.f = h + child.g
def propagate_path_improvement(parent):
    for child in parent.kids:
        if parent.g + child.cost < child.g:
            child.parent = parent
            child.g = parent.g + child.cost
            child.f = child.g + child.h
            propagate_path_improvement(child)
def color(node):
    terrain_colors = {'w': (73, 216, 245), 'm': (99, 99, 99), 'f': (3, 82, 0),
                      'g': (50, 200, 50), 'r': (114, 80, 41), 'A': (90, 180, 90), 'B': (255, 90, 90)}
    return terrain_colors.get(node.status.terrain, (255, 255, 255))
def visualize_solution(start_node, end_node, board, name):
    current_node = end_node
    path = [end_node]
    while current_node != start_node:
        current_node = current_node.parent
        path.append(current_node)
    board.reverse()
    draw_image(board, path, name)
    updated_path = path[1:-1]
    for node in updated_path:
        node.status.terrain = 'O'
    representation = ''
    for line in board:
        representation += ''.join(node.status.terrain for node in line) + '\n'
    print(representation)
def draw_image(board, path, name):
    img = Image.new('RGB', (len(board[0]) * 20, len(board) * 20), "white")
    idraw = ImageDraw.Draw(img)
    for y, row in enumerate(board):
        for x, node in enumerate(row):
            fill_color = color(node)
            idraw.rectangle([(x * 20, y * 20), (x * 20 + 20, y * 20 + 20)], fill=fill_color, outline=(0, 0, 0))
            if node in path:
                idraw.rectangle([(x * 20 + 6, y * 20 + 6), (x * 20 + 14, y * 20 + 14)], fill=(107, 97, 255), outline=(0, 0, 0))
    image_name = "assignment3_images/part2_" + name + ".png"
    img.save(image_name, "PNG")
def best_first_search(start, end, board, name):
    closed = []
    open_list = []
    start_node = board[start[1]][start[0]]
    end_node = board[end[1]][end[0]]
    start_node.g = 0
    h = heuristic(start_node.status, end_node.status)
    start_node.h = h
    start_node.f = h
    open_list.append(start_node)
    while open_list:
        current_node = open_list.pop()
        closed.append(current_node)
        if is_solution(current_node.status, end_node.status):
            visualize_solution(start_node, end_node, board, name)
            return 'SUCCEED'
        successors = generate_successors(current_node.status, board)
        for successor in successors:
            current_node.kids.append(successor)
            if successor not in open_list and successor not in closed:
                attach_and_evaluate(successor, current_node, end_node.status)
                open_list.append(successor)
                open_list.sort(key=lambda e: e.f, reverse=True)
            elif current_node.g + successor.cost < successor.g:
                attach_and_evaluate(successor, current_node, end_node.status)
                if successor in closed:
                    propagate_path_improvement(successor)
    return 'FAIL'
start, end, board = read_board('boards/board-2-1.txt')
board = best_first_search(start, end, board, 'board-2-1')
start, end, board = read_board('boards/board-2-2.txt')
board = best_first_search(start, end, board, 'board-2-2')
start, end, board = read_board('boards/board-2-3.txt')
board = best_first_search(start, end, board, 'board-2-3')
start, end, board = read_board('boards/board-2-4.txt')
board = best_first_search(start, end, board, 'board-2-4')