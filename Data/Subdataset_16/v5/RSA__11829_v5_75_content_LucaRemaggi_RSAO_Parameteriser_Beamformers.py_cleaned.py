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
            raise ValueError('To use this beamformer, the input must be B-format. The data shape should be Nx4, where N is the number of samples')
        W, X, Y, b7 = self.b2[:, 0], self.b2[:, 1], self.b2[:, 2], self.b2[:, 3]
        b8 = self.fonk3()
        b9 = self.fonk4()
        b10 = self.fonk5(len(W), len(b8), len(b9))
        self.fonk6(b10, b8, b9, W, X, Y, b7)
        b11 = np.squeeze(np.sum(b10**2, axis=0))
        max_az, b12 = np.unravel_index(np.argmax(b11), b11.shape)
        self.b4 = b8[max_az]
        self.b5 = b9[b12]
        self.b6 = b10[:, max_az, b12]
        return self
    def fonk3(self):
        if self.b3 in ['az', '3D']:
            return np.linspace(0, 2 * np.pi - (np.pi / 180), 360)
        return np.array([0, np.pi])
    def fonk4(self):
        if self.b3 in ['el', '3D']:
            return np.linspace(-np.pi / 2, np.pi / 2, 181)
        return np.array([0, np.pi / 2])
    def fonk5(self, num_samples, num_azimuths, num_elevations):
        return np.zeros((num_samples, num_azimuths, num_elevations))
    def fonk6(self, b10, b8, b9, W, X, Y, b7):
        for iAz, azimuth in enumerate(b8):
            for iEl, elevation in enumerate(b9):
                b13 = np.cos(elevation) * np.cos(azimuth)
                b14 = np.cos(elevation) * np.sin(azimuth)
                b15 = np.sin(elevation)
                b10[:, iAz, iEl] = 0.5 * ((2 - self.b1) * W + self.b1 * (b13 * X + b14 * Y + b15 * b7))