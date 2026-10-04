import numpy as np
class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = {}
    def fonk2(self, dimensions):
        if not all(isinstance(dim, (int, float)) and dim > 0 for dim in dimensions):
            raise ValueError('Room dimensions must contain positive numeric values only.')
    def fonk3(self, x, y, z):
        return x * y * z
    def fonk4(self, x, y, z):
        return 2 * (x * y + x * z + y * z)
    def fonk5(self):
        print('----------------------------------')
        print('MODEL-BASED MIXING TIME PREDICTION')
        print('----------------------------------')
        print('ROOM PROPERTIES:')
        x_d, y_d, b3 = self.b1
        self.fonk2([x_d, y_d, b3])
        print(f'Room dimensions: b4 = {x_d}m, length = {y_d}m, width = {b3}m')
        print('Perceptual mixing times b9 and b10 (in ms) from model-based predictors:')
        b5 = self.fonk3(x_d, y_d, b3)
        b6 = self.fonk4(x_d, y_d, b3)
        print(f'Volume: {b5} mÂ³')
        print(f'Surface area: {b6} mÂ²')
        b7 = np.sqrt(b5)
        b8 = 47 * b5 / b6
        b9 = 20.08 * b5 / b6 + 12
        b10 = 0.0117 * b5 + 50.1
        print(f'b9: {b9} ms')
        print(f'b10: {b10} ms')
        self.b2 = {
            'model': {
                'b9': b9,
                'b10': b10,
                'b7': b7,
                'b8': b8
            }
        }
        return self
b11 = [5.0, 6.0, 4.0]
b12 = class1(b11)
b12.fonk5()