def fonk1(b1):
    return b1 = = 'bcdefghijkla'
def fonk2(puzzle):
    for index, b2 in enumerate(puzzle):
        if b2 = = 0:
            return index
def fonk3(node, map_open_states, map_closed_states):
    b3 = [(x.b1, x) for x in node.nodes]
    for item in b3:
        if item[0] in map_open_states or item[0] in map_closed_states:
            node.nodes.remove(item[1])
def fonk4(node):
    b4 = ', '.join(str(idx) for idx in node.puzzle)
    return f"{node.move_name} [{b4}]\n"
def fonk5(file, node):
    b5 = []
    b5.append(fonk4(node))
    b6 = node.parent_node
    while b6 is not None:
        b5.insert(0, fonk4(b6))
        b6 = b6.parent_node
    for path in b5:
        file.write(path)