import pygame
from random import randint
import spec
import powerup
class class1(powerup.PowerupGeneric):
    def fonk1(self, centerX, b2, b1, images, group, size):
        super().fonk4(centerX, b2, images, group, size)
        self.b1 = b1
    @staticmethod
    def fonk2(b5, b4):
        centerX, b2 = powerup.PowerupGeneric.generateNewPowerupLocation()
        b1 = randint(3, 7)
        b3 = f"{b4} {centerX} {b2} {b1}\n"
        b5.server.send(b3.encode())
        if b4 = = "AmmoAdded":
            class2(centerX, b2, b1)
        elif b4 = = "PointsAdded":
            class3(centerX, b2, b1)
class class2(class1):
    def fonk3(self, centerX, b2, b1):
        super().fonk4(centerX, b2, b1, spec.ammoPileImages, spec.staticAmmos, spec.cellWidth/3)
class class3(class1):
    def fonk4(self, centerX, b2, b1):
        super().fonk4(centerX, b2, b1, spec.pointPileImages, spec.staticPoints, spec.cellWidth/3)
pygame.init()
b5 = pygame.Surface((800, 600))
class1.fonk2(b5, "AmmoAdded")
class1.fonk2(b5, "PointsAdded")