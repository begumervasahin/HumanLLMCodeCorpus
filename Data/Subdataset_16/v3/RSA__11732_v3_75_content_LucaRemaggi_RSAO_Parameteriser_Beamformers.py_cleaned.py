import numpy as np
class class1:
    def fonk1(self, b2, b1 = 1, b3='3D'):
        self.b2 = b2
        self.b1 = b1
        self.b3 = b3
        self.b4 = None
        self.b5 = None
        self.b6 = None
    def fonk2(self):
        self.fonk3()
        W, X, Y, b7 = self.b2.T
        b8 = self.fonk4()
        b9 = self.fonk5()
        b10 = self.fonk6(W, X, Y, b7, b8, b9)
        b11 = np.squeeze(np.sum(b10 ** 2, axis=0))
        self.fonk9(b11, b8, b9)
        return self
    def fonk3(self):
        if self.b2.shape[1] != 4:
            raise ValueError('To use this b16, the input must be B-format. The data shape should be Nx4, where N is the number of samples.')
    def fonk4(self):
        if self.b3 in ['az', '3D']:
            return np.linspace(0, 2 * np.pi - (np.pi / 180), 360)
        return np.array([0, np.pi])
    def fonk5(self):
        if self.b3 in ['el', '3D']:
            return np.linspace(-np.pi / 2, np.pi / 2, 181)
        return np.array([0, np.pi / 2])
    def fonk6(self, W, X, Y, b7, b8, b9):
        b10 = np.zeros((len(W), len(b8), len(b9)))
        for iAz, az in enumerate(b8):
            for iEl, el in enumerate(b9):
                b13, b14, b12 = self.fonk7(az, el)
                b10[:, iAz, iEl] = self.fonk8(W, X, Y, b7, b13, b14, b12)
        return b10
    def fonk7(self, az, el):
        b13 = np.cos(el) * np.cos(az)
        b14 = np.cos(el) * np.sin(az)
        b12 = np.sin(el)
        return b13, b14, b12
    def fonk8(self, W, X, Y, b7, b13, b14, b12):
        return 0.5 * ((2 - self.b1) * W + self.b1 * (b13 * X + b14 * Y + b12 * b7))
    def fonk9(self, b11, b8, b9):
        max_az_idx, b15 = np.unravel_index(np.argmax(b11), b11.shape)
        self.b4 = b8[max_az_idx]
        self.b5 = b9[b15]
        self.b6 = self.b2[:, max_az_idx, b15]
b2 = np.random.randn(1000, 4)
b16 = class1(b2, b1=1, b3='3D')
b16.fonk2()
print(f"Azimuth: {b16.b4}")
print(f"Elevation: {b16.b5}")
print(f"HBeam: {b16.b6}")