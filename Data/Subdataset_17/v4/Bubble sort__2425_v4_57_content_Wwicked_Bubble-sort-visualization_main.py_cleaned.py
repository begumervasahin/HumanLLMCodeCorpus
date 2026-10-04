import pygame
import random
import time
class Config:
    def __init__(self):
        self.window_size = (1280, 720)
        self.window_title = "Bubble Sort Visualization"
        self.array_items = 25
        self.array_range = (0, 50)
        self.fps = 20
        self.min_height = 0
        self.max_height = self.window_size[1] - round(self.window_size[1] / 10)
        self.offset_x = 5
        self.offset_y = 5
        self.offset_y_top = 0
        self.close_after_sort = False
        self.font_render = True
        if self.font_render:
            self.render_iterations_only = False
            self.font_vertical = False
            self.font_type = "Arial"
            self.font_bold = True
            self.font_size = 14
            self.font = None
            self.offset_y_top = round(self.font_size * 3)
        self.color = {
            "background": (140, 140, 140),
            "neutral_line": (220, 220, 220),
            "higher_line": (20, 200, 20),
            "background_iterations": (40, 40, 40),
            "numbers": (160, 0, 0),
            "highlight_numbers": (20, 200, 20),
            "error_message": (200, 0, 0)
        }
class Visualization:
    def __init__(self, config):
        self.config = config
        self.array = []
        self.array_index = 0
        self.array_length = 0
        self.array_sorted = False
        self.sort_count = 0
        self.highlight = 0
        self.iterations = 0
        self.start_time = 0
        self.end_time = 0
        self.create_array()
        self.setup()
        self.main_loop()
    def setup(self):
        pygame.init()
        self.window = pygame.display.set_mode(self.config.window_size)
        pygame.display.set_caption(self.config.window_title)
        self.clock = pygame.time.Clock()
        self.setup_font()
    def setup_font(self):
        if not self.config.font_render:
            return
        self.config.font = pygame.font.SysFont(self.config.font_type, self.config.font_size)
        self.config.font.set_bold(self.config.font_bold)
    def create_array(self):
        self.array = [
            random.randint(self.config.array_range[0], self.config.array_range[1])
            for _ in range(self.config.array_items)
        ]
        self.array_length = len(self.array)
    def get_line_width(self):
        return round((self.config.window_size[0] / self.array_length) / 2)
    def get_line_x(self, line_index, width):
        return round((self.config.window_size[0] / self.array_length) * line_index) + self.config.offset_x + round(width / 2)
    def get_line_y(self):
        return self.config.window_size[1] - self.config.offset_y
    def get_line_color(self, line_index):
        return self.config.color["higher_line"] if line_index == self.highlight else self.config.color["neutral_line"]
    def get_line_end_y(self, line_index):
        if self.array[line_index]:
            return self.config.max_height - (self.config.max_height * (self.array[line_index] / self.config.array_range[1])) + self.config.offset_y_top
        else:
            return self.config.window_size[1] - self.config.min_height - self.config.offset_y_top
    def draw_background(self):
        self.window.fill(self.config.color["background"])
    def draw_iterations(self):
        text = self.config.font.render(f"Iterations: {self.iterations}", True, self.config.color["background_iterations"])
        self.draw_text(text, round(self.config.window_size[0] / 2) + self.config.offset_x - round(text.get_width() / 2), round(self.config.window_size[1] / 2))
    def draw_horizontal_numbers(self, line_index, x):
        text = self.config.font.render(str(self.array[line_index]), True, self.highlight == line_index and self.config.color["highlight_numbers"] or self.config.color["numbers"])
        self.draw_text(text, x - round(text.get_width() / 2), text.get_height())
    def draw_vertical_numbers(self, line_index, x):
        plain_text = str(self.array[line_index])
        text = self.config.font.render(str(self.array[line_index]), True, self.highlight == line_index and self.config.color["highlight_numbers"] or self.config.color["numbers"])
        self.draw_text(text, x, 0, True, plain_text)
    def draw_time_elapsed(self):
        elapsed_time = self.end_time - self.start_time if self.array_sorted else time.time() - self.start_time
        text = self.config.font.render(f"Time elapsed: {elapsed_time:.2f} sec", True, self.config.color["background_iterations"])
        self.draw_text(text, round(self.config.window_size[0] / 2) + self.config.offset_x - round(text.get_width() / 2), round(self.config.window_size[1] / 2) + text.get_height())
    def draw_error(self, message):
        text = self.config.font.render(f"ERROR: {message}", True, self.config.color["error_message"])
        self.draw_text(text, 0, 0)
    def main_loop(self):
        self.start_time = time.time()
        while True:
            self.clock.tick(self.config.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
            if not self.array_sorted:
                if self.array_index == self.array_length - 1:
                    self.array_index = 0
                if self.sort_count > self.array_length:
                    self.finish()
                    if self.config.close_after_sort:
                        break
                self.sort()
            self.draw()
            pygame.display.update()
    def draw(self):
        self.draw_background()
        for i in range(self.array_length):
            line_width = self.get_line_width()
            line_x = self.get_line_x(i, line_width)
            line_y = self.get_line_y()
            line_color = self.get_line_color(i)
            line_end_y = self.get_line_end_y(i)
            self.draw_line(line_x, line_y, line_end_y, line_width, line_color)
            if self.config.font_render:
                self.draw_iterations()
                if not self.config.render_iterations_only:
                    if self.config.font_vertical:
                        self.draw_vertical_numbers(i, line_x)
                    else:
                        self.draw_horizontal_numbers(i, line_x)
                    self.draw_time_elapsed()
    def draw_line(self, x, y, end_y, width, color):
        pygame.draw.line(self.window, color, (x, y), (x, end_y), width)
    def draw_text(self, text, x, y, vertical=False, plain_text=""):
        if vertical:
            for i, char in enumerate(plain_text):
                temp_text = self.config.font.render(char, True, self.config.color["numbers"])
                self.window.blit(temp_text, (x, y + (temp_text.get_height() * i)))
        else:
            self.window.blit(text, (x, y))
    def sort(self):
        if self.array_length <= 1:
            self.draw_error(f"Invalid array length ({len(self.array)})")
            self.quit()
        self.highlight = self.array_index + 1
        if self.array[self.array_index] > self.array[self.array_index + 1]:
            self.array[self.array_index], self.array[self.array_index + 1] = self.array[self.array_index + 1], self.array[self.array_index]
            self.sort_count = 0
        else:
            self.sort_count += 1
        self.array_index += 1
        self.iterations += 1
    def quit(self):
        pygame.quit()
        quit()
    def finish(self):
        self.array_sorted = True
        self.end_time = time.time()
        print(f"Finished in {self.iterations + 1} iterations.\nTime elapsed: {int(self.end_time - self.start_time)} seconds.")
if __name__ == "__main__":
    config = Config()
    Visualization(config)