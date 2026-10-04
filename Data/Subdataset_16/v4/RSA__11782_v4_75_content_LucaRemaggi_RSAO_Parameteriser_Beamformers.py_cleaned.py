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
        if self.b3 in ['az', '3D']:
            b8 = np.linspace(0, 2 * np.pi - (np.pi / 180), 360)
        else:
            b8 = np.array([0, np.pi])
        if self.b3 in ['el', '3D']:
            b9 = np.linspace(-np.pi / 2, np.pi / 2, 181)
        else:
            b9 = np.array([0, np.pi / 2])
        b10 = np.zeros((len(W), len(b8), len(b9)))
        for iAz, azimuth in enumerate(b8):
            for iEl, elevation in enumerate(b9):
                b11 = np.cos(elevation) * np.cos(azimuth)
                b12 = np.cos(elevation) * np.sin(azimuth)
                b13 = np.sin(elevation)
                b10[:, iAz, iEl] = 0.5 * ((2 - self.b1) * W + self.b1 * (b11 * X + b12 * Y + b13 * b7))
        b14 = np.squeeze(np.sum(b10**2, axis=0))
        max_az, b15 = np.unravel_index(np.argmax(b14), b14.shape)
        self.b4 = b8[max_az]
        self.b5 = b9[b15]
        self.b6 = b10[:, max_az, b15]
        return self