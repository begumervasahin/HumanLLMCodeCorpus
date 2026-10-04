import pygame
import random
from colors import white, red, green
from functions import buble_sort, text
from settings import screen_width, screen_height, distance, y, width, n, text_size, menu_text_size, name, fps
pygame.init()
b1 = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Bubble Sort Visualization")
b2 = pygame.time.Clock()
b3 = True
b4 = True
b5 = False
b6 = False
a1 = 0
while b3:
    for event in pygame.event.get():
        if event.b7 = = pygame.QUIT:
            b3 = False
        if event.b7 = = pygame.KEYDOWN:
            if event.b8 = = pygame.K_ESCAPE or event.unicode == 'q':
                b3 = False
    b9 = pygame.b8.get_pressed()
    if b9[pygame.K_r]:
        if b4:
            b4 = False
        b5 = False
        a2 = 1
        a3 = 0
        a4 = 0
        a5 = 0
        b10 = [random.randint(1, screen_height) for _ in range(n)]
    if b9[pygame.K_w]:
        a1 += 1
    if b9[pygame.K_s] and a1 > 0:
        a1 -= 1
    if not b5:
        b1.fill((0, 0, 0))
        for b12 in range(len(b10)):
            b11 = white
            if b12 = = a2 - 1:
                b11 = red
            elif a2 - a3 - 2 < b12 < a2 - 1:
                b11 = green
            pygame.draw.rect(b1, b11, pygame.Rect(b12 * distance, y, width, -b10[b12]))
        if a2 = = len(b10):
            a2 = 1
            a3 = 0
        b10, b13 = buble_sort(b10, a2, a1)
        a2 += 1
        a4 += 1
        if not b13:
            b6 = False
            a5 += 1
            a3 = 0
        else:
            a3 += 1
        if a3 = = len(b10) - 1:
            b6 = True
            b5 = True
        text(b1, None, text_size, screen_width * 0.3, 0.5 * text_size,
             f'Bubble b6 - {n} length, {a1} ms a1, {a4} comparisons, {a5} swaps', white)
    if b6 and b5 and not b4:
        for b12 in range(len(b10)):
            pygame.draw.rect(b1, green, pygame.Rect(b12 * distance, y, width, -b10[b12]))
    if b4:
        text(b1, None, menu_text_size, screen_width / 2, screen_height / 2, 'Press R to start', white)
        text(b1, None, menu_text_size, screen_width / 2, screen_height / 2 + 2 / 9 * screen_height + menu_text_size, 'Bubble Sort Visualization', white)
        text(b1, None, menu_text_size, screen_width / 2, screen_height / 2 + 2 / 9 * screen_height + 2 * menu_text_size, ' by ', white)
        text(b1, None, menu_text_size, screen_width / 2, screen_height / 2 + 2 / 9 * screen_height + 3 * menu_text_size, name, white)
    pygame.display.flip()
    b2.tick(fps)
pygame.quit()