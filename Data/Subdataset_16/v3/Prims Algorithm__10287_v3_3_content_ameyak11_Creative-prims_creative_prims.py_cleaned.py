import pygame
import random
b1 = (0, 0, 0)
b2 = (255, 255, 255)
b3 = (255, 0, 0)
a1 = 20
a2 = 20
a3 = 0
a4 = 34
a5 = 24
b4 = [680, 480]
b5 = [[0 for _ in range(a4)] for _ in range(a5)]
pygame.init()
b6 = pygame.display.set_mode(b4)
pygame.display.set_caption("RANDOM MAZE")
b7 = pygame.time.Clock()
b8 = []
b9 = random.randint(2, a5 - 3)
b10 = random.randint(2, a4 - 3)
b5[b9][b10] = 1
def fonk1(x, b15):
    if 2 <= x < a5 - 2 and 2 <= b15 < a4 - 2 and b5[x][b15] == 0:
        b5[x][b15] = 2
        b8.append((x, b15))
fonk1(b9 + 2, b10)
fonk1(b9 - 2, b10)
fonk1(b9, b10 + 2)
fonk1(b9, b10 - 2)
def fonk2():
    for row in range(a5):
        for column in range(a4):
            b11 = b1
            if b5[row][column] == 1:
                b11 = b2
            elif b5[row][column] == 2:
                b11 = b3
            pygame.draw.rect(b6, b11,
                             [(a3 + a1) * column + a3,
                              (a3 + a2) * row + a3, a1, a2])
fonk2()
pygame.display.flip()
b12 = False
while not b12:
    for event in pygame.event.get():
        if event.b13 = = pygame.QUIT:
            b12 = True
    while b8:
        b14 = random.randint(0, len(b8) - 1)
        x, b15 = b8[b14]
        b16 = []
        if b5[x - 2][b15] == 1:
            b16.append((x - 2, b15))
        if b5[x + 2][b15] == 1:
            b16.append((x + 2, b15))
        if b5[x][b15 - 2] == 1:
            b16.append((x, b15 - 2))
        if b5[x][b15 + 2] == 1:
            b16.append((x, b15 + 2))
        if b16:
            b18, b17 = random.choice(b16)
            b5[x][b15] = 1
            if b18 = = x:
                if b17 > b15:
                    b5[x][b15 + 1] = 1
                else:
                    b5[x][b15 - 1] = 1
            else:
                if b18 > x:
                    b5[x + 1][b15] = 1
                else:
                    b5[x - 1][b15] = 1
        fonk1(x + 2, b15)
        fonk1(x - 2, b15)
        fonk1(x, b15 + 2)
        fonk1(x, b15 - 2)
        fonk2()
        pygame.display.flip()
        del b8[b14]
    b7.tick(10)
pygame.quit()