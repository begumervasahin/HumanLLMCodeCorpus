import pygame
import spec
import powerup
class Single(powerup.PowerupGeneric):
    @staticmethod
    def generate_new_powerup(data, type_added):
        center_x, center_y = powerup.PowerupGeneric.generate_new_powerup_location()
        msg = "%s %d %d\n" % (type_added, center_x, center_y)
        if data.server is not None:
            data.server.send(msg.encode())
        if type_added == "GhostAdded":
            Ghost(center_x, center_y)
        elif type_added == "ThreeAdded":
            Three(center_x, center_y)
        elif type_added == "PauseAdded":
            Pause(center_x, center_y)
class Ghost(Single):
    def __init__(self, center_x, center_y):
        super().__init__(center_x, center_y, spec.ghostImages, spec.ghost, spec.cellWidth / 2)
class Three(Single):
    def __init__(self, center_x, center_y):
        super().__init__(center_x, center_y, spec.threeTimesImages, spec.threeTimes, spec.cellWidth / 2)
class Pause(Single):
    def __init__(self, center_x, center_y):
        super().__init__(center_x, center_y, spec.pauseImages, spec.pause, spec.cellWidth / 2)
