class class1:
    def fonk1(self, b2, b3, b4, b1 = None):
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b1 = b1
        self.b5 = []
def fonk2(b2):
    return b2 = = 'bcdefghijkla'
def fonk3(b3):
    for index, b6 in enumerate(b3):
        if b6 = = 0:
            return index
def fonk4(node, map_open_states, map_closed_states):
    b7 = [(x.b2, x) for x in node.b5]
    for item in b7:
        if item[0] in map_open_states or item[0] in map_closed_states:
            node.b5.remove(item[1])
def fonk5(node):
    b8 = ', '.join(str(idx) for idx in node.b3)
    return f"{node.b4} [{b8}]\n"
def fonk6(file, node):
    b9 = []
    b9.insert(0, fonk5(node))
    b10 = node.b1
    while b10 is not None:
        b9.insert(0, fonk5(b10))
        b10 = b10.b1
    for path in b9:
        file.write(path)
b11 = class1('root', [1, 2, 3, 4, 5, 6, 7, 8, 0], 'Start')
with open('b9.txt', 'w') as file:
    fonk6(file, b11)