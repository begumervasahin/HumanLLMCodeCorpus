import numpy as np
class Beamformers:
    def __init__(self, signal, d=1, dimension='3D'):
        self.signal = signal
        self.d = d
        self.dimension = dimension
        self.az_rad_curr = None
        self.el_rad_curr = None
        self.hBeam = None
    def steerBFormat(self):
        if self.signal.shape[1] != 4:
            raise ValueError('To use this beamformer, the input must be B-format. The data shape should be Nx4, where N is the number of samples')
        W, X, Y, Z = self.signal[:, 0], self.signal[:, 1], self.signal[:, 2], self.signal[:, 3]
        if self.dimension in ['az', '3D']:
            azimuths = np.linspace(0, 2 * np.pi - (np.pi / 180), 360)
        else:
            azimuths = np.array([0, np.pi])
        if self.dimension in ['el', '3D']:
            elevations = np.linspace(-np.pi / 2, np.pi / 2, 181)
        else:
            elevations = np.array([0, np.pi / 2])
        steeredresp = np.zeros((len(W), len(azimuths), len(elevations)))
        for iAz, azimuth in enumerate(azimuths):
            for iEl, elevation in enumerate(elevations):
                r_x = np.cos(elevation) * np.cos(azimuth)
                r_y = np.cos(elevation) * np.sin(azimuth)
                r_z = np.sin(elevation)
                steeredresp[:, iAz, iEl] = 0.5 * ((2 - self.d) * W + self.d * (r_x * X + r_y * Y + r_z * Z))
        angular_response = np.squeeze(np.sum(steeredresp**2, axis=0))
        max_az, max_el = np.unravel_index(np.argmax(angular_response), angular_response.shape)
        self.az_rad_curr = azimuths[max_az]
        self.el_rad_curr = elevations[max_el]
        self.hBeam = steeredresp[:, max_az, max_el]
        return self