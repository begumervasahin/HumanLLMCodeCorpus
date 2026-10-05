class Node:
    def __init__(self, id, puzzle, move_name, parent_node=None):
        self.id = id
        self.puzzle = puzzle
        self.move_name = move_name
        self.parent_node = parent_node
        self.nodes = []
def is_goal(id):
    return id == 'bcdefghijkla'
def find_empty_tile_index(puzzle):
    return puzzle.index(0)
def clean(node, map_open_states, map_closed_states):
    node.nodes = [n for n in node.nodes if n.id not in map_open_states and n.id not in map_closed_states]
def format_move(node):
    puzzle_str = ', '.join(map(str, node.puzzle))
    return f"{node.move_name} [{puzzle_str}]\n"
def solution_path(file, node):
    solution = []
    current_node = node
    while current_node is not None:
        solution.insert(0, format_move(current_node))
        current_node = current_node.parent_node
    file.writelines(solution)
root_node = Node('root', [1, 2, 3, 4, 5, 6, 7, 8, 0], 'Start')
with open('solution.txt', 'w') as file:
    solution_path(file, root_node)