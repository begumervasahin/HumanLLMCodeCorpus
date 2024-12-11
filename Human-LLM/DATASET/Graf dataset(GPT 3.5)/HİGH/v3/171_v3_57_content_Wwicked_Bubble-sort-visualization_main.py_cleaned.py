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
        self.a3 = 5
        self.a4 = 5
        self.a5 = 0
        self.b4 = False
        self.b5 = True
        if self.b5:
            self.b6 = False
            self.b7 = False
            self.b8 = "Arial"
            self.b9 = True
            self.a6 = 14
            self.b10 = None
            self.a5 = round(self.a6 * 3)
        self.b11 = {
            "background": (140, 140, 140),
            "neutral_line": (220, 220, 220),
            "higher_line": (20, 200, 20),
            "background_iterations": (40, 40, 40),
            "numbers": (160, 0, 0),
            "highlight_numbers": (20, 200, 20),
            "error_message": (200, 0, 0)
        }
class class2:
    def fonk2(self, b12):
        self.b12 = b12
        self.b13 = []
        self.a7 = 0
        self.a8 = 0
        self.b14 = False
        self.a9 = 0
        self.a10 = 0
        self.a11 = 0
        self.a12 = 0
        self.a13 = 0
        self.fonk5()
        self.fonk3()
        self.fonk17()
    def fonk3(self):
        pygame.init()
        self.b15 = pygame.display.set_mode(self.b12.b1)
        pygame.display.set_caption(self.b12.b2)
        self.b16 = pygame.time.Clock()
        self.fonk4()
    def fonk4(self):
        if not self.b12.b5:
            return
        self.b12.b10 = pygame.b10.SysFont(self.b12.b8, self.b12.a6)
        self.b12.b10.set_bold(self.b12.b9)
    def fonk5(self):
        self.b13 = [random.randint(self.b12.b3[0], self.b12.b3[1]) for _ in range(self.b12.a1)]
        self.a8 = len(self.b13)
    def fonk6(self):
        return round((self.b12.b1[0] / self.a8) / 2)
    def fonk7(self, b17, width):
        return round((self.b12.b1[0] / self.a8) * b17) + self.b12.a3 + round(width / 2)
    def fonk8(self):
        return self.b12.b1[1] - self.b12.a4
    def fonk9(self, b17):
        if b17 = = self.a10:
            return self.b12.b11["higher_line"]
        return self.b12.b11["neutral_line"]
    def fonk10(self, b17):
        if self.b13[b17]:
            return self.b12.maximum_height - (self.b12.maximum_height * (self.b13[b17] / self.b12.b3[1])) + self.b12.a5
        else:
            return self.b12.b1[1] - self.b12.minimum_height - self.b12.a5
    def fonk11(self):
        self.b15.fill(self.b12.b11["background"])
    def fonk12(self):
        b18 = self.b12.b10.render(f"Iterations: {self.a11}", True, self.b12.b11["background_iterations"])
        self.fonk20(b18, round(self.b12.b1[0] / 2) + self.b12.a3 - round(b18.get_width() / 2), round(self.b12.b1[1] / 2))
    def fonk13(self, b17, b23):
        b18 = self.b12.b10.render(str(self.b13[b17]), True, self.b12.b11["highlight_numbers"] if self.a10 == b17 else self.b12.b11["numbers"])
        self.fonk20(b18, b23 - round(b18.get_width() / 2), b18.get_height())
    def fonk14(self, b17, b23):
        b19 = str(self.b13[b17])
        for i, char in enumerate(b19):
            b20 = self.b12.b10.render(char, True, self.b12.b11["numbers"])
            self.b15.blit(b20, (b23, b18.get_height() * i))
    def fonk15(self):
        b18 = self.b12.b10.render(f"Time elapsed: %0.2f" % (self.b14 and self.a13 - self.a12 or time.time() - self.a12), True, self.b12.b11["background_iterations"])
        self.fonk20(b18, round(self.b12.b1[0] / 2) + self.b12.a3 - round(b18.get_width() / 2), round(self.b12.b1[1] / 2) + b18.get_height())
    def fonk16(self, message):
        b18 = self.b12.b10.render(f"ERROR: {message}", True, self.b12.b11["error_message"])
        self.fonk20(b18, 0, 0)
    def fonk17(self):
        self.a12 = time.time()
        while True:
            self.b16.tick(self.b12.a2)
            for event in pygame.event.get():
                if event.b21 = = pygame.QUIT:
                    self.fonk22()
            if not self.b14:
                if self.a7 = = self.a8 - 1:
                    self.a7 = 0
                if self.a9 > self.a8:
                    self.fonk23()
                    if self.b12.b4:
                        break
                self.fonk21()
            self.fonk18()
            pygame.display.update()
    def fonk18(self):
        self.fonk11()
        for iterator in range(self.a8):
            b22 = self.fonk6()
            b23 = self.fonk7(iterator, b22)
            b24 = self.fonk8()
            b25 = self.fonk9(iterator)
            b26 = self.fonk10(iterator)
            self.fonk19(b23, b24, b26, b22, b25)
            if not self.b12.b5:
                continue
            self.fonk12()
            if not self.b12.b6:
                if self.b12.b7:
                    self.fonk14(iterator, b23)
                else:
                    self.fonk13(iterator, b23)
                self.fonk15()
    def fonk19(self, b23, b24, b26, b22, b25):
        pygame.draw.line(self.b15, b25, (b23, b24), (b23, b26), b22)
    def fonk20(self, b18, b23, b24, b27 = False, b19=""):
        if b27:
            for i, char in enumerate(b19):
                b20 = self.b12.b10.render(char, True, self.b12.b11["numbers"])
                self.b15.blit(b20, (b23, b24 + (b18.get_height() * i)))
        else:
            self.b15.blit(b18, (b23, b24))
    def fonk21(self):
        if self.a8 <= 1:
            self.fonk16(f"Invalid b13 length ({len(self.b13)})")
            self.fonk22()
        self.a10 = self.a7 + 1
        if self.b13[self.a7] > self.b13[self.a7 + 1]:
            self.b13[self.a7], self.b13[self.a7 + 1] = self.b13[self.a7 + 1], self.b13[self.a7]
            self.a9 = 0
        else:
            self.a9 += 1
        self.a7 += 1
        self.a11 += 1
    def fonk22(self):
        pygame.fonk22()
        fonk22()
    def fonk23(self):
        self.b14 = True
        self.a13 = time.time()
        print(f"Finished in {self.a11 + 1} a11.\nTime elapsed: {int(self.a13 - self.a12)}")
if b28 = = "__main__":
    b12 = class1()
    b29 = class2(b12)