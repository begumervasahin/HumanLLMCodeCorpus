import pygame
from random import randint
b1 = (255, 255, 255)
b2 = (255, 0, 0)
b3 = (0, 255, 0)
def fonk1(arr, a3, a7):
    b4 = len(arr)
    b5 = False
    for b19 in range(b4 - a3):
        if arr[b19] > arr[b19 + 1]:
            arr[b19], arr[b19 + 1] = arr[b19 + 1], arr[b19]
            b5 = True
            pygame.time.wait(a7)
    return arr, b5
def fonk2(b9, b6, size, x, b14, text, color):
    b6 = pygame.b6.Font(None, size)
    b7 = b6.render(text, True, color)
    b8 = b7.get_rect(center=(x, b14))
    b9.blit(b7, b8)
pygame.init()
a1 = 800
a2 = 600
b9 = pygame.display.set_mode((a1, a2))
pygame.display.set_caption("Bubble Sort Visualization")
b10 = pygame.time.Clock()
b11 = True
b12 = True
b13 = False
a3 = 1
a4 = 0
a5 = 0
a6 = 0
b4 = 100
a7 = 10
a8 = 4
a9 = 8
b14 = a2
b15 = [randint(1, a2) for _ in range(b4)]
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
        a3 = 1
        a4 = 0
        a5 = 0
        a6 = 0
        b15 = [randint(1, a2) for _ in range(b4)]
    if b18[pygame.K_w]:
        a7 += 1
    if b18[pygame.K_s] and a7 > 0:
        a7 -= 1
    if b13 is False:
        b9.fill((0, 0, 0))
        for b19 in range(len(b15)):
            if b19 = = a3 - 1:
                pygame.draw.rect(b9, b2, pygame.Rect(b19 * a9, b14, a8, -b15[b19]))
            elif b19 > a3 - a4 - 2 and b19 < a3 - 1:
                pygame.draw.rect(b9, b3, pygame.Rect(b19 * a9, b14, a8, -b15[b19]))
            else:
                pygame.draw.rect(b9, b1, pygame.Rect(b19 * a9, b14, a8, -b15[b19]))
        if a3 = = len(b15):
            a3 = 1
            a4 = 0
        b15, b20 = fonk1(b15, a3, a7)
        a3 += 1
        a5 += 1
        if b20 is False:
            a6 += 1
            a4 = 0
        else:
            a4 += 1
        if a4 = = len(b15) - 1:
            print(a4)
            b13 = True
        fonk2(b9, None, 24, a1 * 0.3, 0.5 * 24,
                  f'Bubble sort - {b4} length, {a7} ms a7, {a5} comparisons, {a6} swaps', b1)
    pygame.display.flip()
    b10.tick(60)
pygame.quit()