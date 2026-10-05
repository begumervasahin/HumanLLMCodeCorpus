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
        self.children = []
def read_board(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    board = []
    start, end = None, None
    for i, line in enumerate(lines):
        nodes = []
        for j, terrain in enumerate(line.strip()):
            node = SearchNode(State(j, len(lines) - i - 1, terrain), cost(terrain))
            nodes.append(node)
            if terrain == 'A':
                start = (j, len(lines) - i - 1)
            elif terrain == 'B':
                end = (j, len(lines) - i - 1)
        board.append(nodes)
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
def attach_and_eval(child, parent, goal_state):
    child.parent = parent
    child.g = parent.g + child.cost
    child.h = heuristic(child.status, goal_state)
    child.f = child.g + child.h
def propagate_path_improvement(node):
    for child in node.children:
        if node.g + child.cost < child.g:
            child.parent = node
            child.g = node.g + child.cost
            child.f = child.g + child.h
            propagate_path_improvement(child)
def cost(terrain):
    terrain_costs = {'w': 100, 'm': 50, 'f': 10, 'g': 5, 'r': 1}
    return terrain_costs.get(terrain, 1)
def color(node):
    terrain_colors = {'w': (73, 216, 245), 'm': (99, 99, 99), 'f': (3, 82, 0),
                      'g': (50, 200, 50), 'r': (114, 80, 41), 'A': (90, 180, 90), 'B': (255, 90, 90)}
    return terrain_colors.get(node.status.terrain, (255, 255, 255))
def visualize_path(start_node, end_node, board, filename):
    current_node = end_node
    path = [end_node]
    while current_node != start_node:
        current_node = current_node.parent
        path.append(current_node)
    board.reverse()
    draw_image(board, path, filename)
    board_representation = ''
    for node in path[1:-1]:
        node.status.terrain = 'O'
    for line in board:
        for node in line:
            board_representation += node.status.terrain
        board_representation += '\n'
    print(board_representation)
def draw_image(board, path, filename):
    img = Image.new('RGB', (len(board[0]) * 20, len(board) * 20), "white")
    draw = ImageDraw.Draw(img)
    for y in range(len(board)):
        for x in range(len(board[0])):
            color_val = color(board[y][x])
            draw.rectangle([(x * 20, y * 20), (x * 20 + 20, y * 20 + 20)], fill=color_val, outline=(0, 0, 0))
            if board[y][x] in path:
                draw.rectangle([(x * 20 + 6, y * 20 + 6), (x * 20 + 14, y * 20 + 14)], fill=(107, 97, 255), outline=(0, 0, 0))
    image_name = "assignment3_images/part2_" + filename + ".png"
    img.save(image_name, "PNG")
def best_first_search(start, end, board, filename):
    closed = []
    open_list = []
    start_node = board[start[1]][start[0]]
    goal_node = board[end[1]][end[0]]
    start_node.g = 0
    start_node.h = heuristic(start_node.status, goal_node.status)
    start_node.f = start_node.h
    open_list.append(start_node)
    while open_list:
        current_node = open_list.pop()
        closed.append(current_node)
        if solution(current_node.status, goal_node.status):
            visualize_path(start_node, goal_node, board, filename)
            return 'SUCCEED'
        successors = generate_all_successors(current_node.status, board)
        for successor in successors:
            current_node.children.append(successor)
            if successor not in open_list and successor not in closed:
                attach_and_eval(successor, current_node, goal_node.status)
                open_list.append(successor)
                open_list.sort(key=lambda x: x.f, reverse=True)
            elif current_node.g + successor.cost < successor.g:
                attach_and_eval(successor, current_node, goal_node.status)
                if successor in closed:
                    propagate_path_improvement(successor)
    return 'FAIL'
start_1, end_1, board_1 = read_board('boards/board-2-1.txt')
board_1 = best_first_search(start_1, end_1, board_1, 'board-2-1')
start_2, end_2, board_2 = read_board('boards/board-2-2.txt')
board_2 = best_first_search(start_2, end_2, board_2, 'board-2-2')
start_3, end_3, board_3 = read_board('boards/board-2-3.txt')
board_3 = best_first_search(start_3, end_3, board_3, 'board-2-3')
start_4, end_4, board_4 = read_board('boards/board-2-4.txt')
board_4 = best_first_search(start_4, end_4, board_4, 'board-2-4')