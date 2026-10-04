import pygame
import random
b1 = (0, 0, 0)
b2 = (255, 255, 255)
b3 = (255, 0, 0)
a1 = 20
a2 = 20
a3 = 0
b4 = []
for row in range(24):
    b4.append([])
    for column in range(34):
        b4[row].append(0)
pygame.init()
b5 = [680, 480]
b6 = pygame.display.set_mode(b5)
pygame.display.set_caption("RANDOM MAZE")
b7 = False
b8 = pygame.time.Clock()
b9 = []
a4 = 0
b10 = random.randint(2, 21)
b11 = random.randint(2, 31)
b4[b10][b11] = 1
print("b4[" + str(b10) + "][" + str(b11) + "]")
if b4[b10 + 2][b11] == 0:
    if (b10 + 2, b11) not in b9:
        if b10 + 2 < 21:
            b4[b10 + 2][b11] = 2
            b9.append((b10 + 2, b11))
    print(b9)
if b4[b10 - 2][b11] == 0:
    if (b10 - 2, b11) not in b9:
        if b10 - 2 >= 2:
            b4[b10 - 2][b11] = 2
            b9.append((b10 - 2, b11))
    print(b9)
if b4[b10][b11 + 2] == 0:
    if (b10, b11 + 2) not in b9:
        if b11 + 2 < 32:
            b4[b10][b11 + 2] = 2
            b9.append((b10, b11 + 2))
    print(b9)
if b4[b10][b11 - 2] == 0:
    if (b10, b11 - 2) not in b9:
        if b11 - 2 >= 2:
            b4[b10][b11 - 2] = 2
            b9.append((b10, b11 - 2))
    print(b9)
for row in range(24):
    for column in range(34):
        b12 = b1
        if b4[row][column] == 1:
            b12 = b2
        if b4[row][column] == 2:
            b12 = b3
        pygame.draw.rect(b6, b12, [(a3 + a1) * column + a3, (a3 + a2) * row + a3, a1, a2])
b8.tick(10)
pygame.display.flip()
while not b7:
    for event in pygame.event.get():
        if event.b13 = = pygame.QUIT:
            b7 = True
    while len(b9) != 0:
        b14 = random.randint(0, len(b9) - 1)
        b15 = b9[b14]
        print("Selected b9 " + str(b15))
        b16 = b15[0]
        b17 = b15[1]
        b18 = []
        if b4[b16 - 2][b17] == 1:
            b18.append((b16 - 2, b17))
        if b4[b16 + 2][b17] == 1:
            b18.append((b16 + 2, b17))
        if b4[b16][b17 - 2] == 1:
            b18.append((b16, b17 - 2))
        if b4[b16][b17 + 2] == 1:
            b18.append((b16, b17 + 2))
        print(b18)
        if len(b18) > 0:
            b19 = random.randint(0, len(b18) - 1)
            b20 = b18[b19]
            print("Selected neighbour is " + str(b20))
            b21 = b20[0]
            b22 = b20[1]
            b4[b16][b17] = 1
            if b21 = = b16:
                if b22 > b17:
                    b4[b16][b17 + 1] = 1
                elif b22 < b17:
                    b4[b16][b17 - 1] = 1
            elif b22 = = b17:
                if b21 > b16:
                    b4[b16 + 1][b17] = 1
                elif b21 < b16:
                    b4[b16 - 1][b17] = 1
        if b4[b16 + 2][b17] == 0:
            if (b16 + 2, b17) not in b9:
                if b16 + 2 < 21:
                    b4[b16 + 2][b17] = 2
                    b9.append((b16 + 2, b17))
            print(b9)
        if b4[b16 - 2][b17] == 0:
            if (b16 - 2, b17) not in b9:
                if b16 - 2 >= 2:
                    b4[b16 - 2][b17] = 2
                    b9.append((b16 - 2, b17))
            print(b9)
        if b4[b16][b17 + 2] == 0:
            if (b16, b17 + 2) not in b9:
                if b17 + 2 < 32:
                    b4[b16][b17 + 2] = 2
                    b9.append((b16, b17 + 2))
            print(b9)
        if b4[b16][b17 - 2] == 0:
            if (b16, b17 - 2) not in b9:
                if b17 - 2 >= 2:
                    b4[b16][b17 - 2] = 2
                    b9.append((b16, b17 - 2))
            print(b9)
        for row in range(24):
            for column in range(34):
                b12 = b1
                if b4[row][column] == 1:
                    b12 = b2
                pygame.draw.rect(b6, b12, [(a3 + a1) * column + a3, (a3 + a2) * row + a3, a1, a2])
        b8.tick(10)
        pygame.display.flip()
        del b9[b14]
pygame.quit()