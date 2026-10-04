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
            raise ValueError('To use this beamformer the input must be B-format. The data shape should be Nx4, where N is the number of samples')
        b7 = self.b2[:, 0]
        b8 = self.b2[:, 1]
        b9 = self.b2[:, 2]
        b10 = self.b2[:, 3]
        if self.b3 = = 'az' or self.b3 == '3D':
            b11 = np.linspace(0, np.pi*2-(np.pi/180), 360)
        else:
            b11 = np.array([0, np.pi])
        if self.b3 = = 'el' or self.b3 == '3D':
            b12 = np.linspace(-np.pi/2, np.pi/2, 181)
        else:
            b12 = np.array([0, np.pi/2])
        b13 = np.zeros([len(b7), len(b11), len(b12)])
        for iAz in range(len(b11)):
            for iEl in range(len(b12)):
                b14 = np.cos(b12[iEl]) * np.cos(b11[iAz])
                b15 = np.cos(b12[iEl]) * np.sin(b11[iAz])
                b16 = np.sin(b12[iEl])
                b13[:, iAz, iEl] = 0.5 * ((2-self.b1)*b7 + self.b1*(b14*b8 + b15*b9 + b16*b10))
        b17 = np.squeeze(np.sum(b13**2, 0))
        max_az, b18 = np.where(b17 == np.max(b17))
        self.b4 = b11[max_az[0]]
        self.b5 = b12[b18[0]]
        self.b6 = b13[:, max_az[0], b18[0]]
        return self