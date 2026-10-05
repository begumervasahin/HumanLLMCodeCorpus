import pygame
from random import randint
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
def bubble_sort(arr, j, delay):
    n = len(arr)
    swapped = False
    for i in range(n - j):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            swapped = True
            pygame.time.wait(delay)
    return arr, swapped
def draw_text(screen, font, size, x, y, text, color):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Bubble Sort Visualization")
clock = pygame.time.Clock()
mainloop = True
first_start = True
done = False
j = 1
k = 0
c = 0
s = 0
n = 100
delay = 10
width = 4
distance = 8
y = SCREEN_HEIGHT
lst = [randint(1, SCREEN_HEIGHT) for _ in range(n)]
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
        j = 1
        k = 0
        c = 0
        s = 0
        lst = [randint(1, SCREEN_HEIGHT) for _ in range(n)]
    if pressed[pygame.K_w]:
        delay += 1
    if pressed[pygame.K_s] and delay > 0:
        delay -= 1
    if done is False:
        screen.fill((0, 0, 0))
        for i in range(len(lst)):
            if i == j - 1:
                pygame.draw.rect(screen, RED, pygame.Rect(i * distance, y, width, -lst[i]))
            elif i > j - k - 2 and i < j - 1:
                pygame.draw.rect(screen, GREEN, pygame.Rect(i * distance, y, width, -lst[i]))
            else:
                pygame.draw.rect(screen, WHITE, pygame.Rect(i * distance, y, width, -lst[i]))
        if j == len(lst):
            j = 1
            k = 0
        lst, flag = bubble_sort(lst, j, delay)
        j += 1
        c += 1
        if flag is False:
            s += 1
            k = 0
        else:
            k += 1
        if k == len(lst) - 1:
            print(k)
            done = True
        draw_text(screen, None, 24, SCREEN_WIDTH * 0.3, 0.5 * 24,
                  f'Bubble sort - {n} length, {delay} ms delay, {c} comparisons, {s} swaps', WHITE)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()