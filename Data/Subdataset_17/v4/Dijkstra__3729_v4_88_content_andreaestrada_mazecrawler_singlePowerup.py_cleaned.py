import pygame
import spec
import powerup
class Single(powerup.PowerupGeneric):
    @staticmethod
    def generate_new_powerup(data, powerup_type):
        """
        Generate and return a new power-up of the specified type, and send its details to the server.
        Parameters:
        data: Data object used for server communication.
        powerup_type (str): Type of the power-up ("GhostAdded", "ThreeAdded", "PauseAdded").
        Returns:
        Single: An instance of the appropriate power-up class.
        """
        center_x, center_y = powerup.PowerupGeneric.generate_new_powerup_location()
        message = f"{powerup_type} {center_x} {center_y}\n"
        if data.server:
            data.server.send(message.encode())
        if powerup_type == "GhostAdded":
            return Ghost(center_x, center_y)
        elif powerup_type == "ThreeAdded":
            return Three(center_x, center_y)
        elif powerup_type == "PauseAdded":
            return Pause(center_x, center_y)
        else:
            raise ValueError(f"Unknown power-up type: {powerup_type}")
class Ghost(Single):
    def __init__(self, center_x, center_y):
        super().__init__(center_x, center_y, spec.ghost_images, spec.ghost_group, spec.cell_width / 2)
        pygame.sprite.Sprite.__init__(self)
class Three(Single):
    def __init__(self, center_x, center_y):
        super().__init__(center_x, center_y, spec.three_images, spec.three_group, spec.cell_width / 2)
        pygame.sprite.Sprite.__init__(self)
class Pause(Single):
    def __init__(self, center_x, center_y):
        super().__init__(center_x, center_y, spec.pause_images, spec.pause_group, spec.cell_width / 2)
        pygame.sprite.Sprite.__init__(self)