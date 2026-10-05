import pygame
from random import randint
b1 = (255, 255, 255)
b2 = (255, 0, 0)
b3 = (0, 255, 0)
pygame.init()
a1 = 800
a2 = 600
b4 = pygame.display.set_mode((a1, a2))
pygame.display.set_caption("Bubble Sort Visualization")
b5 = pygame.time.Clock()
b6 = True
b7 = True
b8 = False
b20, a5, c, b9 = 1, 0, 0, 0
a3 = 100
a4 = 10
width, distance, b10 = 4, 8, a2
b11 = [randint(1, a2) for _ in range(a3)]
def fonk1(arr, b20, a4):
    a3 = len(arr)
    b12 = False
    for b19 in range(a3 - b20):
        if arr[b19] > arr[b19 + 1]:
            arr[b19], arr[b19 + 1] = arr[b19 + 1], arr[b19]
            b12 = True
            pygame.time.wait(a4)
    return arr, b12
def fonk2(b4, b13, size, x, b10, text, color):
    b13 = pygame.b13.Font(None, size)
    b14 = b13.render(text, True, color)
    b15 = b14.get_rect(center=(x, b10))
    b4.blit(b14, b15)
while b6:
    for event in pygame.event.get():
        if event.b16 = = pygame.QUIT:
            b6 = False
        if event.b16 = = pygame.KEYDOWN:
            if event.b17 = = pygame.K_ESCAPE or event.unicode == 'q':
                b6 = False
    b18 = pygame.b17.get_pressed()
    if b18[pygame.K_r]:
        if b7:
            b7 = False
        b8 = False
        b20, a5, c, b9 = 1, 0, 0, 0
        b11 = [randint(1, a2) for _ in range(a3)]
    if b18[pygame.K_w]:
        a4 += 1
    if b18[pygame.K_s] and a4 > 0:
        a4 -= 1
    if b8 is False:
        b4.fill((0, 0, 0))
        for b19 in range(len(b11)):
            if b19 = = b20 - 1:
                pygame.draw.rect(b4, b2, pygame.Rect(b19 * distance, b10, width, -b11[b19]))
            elif b19 > b20 - a5 - 2 and b19 < b20 - 1:
                pygame.draw.rect(b4, b3, pygame.Rect(b19 * distance, b10, width, -b11[b19]))
            else:
                pygame.draw.rect(b4, b1, pygame.Rect(b19 * distance, b10, width, -b11[b19]))
        if b20 = = len(b11):
            b20 = 1
            a5 = 0
        b11, b21 = fonk1(b11, b20, a4)
        b20 += 1
        c += 1
        if b21 is False:
            b9 += 1
            a5 = 0
        else:
            a5 += 1
        if a5 = = len(b11) - 1:
            print(a5)
            b8 = True
        fonk2(b4, None, 24, a1 * 0.3, 0.5 * 24,
                  f'Bubble sort - {a3} length, {a4} ms a4, {c} comparisons, {b9} swaps', b1)
    pygame.display.flip()
    b5.tick(60)
pygame.quit()