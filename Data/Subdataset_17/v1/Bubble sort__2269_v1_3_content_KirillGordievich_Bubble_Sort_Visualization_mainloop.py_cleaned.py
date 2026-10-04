import pygame
import random
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
screen_width = 800
screen_height = 600
distance = 20
width = 15
y = screen_height
text_size = 24
menu_text_size = 36
fps = 30
n = 30
def bubble_sort(arr, j, delay):
    flag = False
    for i in range(len(arr) - j):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            flag = True
    pygame.time.wait(delay)
    return arr, flag
def text(screen, font, size, x, y, message, color):
    font = pygame.font.SysFont(font, size)
    text_surface = font.render(message, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Bubble Sort Visualization")
clock = pygame.time.Clock()
mainloop = True
first_start = True
done = False
sort = False
delay = 50
name = "Your Name"
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
        arr = [random.randint(1, screen_height) for _ in range(n)]
    if pressed[pygame.K_w]:
        delay += 1
    if pressed[pygame.K_s] and delay > 0:
        delay -= 1
    if not done:
        screen.fill((0, 0, 0))
        for i in range(len(arr)):
            if i == j - 1:
                pygame.draw.rect(screen, red, pygame.Rect(i * distance, y, width, -arr[i]))
            elif j - k - 2 < i < j - 1:
                pygame.draw.rect(screen, green, pygame.Rect(i * distance, y, width, -arr[i]))
            else:
                pygame.draw.rect(screen, white, pygame.Rect(i * distance, y, width, -arr[i]))
        if j == len(arr):
            j = 1
            k = 0
        arr, flag = bubble_sort(arr, j, delay)
        j += 1
        c += 1
        if not flag:
            sort = False
            s += 1
            k = 0
        else:
            k += 1
        if k == len(arr) - 1:
            sort = True
            done = True
        text(screen, None, text_size, screen_width * 0.3, 0.5 * text_size,
             f'Bubble sort - {n} length, {delay} ms delay, {c} comparisons, {s} swaps', white)
    if sort and done and not first_start:
        for i in range(len(arr)):
            pygame.draw.rect(screen, green, pygame.Rect(i * distance, y, width, -arr[i]))
    if first_start:
        text(screen, None, menu_text_size, screen_width / 2, screen_height / 2, 'Press R to start', white)
        text(screen, None, menu_text_size, screen_width / 2, screen_height / 2 + 2 / 9 * screen_height + menu_text_size,
             'Bubble Sort Visualization', white)
        text(screen, None, menu_text_size, screen_width / 2, screen_height / 2 + 2 / 9 * screen_height + 2 * menu_text_size,
             'by', white)
        text(screen, None, menu_text_size, screen_width / 2, screen_height / 2 + 2 / 9 * screen_height + 3 * menu_text_size,
             name, white)
    pygame.display.flip()
    clock.tick(fps)
pygame.quit()