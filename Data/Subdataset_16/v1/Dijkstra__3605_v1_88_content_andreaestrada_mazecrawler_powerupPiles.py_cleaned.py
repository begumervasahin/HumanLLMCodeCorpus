import pygame
from random import randint
import spec
import powerup
class class1(powerup.PowerupGeneric):
    def fonk1(self, centerX, b2, b1, images, group, size):
        pygame.sprite.Sprite.fonk4(self)
        super().fonk4(centerX, b2, images, group, size)
        self.b1 = b1
    @staticmethod
    def fonk2(data, b4):
        """
        Generate a new power-up based on the type and send its data.
        Parameters:
        data: Data object for server communication.
        b4 (str): Type of the power-up ("AmmoAdded" or "PointsAdded").
        """
        centerX, b2 = powerup.PowerupGeneric.generate_new_powerup_location()
        b1 = randint(3, 7)
        b3 = f"{b4} {centerX} {b2} {b1}\n"
        data.server.send(b3.encode())
        if b4 = = "AmmoAdded":
            class2(centerX, b2, b1)
        elif b4 = = "PointsAdded":
            class3(centerX, b2, b1)
class class2(class1):
    def fonk3(self, centerX, b2, b1):
        pygame.sprite.Sprite.fonk4(self)
        super().fonk4(centerX, b2, b1, spec.ammo_pile_images, spec.static_ammos, spec.cell_width / 3)
class class3(class1):
    def fonk4(self, centerX, b2, b1):
        pygame.sprite.Sprite.fonk4(self)
        super().fonk4(centerX, b2, b1, spec.point_pile_images, spec.static_points, spec.cell_width / 3)