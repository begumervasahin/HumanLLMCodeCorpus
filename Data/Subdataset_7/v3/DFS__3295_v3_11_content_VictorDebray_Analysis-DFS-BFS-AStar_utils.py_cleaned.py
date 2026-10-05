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
    return b3.index(0)
def fonk4(node, map_open_states, map_closed_states):
    node.b5 = [n for n in node.b5 if n.b2 not in map_open_states and n.b2 not in map_closed_states]
def fonk5(node):
    b6 = ', '.join(map(str, node.b3))
    return f"{node.b4} [{b6}]\n"
def fonk6(file, node):
    b7 = []
    b8 = node
    while b8 is not None:
        b7.insert(0, fonk5(b8))
        b8 = b8.b1
    file.writelines(b7)
b9 = class1('root', [1, 2, 3, 4, 5, 6, 7, 8, 0], 'Start')
with open('b7.txt', 'w') as file:
    fonk6(file, b9)