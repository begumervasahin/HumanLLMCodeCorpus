import pygame
import random
from colors import white, red, green
from functions import bubble_sort, text
from settings import (
    screen_width, screen_height, distance, y, width, n,
    text_size, menu_text_size, name, fps
)
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Bubble Sort Visualization")
clock = pygame.time.Clock()
mainloop = True
first_start = True
done = False
sort = False
delay = 0
def reset_sorting():
    global lst, j, k, c, s
    lst = [random.randint(1, screen_height) for _ in range(n)]
    j = 1
    k = 0
    c = 0
    s = 0
def draw_list(lst, j, k):
    for i in range(len(lst)):
        color = white
        if i == j - 1:
            color = red
        elif j - k - 2 < i < j - 1:
            color = green
        pygame.draw.rect(screen, color, pygame.Rect(i * distance, y, width, -lst[i]))
def display_text():
    text(
        screen, None, text_size, screen_width * 0.3, 0.5 * text_size,
        f'Bubble sort - {n} length, {delay} ms delay, {c} comparisons, {s} swaps', white
    )
def display_menu():
    text(screen, None, menu_text_size, screen_width / 2, screen_height / 2, 'Press R to start', white)
    text(
        screen, None, menu_text_size, screen_width / 2, screen_height / 2 + 2 / 9 * screen_height + menu_text_size,
        'Bubble Sort Visualization', white
    )
    text(screen, None, menu_text_size, screen_width / 2, screen_height / 2 + 2 / 9 * screen_height + 2 * menu_text_size, ' by ', white)
    text(screen, None, menu_text_size, screen_width / 2, screen_height / 2 + 2 / 9 * screen_height + 3 * menu_text_size, name, white)
while mainloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.unicode == 'q':
                mainloop = False
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_r]:
        if first_start:
            first_start = False
        done = False
        reset_sorting()
    if pressed[pygame.K_w]:
        delay += 1
    if pressed[pygame.K_s] and delay > 0:
        delay -= 1
    if not done:
        screen.fill((0, 0, 0))
        draw_list(lst, j, k)
        if j == len(lst):
            j = 1
            k = 0
        lst, flag = bubble_sort(lst, j, delay)
        j += 1
        c += 1
        if not flag:
            sort = False
            s += 1
            k = 0
        else:
            k += 1
        if k == len(lst) - 1:
            sort = True
            done = True
        display_text()
    if sort and done and not first_start:
        for i in range(len(lst)):
            pygame.draw.rect(screen, green, pygame.Rect(i * distance, y, width, -lst[i]))
    if first_start:
        display_menu()
    pygame.display.flip()
    clock.tick(fps)
pygame.quit()