def is_goal(id):
    return id == 'bcdefghijkla'
def find_empty_tile_index(puzzle):
    for index, value in enumerate(puzzle):
        if value == 0:
            return index
def clean(node, map_open_states, map_closed_states):
    id_node_tuples = [(x.id, x) for x in node.nodes]
    for item in id_node_tuples:
        if item[0] in map_open_states or item[0] in map_closed_states:
            node.nodes.remove(item[1])
def format_move(node):
    puzzle_str = ', '.join(str(idx) for idx in node.puzzle)
    return f"{node.move_name} [{puzzle_str}]\n"
def solution_path(file, node):
    solution = []
    solution.append(format_move(node))
    it = node.parent_node
    while it is not None:
        solution.insert(0, format_move(it))
        it = it.parent_node
    for path in solution:
        file.write(path)