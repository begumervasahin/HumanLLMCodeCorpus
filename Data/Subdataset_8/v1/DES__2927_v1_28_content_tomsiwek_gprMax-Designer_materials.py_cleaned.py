class TMaterial:
    def __init__(self, epsilon_r=0.0, sigma=0.0, mu_r=0.0, sigma_mag=0.0, name=""):
        self.epsilon_r = epsilon_r
        self.sigma = sigma
        self.mu_r = mu_r
        self.sigma_mag = sigma_mag
        self.name = name
    def velocity(self):
        c = 299792458
        return c / (self.epsilon_r ** 0.5)
material1 = TMaterial(epsilon_r=4.0, sigma=0.01, mu_r=1.0, sigma_mag=0.005, name="Material1")
material2 = TMaterial(epsilon_r=3.5, sigma=0.02, mu_r=1.2, sigma_mag=0.007, name="Material2")
print("Material 1 Velocity:", material1.velocity())
print("Material 2 Velocity:", material2.velocity())