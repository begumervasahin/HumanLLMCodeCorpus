import pygame
import random
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
WIDTH = 20
HEIGHT = 20
MARGIN = 0
grid = [[0 for _ in range(34)] for _ in range(24)]
pygame.init()
WINDOW_SIZE = [680, 480]
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("RANDOM MAZE")
done = False
clock = pygame.time.Clock()
frontier = []
i = random.randint(2, 21)
j = random.randint(2, 31)
grid[i][j] = 1
print(f"grid[{i}][{j}]")
def add_frontier(x, y):
    if 2 <= x < 22 and 2 <= y < 32 and grid[x][y] == 0:
        grid[x][y] = 2
        frontier.append((x, y))
add_frontier(i + 2, j)
add_frontier(i - 2, j)
add_frontier(i, j + 2)
add_frontier(i, j - 2)
def draw_grid():
    for row in range(24):
        for column in range(34):
            color = BLACK
            if grid[row][column] == 1:
                color = WHITE
            elif grid[row][column] == 2:
                color = RED
            pygame.draw.rect(screen, color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])
draw_grid()
pygame.display.flip()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    while frontier:
        f = random.randint(0, len(frontier) - 1)
        x, y = frontier[f]
        print(f"Selected frontier {x, y}")
        neighbors = []
        if grid[x - 2][y] == 1:
            neighbors.append((x - 2, y))
        if grid[x + 2][y] == 1:
            neighbors.append((x + 2, y))
        if grid[x][y - 2] == 1:
            neighbors.append((x, y - 2))
        if grid[x][y + 2] == 1:
            neighbors.append((x, y + 2))
        print(neighbors)
        if neighbors:
            p, q = random.choice(neighbors)
            print(f"Selected neighbor is {p, q}")
            grid[x][y] = 1
            if p == x:
                if q > y:
                    grid[x][y + 1] = 1
                else:
                    grid[x][y - 1] = 1
            else:
                if p > x:
                    grid[x + 1][y] = 1
                else:
                    grid[x - 1][y] = 1
        add_frontier(x + 2, y)
        add_frontier(x - 2, y)
        add_frontier(x, y + 2)
        add_frontier(x, y - 2)
        draw_grid()
        pygame.display.flip()
        del frontier[f]
    clock.tick(10)
pygame.quit()