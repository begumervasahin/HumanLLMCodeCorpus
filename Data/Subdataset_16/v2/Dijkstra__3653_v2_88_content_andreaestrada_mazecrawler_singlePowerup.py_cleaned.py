import pygame
import spec
import powerup
class class1(powerup.PowerupGeneric):
    @staticmethod
    def fonk1(data, b3):
        """
        Generate a new power-up of the specified type and send its details to the server.
        Parameters:
        data: Data object used for server communication.
        b3 (str): Type of the power-up ("GhostAdded", "ThreeAdded", "PauseAdded").
        Returns:
        class1: An instance of class2, class3, or class4 based on the power-up type.
        """
        center_x, b1 = powerup.PowerupGeneric.generate_new_powerup_location()
        b2 = f"{b3} {center_x} {b1}\n"
        if data.server:
            data.server.send(b2.encode())
        if b3 = = "GhostAdded":
            return class2(center_x, b1)
        elif b3 = = "ThreeAdded":
            return class3(center_x, b1)
        elif b3 = = "PauseAdded":
            return class4(center_x, b1)
        else:
            raise ValueError(f"Unknown power-up type: {b3}")
class class2(class1):
    def fonk2(self, center_x, b1):
        super().fonk4(center_x, b1, spec.ghost_images, spec.ghost_group, spec.cell_width / 2)
class class3(class1):
    def fonk3(self, center_x, b1):
        super().fonk4(center_x, b1, spec.three_images, spec.three_group, spec.cell_width / 2)
class class4(class1):
    def fonk4(self, center_x, b1):
        super().fonk4(center_x, b1, spec.pause_images, spec.pause_group, spec.cell_width / 2)