from colors import white, red, green
from functions import *
from settings import *
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Bubble Sort Visualization")
clock = pygame.time.Clock()
while mainloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.unicode == 'q':
                mainloop = False
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_r]:
        if first_start is True:
            first_start = False
        done = False
        j = 1
        k = 0
        c = 0
        s = 0
        list = [randint(1, screen_height) for p in range(0, n)]
    if pressed[pygame.K_w]:
        delay += 1
    if pressed[pygame.K_s] and delay > 0:
        delay -= 1
    if done is False:
        screen.fill((0, 0, 0))
        for i in range(len(list)):
            if i == j - 1:
                pygame.draw.rect(screen, red,
                                 pygame.Rect(i * distance, y, width, -list[i]))
            elif i > j - k - 2 and i < j - 1:
                pygame.draw.rect(screen, green,
                                 pygame.Rect(i * distance, y, width, -list[i]))
            else:
                pygame.draw.rect(screen, white,
                                 pygame.Rect(i * distance, y, width, -list[i]))
        if j == len(list):
            j = 1
            k = 0
        list, flag = buble_sort(list, j, delay)
        j += 1
        c += 1
        if flag is False:
            sort = False
            s += 1
            k = 0
        else:
            k += 1
        if k == len(list)-1:
            print(k)
            sort = True
            done = True
        text(screen, None, text_size, screen_width*0.3, 0.5*text_size,
             'Bubble sort - %s length, %s ms delay, %s comparisons, '
             '%s swaps' % (n, delay, c, s), white)
    if sort is True and done is True and first_start is False:
        for i in range(len(list)):
            pygame.draw.rect(screen, green, pygame.Rect(i * distance, y, width, -list[i]))
    if first_start is True:
        text(screen, None, menu_text_size, screen_width/2,
             screen_height/2, 'Press R for start', white)
        text(screen, None, menu_text_size, screen_width/2,
             screen_height/2 + 2/9*screen_height + menu_text_size,
             'Bubble Sort Visualization', white)
        text(screen, None, menu_text_size, screen_width/2,
             screen_height/2 + 2/9*screen_height + 2*menu_text_size,
             ' by ', white)
        text(screen, None, menu_text_size, screen_width/2,
             screen_height/2 + 2/9*screen_height + 3*menu_text_size,
             '%s' % name, white)
    pygame.display.flip()
    clock.tick(fps)
pygame.quit()