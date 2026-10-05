def fonk1(b1):
    return b1 = = 'bcdefghijkla'
def fonk2(puzzle):
    return puzzle.index(0)
def fonk3(b5, map_open_states, map_closed_states):
    b5.b2 = [n for n in b5.b2 if n.b1 not in map_open_states and n.b1 not in map_closed_states]
def fonk4(b5):
    b3 = ', '.join(map(str, b5.puzzle))
    return f"{b5.move_name} [{b3}]\n"
def fonk5(file, b5):
    b4 = []
    while b5 is not None:
        b4.append(fonk4(b5))
        b5 = b5.parent_node
    for path in reversed(b4):
        file.write(path)