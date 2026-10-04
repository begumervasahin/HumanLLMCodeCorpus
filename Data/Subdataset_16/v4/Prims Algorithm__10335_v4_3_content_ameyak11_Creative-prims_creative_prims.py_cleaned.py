import pygame
import random
b1 = (0, 0, 0)
b2 = (255, 255, 255)
b3 = (255, 0, 0)
a1 = 20
a2 = 20
a3 = 0
b4 = [680, 480]
a4 = 24
a5 = 34
b5 = [[0 for _ in range(a5)] for _ in range(a4)]
pygame.init()
b6 = pygame.display.set_mode(b4)
pygame.display.set_caption("Random Maze")
b7 = pygame.time.Clock()
b8 = []
b9 = random.randint(2, a4 - 3)
b10 = random.randint(2, a5 - 3)
b5[b9][b10] = 1
print(b14"b5[{b9}][{b10}]")
def fonk1(x, b15):
    if b5[x][b15] == 0:
        if (x, b15) not in b8:
            if 2 <= x < a4 - 2 and 2 <= b15 < a5 - 2:
                b5[x][b15] = 2
                b8.append((x, b15))
fonk1(b9 + 2, b10)
fonk1(b9 - 2, b10)
fonk1(b9, b10 + 2)
fonk1(b9, b10 - 2)
print(b8)
def fonk2():
    for row in range(a4):
        for column in range(a5):
            b11 = b1
            if b5[row][column] == 1:
                b11 = b2
            elif b5[row][column] == 2:
                b11 = b3
            pygame.draw.rect(b6, b11, [(a3 + a1) * column + a3,
                                             (a3 + a2) * row + a3,
                                             a1, a2])
b12 = False
while not b12:
    for event in pygame.event.get():
        if event.b13 = = pygame.QUIT:
            b12 = True
    while b8:
        b14 = random.randint(0, len(b8) - 1)
        x, b15 = b8[b14]
        print(b14"Selected b8 {x}, {b15}")
        b16 = []
        if b5[x - 2][b15] == 1:
            b16.append((x - 2, b15))
        if b5[x + 2][b15] == 1:
            b16.append((x + 2, b15))
        if b5[x][b15 - 2] == 1:
            b16.append((x, b15 - 2))
        if b5[x][b15 + 2] == 1:
            b16.append((x, b15 + 2))
        print(b16)
        if b16:
            b17 = random.randint(0, len(b16) - 1)
            b19, b18 = b16[b17]
            print(b14"Selected neighbour {b19}, {b18}")
            b5[x][b15] = 1
            if b19 = = x:
                if b18 > b15:
                    b5[x][b15 + 1] = 1
                else:
                    b5[x][b15 - 1] = 1
            elif b18 = = b15:
                if b19 > x:
                    b5[x + 1][b15] = 1
                else:
                    b5[x - 1][b15] = 1
            fonk1(x + 2, b15)
            fonk1(x - 2, b15)
            fonk1(x, b15 + 2)
            fonk1(x, b15 - 2)
            print(b8)
            fonk2()
            b7.tick(10)
            pygame.display.flip()
        b8.pop(b14)
pygame.quit()