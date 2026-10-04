import pygame
import random
b1 = (255, 255, 255)
b2 = (255, 0, 0)
b3 = (0, 255, 0)
a1 = 800
a2 = 600
a3 = 20
a4 = 15
b4 = a2
a5 = 24
a6 = 36
a7 = 30
a8 = 30
def fonk1(b19, a10, a9):
    b5 = False
    for b20 in range(len(b19) - a10):
        if b19[b20] > b19[b20 + 1]:
            b19[b20], b19[b20 + 1] = b19[b20 + 1], b19[b20]
            b5 = True
    pygame.time.wait(a9)
    return b19, b5
def fonk2(b9, b6, size, x, b4, message, color):
    b6 = pygame.b6.SysFont(b6, size)
    b7 = b6.render(message, True, color)
    b8 = b7.get_rect(center=(x, b4))
    b9.blit(b7, b8)
pygame.init()
b9 = pygame.display.set_mode((a1, a2))
pygame.display.set_caption("Bubble Sort Visualization")
b10 = pygame.time.Clock()
b11 = True
b12 = True
b13 = False
b14 = False
a9 = 50
b15 = "Your Name"
while b11:
    for event in pygame.event.get():
        if event.b16 = = pygame.QUIT:
            b11 = False
        if event.b16 = = pygame.KEYDOWN:
            if event.b17 = = pygame.K_ESCAPE or event.unicode == 'q':
                b11 = False
    b18 = pygame.b17.get_pressed()
    if b18[pygame.K_r]:
        if b12:
            b12 = False
        b13 = False
        a10 = 1
        a11 = 0
        a12 = 0
        a13 = 0
        b19 = [random.randint(1, a2) for _ in range(a8)]
    if b18[pygame.K_w]:
        a9 += 1
    if b18[pygame.K_s] and a9 > 0:
        a9 -= 1
    if not b13:
        b9.fill((0, 0, 0))
        for b20 in range(len(b19)):
            if b20 = = a10 - 1:
                pygame.draw.rect(b9, b2, pygame.Rect(b20 * a3, b4, a4, -b19[b20]))
            elif a10 - a11 - 2 < b20 < a10 - 1:
                pygame.draw.rect(b9, b3, pygame.Rect(b20 * a3, b4, a4, -b19[b20]))
            else:
                pygame.draw.rect(b9, b1, pygame.Rect(b20 * a3, b4, a4, -b19[b20]))
        if a10 = = len(b19):
            a10 = 1
            a11 = 0
        b19, b5 = fonk1(b19, a10, a9)
        a10 += 1
        a12 += 1
        if not b5:
            b14 = False
            a13 += 1
            a11 = 0
        else:
            a11 += 1
        if a11 = = len(b19) - 1:
            b14 = True
            b13 = True
        fonk2(b9, None, a5, a1 * 0.3, 0.5 * a5,
             f'Bubble b14 - {a8} length, {a9} ms a9, {a12} comparisons, {a13} swaps', b1)
    if b14 and b13 and not b12:
        for b20 in range(len(b19)):
            pygame.draw.rect(b9, b3, pygame.Rect(b20 * a3, b4, a4, -b19[b20]))
    if b12:
        fonk2(b9, None, a6, a1 / 2, a2 / 2, 'Press R to start', b1)
        fonk2(b9, None, a6, a1 / 2, a2 / 2 + 2 / 9 * a2 + a6,
             'Bubble Sort Visualization', b1)
        fonk2(b9, None, a6, a1 / 2, a2 / 2 + 2 / 9 * a2 + 2 * a6,
             'by', b1)
        fonk2(b9, None, a6, a1 / 2, a2 / 2 + 2 / 9 * a2 + 3 * a6,
             b15, b1)
    pygame.display.flip()
    b10.tick(a7)
pygame.quit()