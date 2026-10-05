import pygame
import sys
import random
SKIER_IMAGES = [
    "skier_down.png", "skier_right1.png", "skier_right2.png",
    "skier_left2.png", "skier_left1.png"
]
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 640
SKIER_START_POS = [320, 100]
MIN_X_POS = 20
MAX_X_POS = 620
OBSTACLE_ROWS = {"map0": (20, 29), "map1": (10, 19)}
class Skier(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("skier_down.png")
        self.rect = self.image.get_rect(center=SKIER_START_POS)
        self.angle = 0
    def turn(self, direction):
        self.angle = max(min(self.angle + direction, 2), -2)
        center = self.rect.center
        self.image = pygame.image.load(SKIER_IMAGES[self.angle])
        self.rect = self.image.get_rect(center=center)
        speed = [self.angle, max(6 - abs(self.angle) * 2, 0)]
        return speed
    def move(self, speed):
        self.rect.centerx += speed[0]
        self.rect.centerx = min(max(self.rect.centerx, MIN_X_POS), MAX_X_POS)
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, image_file, location, obstacle_type):
        super().__init__()
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect(center=location)
        self.type = obstacle_type
        self.passed = False
    def scroll(self, terrain_pos):
        self.rect.centery = self.rect.centery - terrain_pos
def create_obstacles():
    obstacles = pygame.sprite.Group()
    locations = []
    for _ in range(10):
        row = random.randint(*OBSTACLE_ROWS[current_map])
        col = random.randint(0, 9)
        location = [col * 64 + 20, row * 64 + 20]
        if location not in locations:
            locations.append(location)
            obstacle_type = random.choice(["tree", "flag"])
            img = "skier_tree.png" if obstacle_type == "tree" else "skier_flag.png"
            obstacle = Obstacle(img, location, obstacle_type)
            obstacles.add(obstacle)
    return obstacles
pygame.init()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
clock = pygame.time.Clock()
skier = Skier()
speed = [0, 6]
map_position = 0
points = 0
current_map = "map0"
obstacles = create_obstacles()
font = pygame.font.Font(None, 50)
while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed = skier.turn(-1)
            elif event.key == pygame.K_RIGHT:
                speed = skier.turn(1)
    skier.move(speed)
    map_position += speed[1]
    if map_position >= SCREEN_WIDTH and current_map == "map0":
        current_map = "map1"
        obstacles = create_obstacles()
    if map_position >= SCREEN_WIDTH * 2 and current_map == "map1":
        current_map = "map0"
        for obstacle in obstacles:
            obstacle.rect.centery -= SCREEN_WIDTH
        map_position -= SCREEN_WIDTH
        obstacles = create_obstacles()
    for obstacle in obstacles:
        obstacle.scroll(map_position)
    hit = pygame.sprite.spritecollide(skier, obstacles, False)
    if hit:
        if hit[0].type == "tree" and not hit[0].passed:
            points -= 100
            skier.image = pygame.image.load("skier_crash.png")
            pygame.time.delay(1000)
            skier.image = pygame.image.load("skier_down.png")
            skier.angle = 0
            speed = [0, 6]
            hit[0].passed = True
        elif hit[0].type == "flag" and not hit[0].passed:
            points += 10
            obstacles.remove(hit[0])
    score_text = font.render("Score: " + str(points), 1, (0, 0, 0))
    screen.fill([255, 255, 255])
    screen.blit(score_text, [10, 10])
    screen.blit(skier.image, skier.rect)
    pygame.display.flip()