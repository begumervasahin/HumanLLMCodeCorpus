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
        Generate a new power-up based on its type and send its data to the server.
        Parameters:
        data: Data object for server communication.
        type_added (str): Type of the power-up ("AmmoAdded" or "PointsAdded").
        """
        centerX, centerY = powerup.PowerupGeneric.generate_new_powerup_location()
        amount = randint(3, 7)
        message = f"{type_added} {centerX} {centerY} {amount}\n"
        data.server.send(message.encode())
        if type_added == "AmmoAdded":
            return AmmoPile(centerX, centerY, amount)
        elif type_added == "PointsAdded":
            return PointPile(centerX, centerY, amount)
        else:
            raise ValueError(f"Unknown power-up type: {type_added}")
class AmmoPile(Piles):
    def __init__(self, centerX, centerY, amount):
        images = spec.ammo_pile_images
        group = spec.static_ammos
        size = spec.cell_width / 3
        super().__init__(centerX, centerY, amount, images, group, size)
class PointPile(Piles):
    def __init__(self, centerX, centerY, amount):
        images = spec.point_pile_images
        group = spec.static_points
        size = spec.cell_width / 3
        super().__init__(centerX, centerY, amount, images, group, size)