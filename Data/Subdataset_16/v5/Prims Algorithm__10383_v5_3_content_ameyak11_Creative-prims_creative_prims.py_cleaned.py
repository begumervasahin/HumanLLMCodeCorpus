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
i, b9 = random.randint(2, a4 - 3), random.randint(2, a5 - 3)
b5[i][b9] = 1
print(b11"b5[{i}][{b9}]")
def fonk1(x, b12):
    if 2 <= x < a4 - 2 and 2 <= b12 < a5 - 2 and b5[x][b12] == 0:
        if (x, b12) not in b8:
            b5[x][b12] = 2
            b8.append((x, b12))
fonk1(i + 2, b9)
fonk1(i - 2, b9)
fonk1(i, b9 + 2)
fonk1(i, b9 - 2)
print(b8)
def fonk2():
    for row in range(a4):
        for column in range(a5):
            b10 = b1
            if b5[row][column] == 1:
                b10 = b2
            elif b5[row][column] == 2:
                b10 = b3
            pygame.draw.rect(b6, b10,
                             [(a3 + a1) * column + a3,
                              (a3 + a2) * row + a3,
                              a1, a2])
def fonk3():
    b11 = random.randint(0, len(b8) - 1)
    x, b12 = b8[b11]
    print(b11"Selected b8 {x}, {b12}")
    b13 = [(x - 2, b12), (x + 2, b12), (x, b12 - 2), (x, b12 + 2)]
    b14 = [(nx, ny) for nx, ny in b13 if 0 <= nx < a4 and 0 <= ny < a5 and b5[nx][ny] == 1]
    if b14:
        b16, b15 = random.choice(b14)
        print(b11"Selected neighbour {b16}, {b15}")
        b5[x][b12] = 1
        if b16 = = x:
            b5[x][b12 + 1 if b15 > b12 else b12 - 1] = 1
        elif b15 = = b12:
            b5[x + 1 if b16 > x else x - 1][b12] = 1
        fonk1(x + 2, b12)
        fonk1(x - 2, b12)
        fonk1(x, b12 + 2)
        fonk1(x, b12 - 2)
        print(b8)
        fonk2()
        b7.tick(10)
        pygame.display.flip()
    b8.pop(b11)
b17 = False
while not b17:
    for event in pygame.event.get():
        if event.b18 = = pygame.QUIT:
            b17 = True
    if b8:
        fonk3()
pygame.quit()