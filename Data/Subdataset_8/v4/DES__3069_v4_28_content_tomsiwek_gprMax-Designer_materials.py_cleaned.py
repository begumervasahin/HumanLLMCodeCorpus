class Material:
    def __init__(self, epsilon_r=0.0, sigma=0.0, mu_r=0.0, sigma_mag=0.0, name=""):
        self.epsilon_r = epsilon_r
        self.sigma = sigma
        self.mu_r = mu_r
        self.sigma_mag = sigma_mag
        self.name = name
    def calculate_wave_velocity(self):
        speed_of_light = 299792458
        return speed_of_light / (self.epsilon_r ** 0.5)