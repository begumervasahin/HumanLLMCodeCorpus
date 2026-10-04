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
        b3 = self.b1[0]
        b4 = self.b1[1]
        b5 = self.b1[2]
        try:
            b3 > 0
        except ValueError:
            print('b1 must contain positive, numeric values only.')
        try:
            b4 > 0
        except ValueError:
            print('b1 must contain positive, numeric values only.')
        try:
            b5 > 0
        except ValueError:
            print('b1 must contain positive, numeric values only.')
        print('Room dimensions: b6 = ' + str(b3) + 'm, length = ' + str(b4) + 'm, width = ' + str(b5) + 'm')
        print('Perceptual mixing times b11 and b12 (in ms) from model-based predictors:')
        b7 = b3 * b4 * b5
        b8 = 2*b3*b4 + 2*b3*b5 + 2*b4*b5
        print('Volume: ' + str(b7) + 'm3')
        print('Surface area: ' + str(b8) + 'm2')
        b9 = np.sqrt(b7)
        b10 = 47*b7/b8
        b11 = 20.08 * b7/b8 + 12
        print('b11: ' + str(b11) + 'ms')
        b12 = 0.0117 * b7 + 50.1
        print('b12: ' + str(b12) + 'ms')
        self.b2.update({'model': {'b11': b11}})
        self.b2['model'].update({'b12': b12})
        self.b2['model'].update({'rootV': b9})
        self.b2['model'].update({'mfp_based': b10})
        return self