import pygame
import spec
import powerup
class class1(powerup.PowerupGeneric):
    @staticmethod
    def fonk1(data, b3):
        center_x, b1 = powerup.PowerupGeneric.generate_new_powerup_location()
        b2 = "%s %d %d\n" % (b3, center_x, b1)
        if data.server is not None:
            data.server.send(b2.encode())
        if b3 = = "GhostAdded":
            class2(center_x, b1)
        elif b3 = = "ThreeAdded":
            class3(center_x, b1)
        elif b3 = = "PauseAdded":
            class4(center_x, b1)
class class2(class1):
    def fonk2(self, center_x, b1):
        pygame.sprite.Sprite.fonk4(self)
        super().fonk4(center_x, b1, spec.ghostImages, spec.ghost, spec.cellWidth / 2)
class class3(class1):
    def fonk3(self, center_x, b1):
        pygame.sprite.Sprite.fonk4(self)
        super().fonk4(center_x, b1, spec.threeTimesImages, spec.threeTimes, spec.cellWidth / 2)
class class4(class1):
    def fonk4(self, center_x, b1):
        pygame.sprite.Sprite.fonk4(self)
        super().fonk4(center_x, b1, spec.pauseImages, spec.pause, spec.cellWidth / 2)