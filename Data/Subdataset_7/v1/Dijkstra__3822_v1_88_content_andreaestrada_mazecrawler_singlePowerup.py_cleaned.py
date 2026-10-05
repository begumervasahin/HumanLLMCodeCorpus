import pygame
import spec
import powerup
class class1(powerup.PowerupGeneric):
    @staticmethod
    def fonk1(data, b3):
        centerX, b1 = powerup.PowerupGeneric.generateNewPowerupLocation()
        b2 = "%s %d %d\n" % (b3, centerX, b1)
        if data.server is not None:
            data.server.send(b2.encode())
        if b3 = = "GhostAdded":
            class2(centerX, b1)
        elif b3 = = "ThreeAdded":
            class3(centerX, b1)
        elif b3 = = "PauseAdded":
            class4(centerX, b1)
class class2(class1):
    def fonk2(self, centerX, b1):
        super().fonk4(centerX, b1, spec.ghostImages, spec.ghost, spec.cellWidth/2)
class class3(class1):
    def fonk3(self, centerX, b1):
        super().fonk4(centerX, b1, spec.threeTimesImages, spec.threeTimes, spec.cellWidth/2)
class class4(class1):
    def fonk4(self, centerX, b1):
        super().fonk4(centerX, b1, spec.pauseImages, spec.pause, spec.cellWidth/2)
