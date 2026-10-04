import numpy as np
class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = {}
    def fonk2(self):
        print('----------------------------------')
        print('MODEL-BASED MIXING TIME PREDICTION')
        print('----------------------------------')
        print('ROOM PROPERTIES:')
        x_d, y_d, b3 = self.b1
        self.fonk3(x_d, y_d, b3)
        print(f'Room dimensions: b4 = {x_d}m, length = {y_d}m, width = {b3}m')
        b7, b5 = self.fonk4(x_d, y_d, b3)
        print(f'Volume: {b7} mÂ³')
        print(f'Surface area: {b5} mÂ²')
        b9, b10, b8, b6 = self.fonk5(b7, b5)
        print(f'b9: {b9} ms')
        print(f'b10: {b10} ms')
        self.fonk6(b9, b10, b8, b6)
        return self
    def fonk3(self, x_d, y_d, b3):
        if x_d <= 0 or y_d <= 0 or b3 <= 0:
            raise ValueError('b1 must contain positive, numeric values only.')
    def fonk4(self, x_d, y_d, b3):
        b7 = x_d * y_d * b3
        b5 = 2 * (x_d * y_d + x_d * b3 + y_d * b3)
        return b7, b5
    def fonk5(self, b7, b5):
        b8 = np.sqrt(b7)
        b6 = 47 * b7 / b5
        b9 = 20.08 * b7 / b5 + 12
        b10 = 0.0117 * b7 + 50.1
        return b9, b10, b8, b6
    def fonk6(self, b9, b10, b8, b6):
        self.b2['model'] = {
            'b9': b9,
            'b10': b10,
            'rootV': b8,
            'mfp_based': b6
        }