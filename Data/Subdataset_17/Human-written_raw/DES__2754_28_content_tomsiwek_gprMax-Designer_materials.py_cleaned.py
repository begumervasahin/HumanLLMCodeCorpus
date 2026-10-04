class TMaterial(object):
    def __init__(self, epsilon_r = 0.0, sigma = 0.0, mu_r = 0.0, sigma_mag = 0.0, name = ""):
        self.epsilon_r = epsilon_r
        self.sigma = sigma
        self.mu_r = mu_r
        self.sigma_mag = sigma_mag
        self.name = name
    def velocity(self):
        c = 299792458
        return c/(self.epsilon_r**(0.5))