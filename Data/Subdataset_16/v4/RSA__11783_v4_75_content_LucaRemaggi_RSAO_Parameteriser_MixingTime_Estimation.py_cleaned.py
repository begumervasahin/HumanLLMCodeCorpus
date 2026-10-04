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
        if x_d <= 0 or y_d <= 0 or b3 <= 0:
            raise ValueError('b1 must contain positive, numeric values only.')
        print(f'Room dimensions: b4 = {x_d}m, length = {y_d}m, width = {b3}m')
        b5 = x_d * y_d * b3
        b6 = 2 * (x_d * y_d + x_d * b3 + y_d * b3)
        print(f'Volume: {b5} mÂ³')
        print(f'Surface area: {b6} mÂ²')
        b7 = np.sqrt(b5)
        b8 = 47 * b5 / b6
        b9 = 20.08 * b5 / b6 + 12
        b10 = 0.0117 * b5 + 50.1
        print(f'b9: {b9} ms')
        print(f'b10: {b10} ms')
        self.b2['model'] = {
            'b9': b9,
            'b10': b10,
            'rootV': b7,
            'mfp_based': b8
        }
        return self