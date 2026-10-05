from colors import white, red, green
from functions import *
from settings import *
pygame.init()
b1 = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Bubble Sort Visualization")
b2 = pygame.time.Clock()
while b4:
    for event in pygame.event.get():
        if event.b3 = = pygame.QUIT:
            b4 = False
        if event.b3 = = pygame.KEYDOWN:
            if event.b5 = = pygame.K_ESCAPE or event.unicode == 'q':
                b4 = False
    b6 = pygame.b5.get_pressed()
    if b6[pygame.K_r]:
        if b7 is True:
            b7 = False
        b8 = False
        a1 = 1
        a2 = 0
        a3 = 0
        a4 = 0
        b9 = [randint(1, screen_height) for p in range(0, n)]
    if b6[pygame.K_w]:
        delay += 1
    if b6[pygame.K_s] and delay > 0:
        delay -= 1
    if b8 is False:
        b1.fill((0, 0, 0))
        for b10 in range(len(b9)):
            if b10 = = a1 - 1:
                pygame.draw.rect(b1, red,
                                 pygame.Rect(b10 * distance, y, width, -b9[b10]))
            elif b10 > a1 - a2 - 2 and b10 < a1 - 1:
                pygame.draw.rect(b1, green,
                                 pygame.Rect(b10 * distance, y, width, -b9[b10]))
            else:
                pygame.draw.rect(b1, white,
                                 pygame.Rect(b10 * distance, y, width, -b9[b10]))
        if a1 = = len(b9):
            a1 = 1
            a2 = 0
        b9, b11 = buble_sort(b9, a1, delay)
        a1 += 1
        a3 += 1
        if b11 is False:
            b12 = False
            a4 += 1
            a2 = 0
        else:
            a2 += 1
        if a2 = = len(b9)-1:
            print(a2)
            b12 = True
            b8 = True
        text(b1, None, text_size, screen_width*0.3, 0.5*text_size,
             'Bubble b12 - %a4 length, %a4 ms delay, %a4 comparisons, '
             '%a4 swaps' % (n, delay, a3, a4), white)
    if b12 is True and b8 is True and b7 is False:
        for b10 in range(len(b9)):
            pygame.draw.rect(b1, green, pygame.Rect(b10 * distance, y, width, -b9[b10]))
    if b7 is True:
        text(b1, None, menu_text_size, screen_width/2,
             screen_height/2, 'Press R for start', white)
        text(b1, None, menu_text_size, screen_width/2,
             screen_height/2 + 2/9*screen_height + menu_text_size,
             'Bubble Sort Visualization', white)
        text(b1, None, menu_text_size, screen_width/2,
             screen_height/2 + 2/9*screen_height + 2*menu_text_size,
             ' by ', white)
        text(b1, None, menu_text_size, screen_width/2,
             screen_height/2 + 2/9*screen_height + 3*menu_text_size,
             '%a4' % name, white)
    pygame.display.flip()
    b2.tick(fps)
pygame.quit()