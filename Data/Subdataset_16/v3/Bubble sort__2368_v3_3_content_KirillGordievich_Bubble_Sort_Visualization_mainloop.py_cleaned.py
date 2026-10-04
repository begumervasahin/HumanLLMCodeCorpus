import pygame
import random
b1 = (255, 255, 255)
b2 = (255, 0, 0)
b3 = (0, 255, 0)
b4 = (0, 0, 0)
a1 = 800
a2 = 600
a3 = 20
a4 = 15
b5 = a2
a5 = 24
a6 = 36
a7 = 30
a8 = 30
def fonk1(b20, a10, a9):
    b6 = False
    for b22 in range(len(b20) - a10):
        if b20[b22] > b20[b22 + 1]:
            b20[b22], b20[b22 + 1] = b20[b22 + 1], b20[b22]
            b6 = True
    pygame.time.wait(a9)
    return b20, b6
def fonk2(b10, b7, size, x, y, message, b21):
    b7 = pygame.b7.SysFont(b7, size)
    b8 = b7.render(message, True, b21)
    b9 = b8.get_rect(center=(x, y))
    b10.blit(b8, b9)
def fonk3():
    pygame.init()
    b10 = pygame.display.set_mode((a1, a2))
    pygame.display.set_caption("Bubble Sort Visualization")
    return b10, pygame.time.Clock()
def fonk4():
    b10, b11 = fonk3()
    b12 = True
    b13 = True
    b14 = False
    b15 = False
    a9 = 50
    b16 = "Your Name"
    while b12:
        for event in pygame.event.get():
            if event.b17 = = pygame.QUIT:
                b12 = False
            if event.b17 = = pygame.KEYDOWN:
                if event.b18 = = pygame.K_ESCAPE or event.unicode == 'q':
                    b12 = False
        b19 = pygame.b18.get_pressed()
        if b19[pygame.K_r]:
            if b13:
                b13 = False
            b14 = False
            a10 = 1
            a11 = 0
            a12 = 0
            a13 = 0
            b20 = [random.randint(1, a2) for _ in range(a8)]
        if b19[pygame.K_w]:
            a9 += 1
        if b19[pygame.K_s] and a9 > 0:
            a9 -= 1
        if not b14:
            b10.fill(b4)
            for b22 in range(len(b20)):
                b21 = b1
                if b22 = = a10 - 1:
                    b21 = b2
                elif a10 - a11 - 2 < b22 < a10 - 1:
                    b21 = b3
                pygame.draw.rect(b10, b21, pygame.Rect(b22 * a3, b5, a4, -b20[b22]))
            if a10 = = len(b20):
                a10 = 1
                a11 = 0
            b20, b6 = fonk1(b20, a10, a9)
            a10 += 1
            a12 += 1
            if not b6:
                b15 = False
                a13 += 1
                a11 = 0
            else:
                a11 += 1
            if a11 = = len(b20) - 1:
                b15 = True
                b14 = True
            fonk2(b10, None, a5, a1 * 0.3, 0.5 * a5,
                        f'Bubble b15 - {a8} length, {a9} ms a9, {a12} a12, {a13} a13', b1)
        if b15 and b14 and not b13:
            for b22 in range(len(b20)):
                pygame.draw.rect(b10, b3, pygame.Rect(b22 * a3, b5, a4, -b20[b22]))
        if b13:
            fonk2(b10, None, a6, a1 / 2, a2 / 2, 'Press R to start', b1)
            fonk2(b10, None, a6, a1 / 2, a2 / 2 + 2 / 9 * a2 + a6,
                        'Bubble Sort Visualization', b1)
            fonk2(b10, None, a6, a1 / 2, a2 / 2 + 2 / 9 * a2 + 2 * a6,
                        'by', b1)
            fonk2(b10, None, a6, a1 / 2, a2 / 2 + 2 / 9 * a2 + 3 * a6,
                        b16, b1)
        pygame.display.flip()
        b11.tick(a7)
    pygame.quit()
if b23 = = "__main__":
    fonk4()