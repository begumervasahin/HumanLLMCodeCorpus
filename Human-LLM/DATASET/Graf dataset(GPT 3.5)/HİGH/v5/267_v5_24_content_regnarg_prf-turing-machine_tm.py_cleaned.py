
a1 = 0
a2 = 1
a3 = 2
b1 = [...]
def fonk1(b8):
    state, b3, b2 = b8
    b3 = list(reversed(b3))
    b4 = f'[{state}] {" ".join(map(str, b3))} > {" ".join(map(str, b2))}'
    print(b4)
def fonk2(b8, action):
    state, b3, b2 = b8
    b5 = action[2]
    if b5 = = a2:
        b3, b2 = b3[:-1], [b3[-1]] + b2
    elif b5 = = a3:
        b3, b2 = b3 + [b2[0]], b2[1:]
    return (action[0], b3, b2)
def fonk3(tm_map, b8):
    state, b6, b6 = b8
    b7 = tm_map[state]
    for action in b7:
        if action[0] == b8[0]:
            return fonk2(b8, action)
    return b8
def fonk4(tm_map, b10):
    b8 = (0, b10, [])
    while not fonk5(tm_map, b8):
        b8 = fonk3(tm_map, b8)
        fonk1(b8)
    return b8
def fonk5(tm_map, b8):
    return b8[0] in tm_map[-1]
if b9 = = '__main__':
    b10 = [1, 1, 2, 2, 1]
    b8 = fonk4(b1, b10)
    fonk1(b8)