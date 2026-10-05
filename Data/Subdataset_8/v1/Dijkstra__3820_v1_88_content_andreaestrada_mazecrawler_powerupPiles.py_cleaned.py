import pygame
from random import randint
import spec
import powerup
class Piles(powerup.PowerupGeneric):
    def __init__(self, centerX, centerY, amount, images, group, size):
        super().__init__(centerX, centerY, images, group, size)
        self.amount = amount
    @staticmethod
    def generateNewPowerup(data, typeAdded):
        centerX, centerY = powerup.PowerupGeneric.generateNewPowerupLocation()
        amount = randint(3,7)
        msg = f"{typeAdded} {centerX} {centerY} {amount}\n"
        data.server.send(msg.encode())
        if typeAdded == "AmmoAdded":
            AmmoPile(centerX, centerY, amount)
        elif typeAdded == "PointsAdded":
            PointPile(centerX, centerY, amount)
class AmmoPile(Piles):
    def __init__(self, centerX, centerY, amount):
        super().__init__(centerX, centerY, amount, spec.ammoPileImages, spec.staticAmmos, spec.cellWidth/3)
class PointPile(Piles):
    def __init__(self, centerX, centerY, amount):
        super().__init__(centerX, centerY, amount, spec.pointPileImages, spec.staticPoints, spec.cellWidth/3)
pygame.init()
data = pygame.Surface((800, 600))
Piles.generateNewPowerup(data, "AmmoAdded")
Piles.generateNewPowerup(data, "PointsAdded")