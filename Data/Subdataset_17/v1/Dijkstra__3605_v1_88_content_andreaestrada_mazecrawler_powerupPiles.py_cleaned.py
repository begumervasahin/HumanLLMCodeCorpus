import pygame
from random import randint
import spec
import powerup
class Piles(powerup.PowerupGeneric):
    def __init__(self, centerX, centerY, amount, images, group, size):
        pygame.sprite.Sprite.__init__(self)
        super().__init__(centerX, centerY, images, group, size)
        self.amount = amount
    @staticmethod
    def generate_new_powerup(data, type_added):
        """
        Generate a new power-up based on the type and send its data.
        Parameters:
        data: Data object for server communication.
        type_added (str): Type of the power-up ("AmmoAdded" or "PointsAdded").
        """
        centerX, centerY = powerup.PowerupGeneric.generate_new_powerup_location()
        amount = randint(3, 7)
        msg = f"{type_added} {centerX} {centerY} {amount}\n"
        data.server.send(msg.encode())
        if type_added == "AmmoAdded":
            AmmoPile(centerX, centerY, amount)
        elif type_added == "PointsAdded":
            PointPile(centerX, centerY, amount)
class AmmoPile(Piles):
    def __init__(self, centerX, centerY, amount):
        pygame.sprite.Sprite.__init__(self)
        super().__init__(centerX, centerY, amount, spec.ammo_pile_images, spec.static_ammos, spec.cell_width / 3)
class PointPile(Piles):
    def __init__(self, centerX, centerY, amount):
        pygame.sprite.Sprite.__init__(self)
        super().__init__(centerX, centerY, amount, spec.point_pile_images, spec.static_points, spec.cell_width / 3)