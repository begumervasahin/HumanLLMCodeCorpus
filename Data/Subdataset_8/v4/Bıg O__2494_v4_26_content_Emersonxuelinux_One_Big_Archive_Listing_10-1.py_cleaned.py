import pygame
import sys
import random
skier_images = [
    "skier_down.png", "skier_right1.png", "skier_right2.png",
    "skier_left2.png", "skier_left1.png"
]
class Skier(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("skier_down.png")
        self.rect = self.image.get_rect(center=[320, 100])
        self.angle = 0
    def turn(self, direction):
        self.angle = max(min(self.angle + direction, 2), -2)
        center = self.rect.center
        self.image = pygame.image.load(skier_images[self.angle])
        self.rect = self.image.get_rect(center=center)
        speed = [self.angle, max(6 - abs(self.angle) * 2, 0)]
        return speed
    def move(self, speed):
        self.rect.centerx += speed[0]
        self.rect.centerx = min(max(self.rect.centerx, 20), 620)
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, image_file, location, obstacle_type):
        super().__init__()
        self.image_file = image_file
        self.image = pygame.image.load(image_file)
        self.location = location
        self.rect = self.image.get_rect(center=location)
        self.type = obstacle_type
        self.passed = False
    def scroll(self, terrain_pos):
        self.rect.centery = self.location[1] - terrain_pos
def create_map(start, end):
    obstacles = pygame.sprite.Group()
    locations = []
    for _ in range(10):
        row = random.randint(start, end)
        col = random.randint(0, 9)
        location = [col * 64 + 20, row * 64 + 20]
        if location not in locations:
            locations.append(location)
            obstacle_type = random.choice(["tree", "flag"])
            img = "skier_tree.png" if obstacle_type == "tree" else "skier_flag.png"
            obstacle = Obstacle(img, location, obstacle_type)
            obstacles.add(obstacle)
    return obstacles
def update_obstacle_group(map0, map1):
    obstacles = pygame.sprite.Group()
    for ob in map0:
        obstacles.add(ob)
    for ob in map1:
        obstacles.add(ob)
    return obstacles
pygame.init()
screen = pygame.display.set_mode([640, 640])
clock = pygame.time.Clock()
skier = Skier()
speed = [0, 6]
map_position = 0
points = 0
map0 = create_map(20, 29)
map1 = create_map(10, 19)
active_map = 0
obstacles = update_obstacle_group(map0, map1)
font = pygame.font.Font(None, 50)
def animate():
    screen.fill([255, 255, 255])
    pygame.display.update(obstacles.draw(screen))
    screen.blit(skier.image, skier.rect)
    screen.blit(score_text, [10, 10])
    pygame.display.flip()
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
    if map_position >= 640 and active_map == 0:
        active_map = 1
        map0 = create_map(20, 29)
        obstacles = update_obstacle_group(map0, map1)
    if map_position >= 1280 and active_map == 1:
        active_map = 0
        for obstacle in map0:
            obstacle.location[1] -= 1280
        map_position -= 1280
        map1 = create_map(10, 19)
        obstacles = update_obstacle_group(map0, map1)
    for obstacle in obstacles:
        obstacle.scroll(map_position)
    hit = pygame.sprite.spritecollide(skier, obstacles, False)
    if hit:
        if hit[0].type == "tree" and not hit[0].passed:
            points -= 100
            skier.image = pygame.image.load("skier_crash.png")
            animate()
            pygame.time.delay(1000)
            skier.image = pygame.image.load("skier_down.png")
            skier.angle = 0
            speed = [0, 6]
            hit[0].passed = True
        elif hit[0].type == "flag" and not hit[0].passed:
            points += 10
            obstacles.remove(hit[0])
    score_text = font.render("Score: " + str(points), 1, (0, 0, 0))
    animate()