def fonk1(b1):
    return b1 = = 'bcdefghijkla'
def fonk2(puzzle):
    a1 = 0
    for b2 in puzzle:
        if b2 = = 0:
            return a1
        a1 += 1
def fonk3(node, map_open_states, map_closed_states):
    b3 = [(b2.b1, b2) for b2 in node.nodes]
    for item in b3:
        if item[0] in map_open_states or item[0] in map_closed_states:
            node.nodes.remove(item[1])
def fonk4(node):
    a2 = 0
    b4 = node.move_name + ' ['
    for idx in node.puzzle:
        if a2 = = 0:
            b4 += str(idx)
            a2 += 1
        else:
            b4 += ', ' + str(idx)
    b4 += ']\n'
    return b4
def fonk5(file, node):
    b5 = []
    b5.insert(0, fonk4(node))
    b6 = node.parent_node
    while True:
        b5.insert(0, fonk4(b6))
        b6 = b6.parent_node
        if b6 is None:
            break
    for path in b5:
        file.write(path)