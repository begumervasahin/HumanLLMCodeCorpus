import pygame
import random
b1 = (0, 0, 0)
b2 = (255, 255, 255)
b3 = (255, 0, 0)
a1 = 20
a2 = 20
a3 = 0
b4 = [[0 for _ in range(34)] for _ in range(24)]
pygame.init()
b5 = [680, 480]
b6 = pygame.display.set_mode(b5)
pygame.display.set_caption("RANDOM MAZE")
b7 = False
b8 = pygame.time.Clock()
b9 = []
b10 = random.randint(2, 21)
b11 = random.randint(2, 31)
b4[b10][b11] = 1
print(b14"b4[{b10}][{b11}]")
def fonk1(x, b15):
    if 2 <= x < 22 and 2 <= b15 < 32 and b4[x][b15] == 0:
        b4[x][b15] = 2
        b9.append((x, b15))
fonk1(b10 + 2, b11)
fonk1(b10 - 2, b11)
fonk1(b10, b11 + 2)
fonk1(b10, b11 - 2)
def fonk2():
    for row in range(24):
        for column in range(34):
            b12 = b1
            if b4[row][column] == 1:
                b12 = b2
            elif b4[row][column] == 2:
                b12 = b3
            pygame.draw.rect(b6, b12,
                             [(a3 + a1) * column + a3,
                              (a3 + a2) * row + a3, a1, a2])
fonk2()
pygame.display.flip()
while not b7:
    for event in pygame.event.get():
        if event.b13 = = pygame.QUIT:
            b7 = True
    while b9:
        b14 = random.randint(0, len(b9) - 1)
        x, b15 = b9[b14]
        print(b14"Selected b9 {x, b15}")
        b16 = []
        if b4[x - 2][b15] == 1:
            b16.append((x - 2, b15))
        if b4[x + 2][b15] == 1:
            b16.append((x + 2, b15))
        if b4[x][b15 - 2] == 1:
            b16.append((x, b15 - 2))
        if b4[x][b15 + 2] == 1:
            b16.append((x, b15 + 2))
        print(b16)
        if b16:
            b18, b17 = random.choice(b16)
            print(b14"Selected neighbor is {b18, b17}")
            b4[x][b15] = 1
            if b18 = = x:
                if b17 > b15:
                    b4[x][b15 + 1] = 1
                else:
                    b4[x][b15 - 1] = 1
            else:
                if b18 > x:
                    b4[x + 1][b15] = 1
                else:
                    b4[x - 1][b15] = 1
        fonk1(x + 2, b15)
        fonk1(x - 2, b15)
        fonk1(x, b15 + 2)
        fonk1(x, b15 - 2)
        fonk2()
        pygame.display.flip()
        del b9[b14]
    b8.tick(10)
pygame.quit()