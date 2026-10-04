import numpy as np
class EstimatePerceptualMixingTime:
    def __init__(self, RoomDims):
        self.RoomDims = RoomDims
        self.mixing_time_estimate = {}
    def model_based(self):
        print('----------------------------------')
        print('MODEL-BASED MIXING TIME PREDICTION')
        print('----------------------------------')
        print('ROOM PROPERTIES:')
        x_d, y_d, z_d = self.RoomDims
        if x_d <= 0 or y_d <= 0 or z_d <= 0:
            raise ValueError('RoomDims must contain positive, numeric values only.')
        print(f'Room dimensions: height = {x_d}m, length = {y_d}m, width = {z_d}m')
        volume = x_d * y_d * z_d
        surface_area = 2 * (x_d * y_d + x_d * z_d + y_d * z_d)
        print(f'Volume: {volume} mÂ³')
        print(f'Surface area: {surface_area} mÂ²')
        rootvol = np.sqrt(volume)
        MFP = 47 * volume / surface_area
        tmp50 = 20.08 * volume / surface_area + 12
        tmp95 = 0.0117 * volume + 50.1
        print(f'tmp50: {tmp50} ms')
        print(f'tmp95: {tmp95} ms')
        self.mixing_time_estimate['model'] = {
            'tmp50': tmp50,
            'tmp95': tmp95,
            'rootV': rootvol,
            'mfp_based': MFP
        }
        return self