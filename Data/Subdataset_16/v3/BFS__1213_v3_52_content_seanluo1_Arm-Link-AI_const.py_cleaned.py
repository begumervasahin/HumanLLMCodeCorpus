import pygame
from collections import deque
b1 = "config.txt"
a1 = 3
b2 = [5, 3, 1]
b3 = (0, 0, 0)
b4 = (255, 255, 255)
b5 = (255, 0, 0)
b6 = (0, 0, 255)
b7 = '%'
b8 = 'P'
b9 = '.'
b10 = ' '
a2 = 30
a3 = 2
class class1:
    def fonk1(self, b24):
        self.b11 = self.fonk2(b24)
        self.b12 = None
        self.b13 = None
        self.fonk3()
    def fonk2(self, b24):
        with open(b24, 'r') as file:
            return [list(line.strip()) for line in file]
    def fonk3(self):
        for b19, row in enumerate(self.b11):
            for x, b14 in enumerate(row):
                if b14 = = b8:
                    self.b12 = (x, b19)
                elif b14 = = b9:
                    self.b13 = (x, b19)
    def fonk4(self):
        for row in self.b11:
            print(''.join(row))
def fonk5(b25):
    b12 = b25.b12
    b13 = b25.b13
    if not b12 or not b13:
        return None
    b15 = deque([b12])
    b16 = set([b12])
    b17 = {b12: None}
    while b15:
        b18 = b15.popleft()
        if b18 = = b13:
            return fonk7(b17, b12, b13)
        for neighbor in fonk6(b18, b25):
            if neighbor not in b16:
                b16.add(neighbor)
                b17[neighbor] = b18
                b15.append(neighbor)
    return None
def fonk6(pos, b25):
    x, b19 = pos
    b20 = []
    b21 = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in b21:
        nx, b22 = x + dx, b19 + dy
        if 0 <= nx < len(b25.b11[0]) and 0 <= b22 < len(b25.b11):
            if b25.b11[b22][nx] != b7:
                b20.append((nx, b22))
    return b20
def fonk7(b17, b12, b13):
    b23 = []
    b18 = b13
    while b18 != b12:
        b23.append(b18)
        b18 = b17[b18]
    b23.append(b12)
    b23.reverse()
    return b23
def fonk8():
    b24 = 'BasicMap.txt'
    b25 = class1(b24)
    print("Map:")
    b25.fonk4()
    b23 = fonk5(b25)
    if b23:
        print("Path found:")
        for step in b23:
            print(step)
    else:
        print("No b23 found.")
if b26 = = '__main__':
    fonk8()