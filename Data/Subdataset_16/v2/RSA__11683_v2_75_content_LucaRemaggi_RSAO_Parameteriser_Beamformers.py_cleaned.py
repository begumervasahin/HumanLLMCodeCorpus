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
        if self.b2.shape[1] != 4:
            raise ValueError('To use this b19, the input must be B-format. The data shape should be Nx4, where N is the number of samples.')
        b7 = self.b2[:, 0]
        b8 = self.b2[:, 1]
        b9 = self.b2[:, 2]
        b10 = self.b2[:, 3]
        if self.b3 in ['az', '3D']:
            b11 = np.linspace(0, 2 * np.pi - (np.pi / 180), 360)
        else:
            b11 = np.array([0, np.pi])
        if self.b3 in ['el', '3D']:
            b12 = np.linspace(-np.pi / 2, np.pi / 2, 181)
        else:
            b12 = np.array([0, np.pi / 2])
        b13 = np.zeros((len(b7), len(b11), len(b12)))
        for iAz, az in enumerate(b11):
            for iEl, el in enumerate(b12):
                b14 = np.cos(el) * np.cos(az)
                b15 = np.cos(el) * np.sin(az)
                b16 = np.sin(el)
                b13[:, iAz, iEl] = 0.5 * ((2 - self.b1) * b7 + self.b1 * (b14 * b8 + b15 * b9 + b16 * b10))
        b17 = np.squeeze(np.sum(b13 ** 2, axis=0))
        max_az_idx, b18 = np.unravel_index(np.argmax(b17), b17.shape)
        self.b4 = b11[max_az_idx]
        self.b5 = b12[b18]
        self.b6 = b13[:, max_az_idx, b18]
        return self
b2 = np.random.randn(1000, 4)
b19 = class1(b2, b1=1, b3='3D')
b19.fonk2()
print(f"Azimuth: {b19.b4}")
print(f"Elevation: {b19.b5}")
print(f"HBeam: {b19.b6}")