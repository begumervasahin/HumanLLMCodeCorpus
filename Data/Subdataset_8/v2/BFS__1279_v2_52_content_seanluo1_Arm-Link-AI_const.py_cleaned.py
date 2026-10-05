import pygame
import sys
from pygame.locals import *
CONFIG_FILE = "config.txt"
MAX_NUM_OF_ART_LINKS = 3
ARM_LINKS_WIDTH = [5, 3, 1]
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WALL_CHAR = '%'
START_CHAR = 'P'
OBJECTIVE_CHAR = '.'
SPACE_CHAR = ' '
ALPHA = 0
BETA = 1
GAMMA = 2
DEFAULT_FPS = 30
DEFAULT_GRANULARITY = 2
class ArmLinkAI:
    def __init__(self):
        self.config_file = CONFIG_FILE
        self.max_num_of_art_links = MAX_NUM_OF_ART_LINKS
        self.arm_links_width = ARM_LINKS_WIDTH
        self.colors = [BLACK, WHITE, RED, BLUE]
        self.wall_char = WALL_CHAR
        self.start_char = START_CHAR
        self.objective_char = OBJECTIVE_CHAR
        self.space_char = SPACE_CHAR
        self.alpha = ALPHA
        self.beta = BETA
        self.gamma = GAMMA
        self.default_fps = DEFAULT_FPS
        self.default_granularity = DEFAULT_GRANULARITY
    def play_game(self):
        pygame.init()
        fps_clock = pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
            fps_clock.tick(self.default_fps)
if __name__ == '__main__':
    arm_link_ai = ArmLinkAI()
    arm_link_ai.play_game()