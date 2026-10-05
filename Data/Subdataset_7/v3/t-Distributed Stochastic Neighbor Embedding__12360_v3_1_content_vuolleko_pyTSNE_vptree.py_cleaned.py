import numpy as np
class class1:
    def fonk1(self, indices, b5):
        if len(indices) == 0:
            self.b1 = None
            self.b2 = None
            return
        self.b1 = indices[0]
        b3 = indices[1:]
        if b3:
            b4 = np.sum((b5[1:, :] - b5[0, :]) ** 2., axis=1)
            b5 = b5[1:, :]
            self.b2 = np.median(b4)
            b6 = b4 < self.b2
            b7 = ~b6
            self.b8 = class1(b3[b6], b5[b6])
            self.b9 = class1(b3[b7], b5[b7])
        else:
            self.b2 = None
            self.b8 = class1([], [])
            self.b9 = class1([], [])
    def fonk2(self, b10 = 0):
        if self.b1 is None:
            return
        b11 = "    " * b10
        print(b11 + "* (Node {})".format(self.b1))
        if self.b8.b1 is not None:
            print(b11 + "  - Inside {}:".format(self.b1))
            self.b8.fonk2(b10 + 1)
        if self.b9.b1 is not None:
            print(b11 + "  - Outside {}:".format(self.b1))
            self.b9.fonk2(b10 + 1)
    def fonk3(self, point_index, neighbors, b4, b5):
        if self.b1 is None:
            return
        b12 = np.sum((b5[self.b1, :] - b5[point_index, :]) ** 2.)
        b13 = b4[-1]
        if point_index != self.b1 and b12 < b13:
            b4[-1] = b12
            neighbors[-1] = self.b1
            b14 = np.argsort(b4)
            b4[:] = b4[b14]
            neighbors[:] = neighbors[b14]
        if self.b2 is None:
            return
        if b12 >= b13 + self.b2:
            self.b9.fonk3(point_index, neighbors, b4, b5)
        elif self.b2 > b13 + b12:
            self.b8.fonk3(point_index, neighbors, b4, b5)
        else:
            self.b8.fonk3(point_index, neighbors, b4, b5)
            self.b9.fonk3(point_index, neighbors, b4, b5)
        return neighbors