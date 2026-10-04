import numpy as np
class EstimatePerceptualMixingTime:
    def __init__(self, room_dims):
        self.room_dims = room_dims
        self.mixing_time_estimate = {}
    def validate_dimensions(self, dimensions):
        if not all(isinstance(dim, (int, float)) and dim > 0 for dim in dimensions):
            raise ValueError('Room dimensions must contain positive numeric values only.')
    def calculate_volume(self, x, y, z):
        return x * y * z
    def calculate_surface_area(self, x, y, z):
        return 2 * (x * y + x * z + y * z)
    def model_based(self):
        print('----------------------------------')
        print('MODEL-BASED MIXING TIME PREDICTION')
        print('----------------------------------')
        print('ROOM PROPERTIES:')
        x_d, y_d, z_d = self.room_dims
        self.validate_dimensions([x_d, y_d, z_d])
        print(f'Room dimensions: height = {x_d}m, length = {y_d}m, width = {z_d}m')
        print('Perceptual mixing times tmp50 and tmp95 (in ms) from model-based predictors:')
        volume = self.calculate_volume(x_d, y_d, z_d)
        surface_area = self.calculate_surface_area(x_d, y_d, z_d)
        print(f'Volume: {volume} mÂ³')
        print(f'Surface area: {surface_area} mÂ²')
        root_volume = np.sqrt(volume)
        mean_free_path = 47 * volume / surface_area
        tmp50 = 20.08 * volume / surface_area + 12
        tmp95 = 0.0117 * volume + 50.1
        print(f'tmp50: {tmp50} ms')
        print(f'tmp95: {tmp95} ms')
        self.mixing_time_estimate = {
            'model': {
                'tmp50': tmp50,
                'tmp95': tmp95,
                'root_volume': root_volume,
                'mean_free_path': mean_free_path
            }
        }
        return self
dims = [5.0, 6.0, 4.0]
estimator = EstimatePerceptualMixingTime(dims)
estimator.model_based()