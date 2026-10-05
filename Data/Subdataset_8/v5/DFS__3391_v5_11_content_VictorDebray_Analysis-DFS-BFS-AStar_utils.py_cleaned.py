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
    while node is not None:
        solution.append(format_move(node))
        node = node.parent_node
    for path in reversed(solution):
        file.write(path)