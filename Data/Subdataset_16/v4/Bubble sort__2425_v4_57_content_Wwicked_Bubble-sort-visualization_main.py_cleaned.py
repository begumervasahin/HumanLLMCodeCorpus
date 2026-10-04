import pygame
import random
import time
class class1:
    def fonk1(self):
        self.b1 = (1280, 720)
        self.b2 = "Bubble Sort class2"
        self.a1 = 25
        self.b3 = (0, 50)
        self.a2 = 20
        self.a3 = 0
        self.b4 = self.b1[1] - round(self.b1[1] / 10)
        self.a4 = 5
        self.a5 = 5
        self.a6 = 0
        self.b5 = False
        self.b6 = True
        if self.b6:
            self.b7 = False
            self.b8 = False
            self.b9 = "Arial"
            self.b10 = True
            self.a7 = 14
            self.b11 = None
            self.a6 = round(self.a7 * 3)
        self.b12 = {
            "background": (140, 140, 140),
            "neutral_line": (220, 220, 220),
            "higher_line": (20, 200, 20),
            "background_iterations": (40, 40, 40),
            "numbers": (160, 0, 0),
            "highlight_numbers": (20, 200, 20),
            "error_message": (200, 0, 0)
        }
class class2:
    def fonk2(self, b13):
        self.b13 = b13
        self.b14 = []
        self.a8 = 0
        self.a9 = 0
        self.b15 = False
        self.a10 = 0
        self.a11 = 0
        self.a12 = 0
        self.a13 = 0
        self.a14 = 0
        self.fonk5()
        self.fonk3()
        self.fonk17()
    def fonk3(self):
        pygame.init()
        self.b16 = pygame.display.set_mode(self.b13.b1)
        pygame.display.set_caption(self.b13.b2)
        self.b17 = pygame.time.Clock()
        self.fonk4()
    def fonk4(self):
        if not self.b13.b6:
            return
        self.b13.b11 = pygame.b11.SysFont(self.b13.b9, self.b13.a7)
        self.b13.b11.set_bold(self.b13.b10)
    def fonk5(self):
        self.b14 = [
            random.randint(self.b13.b3[0], self.b13.b3[1])
            for _ in range(self.b13.a1)
        ]
        self.a9 = len(self.b14)
    def fonk6(self):
        return round((self.b13.b1[0] / self.a9) / 2)
    def fonk7(self, b18, width):
        return round((self.b13.b1[0] / self.a9) * b18) + self.b13.a4 + round(width / 2)
    def fonk8(self):
        return self.b13.b1[1] - self.b13.a5
    def fonk9(self, b18):
        return self.b13.b12["higher_line"] if b18 = = self.a11 else self.b13.b12["neutral_line"]
    def fonk10(self, b18):
        if self.b14[b18]:
            return self.b13.b4 - (self.b13.b4 * (self.b14[b18] / self.b13.b3[1])) + self.b13.a6
        else:
            return self.b13.b1[1] - self.b13.a3 - self.b13.a6
    def fonk11(self):
        self.b16.fill(self.b13.b12["background"])
    def fonk12(self):
        b19 = self.b13.b11.render(f"Iterations: {self.a12}", True, self.b13.b12["background_iterations"])
        self.fonk20(b19, round(self.b13.b1[0] / 2) + self.b13.a4 - round(b19.get_width() / 2), round(self.b13.b1[1] / 2))
    def fonk13(self, b18, x):
        b19 = self.b13.b11.render(str(self.b14[b18]), True, self.a11 == b18 and self.b13.b12["highlight_numbers"] or self.b13.b12["numbers"])
        self.fonk20(b19, x - round(b19.get_width() / 2), b19.get_height())
    def fonk14(self, b18, x):
        b20 = str(self.b14[b18])
        b19 = self.b13.b11.render(str(self.b14[b18]), True, self.a11 == b18 and self.b13.b12["highlight_numbers"] or self.b13.b12["numbers"])
        self.fonk20(b19, x, 0, True, b20)
    def fonk15(self):
        b21 = self.a14 - self.a13 if self.b15 else time.time() - self.a13
        b19 = self.b13.b11.render(f"Time elapsed: {b21:.2f} sec", True, self.b13.b12["background_iterations"])
        self.fonk20(b19, round(self.b13.b1[0] / 2) + self.b13.a4 - round(b19.get_width() / 2), round(self.b13.b1[1] / 2) + b19.get_height())
    def fonk16(self, message):
        b19 = self.b13.b11.render(f"ERROR: {message}", True, self.b13.b12["error_message"])
        self.fonk20(b19, 0, 0)
    def fonk17(self):
        self.a13 = time.time()
        while True:
            self.b17.tick(self.b13.a2)
            for event in pygame.event.get():
                if event.b22 = = pygame.QUIT:
                    self.fonk22()
            if not self.b15:
                if self.a8 = = self.a9 - 1:
                    self.a8 = 0
                if self.a10 > self.a9:
                    self.fonk23()
                    if self.b13.b5:
                        break
                self.fonk21()
            self.fonk18()
            pygame.display.update()
    def fonk18(self):
        self.fonk11()
        for i in range(self.a9):
            b23 = self.fonk6()
            b24 = self.fonk7(i, b23)
            b25 = self.fonk8()
            b26 = self.fonk9(i)
            b27 = self.fonk10(i)
            self.fonk19(b24, b25, b27, b23, b26)
            if self.b13.b6:
                self.fonk12()
                if not self.b13.b7:
                    if self.b13.b8:
                        self.fonk14(i, b24)
                    else:
                        self.fonk13(i, b24)
                    self.fonk15()
    def fonk19(self, x, y, end_y, width, b12):
        pygame.draw.line(self.b16, b12, (x, y), (x, end_y), width)
    def fonk20(self, b19, x, y, b28 = False, b20=""):
        if b28:
            for i, char in enumerate(b20):
                b29 = self.b13.b11.render(char, True, self.b13.b12["numbers"])
                self.b16.blit(b29, (x, y + (b29.get_height() * i)))
        else:
            self.b16.blit(b19, (x, y))
    def fonk21(self):
        if self.a9 <= 1:
            self.fonk16(f"Invalid b14 length ({len(self.b14)})")
            self.fonk22()
        self.a11 = self.a8 + 1
        if self.b14[self.a8] > self.b14[self.a8 + 1]:
            self.b14[self.a8], self.b14[self.a8 + 1] = self.b14[self.a8 + 1], self.b14[self.a8]
            self.a10 = 0
        else:
            self.a10 += 1
        self.a8 += 1
        self.a12 += 1
    def fonk22(self):
        pygame.fonk22()
        fonk22()
    def fonk23(self):
        self.b15 = True
        self.a14 = time.time()
        print(f"Finished in {self.a12 + 1} a12.\nTime elapsed: {int(self.a14 - self.a13)} seconds.")
if b30 = = "__main__":
    b13 = class1()
    class2(b13)