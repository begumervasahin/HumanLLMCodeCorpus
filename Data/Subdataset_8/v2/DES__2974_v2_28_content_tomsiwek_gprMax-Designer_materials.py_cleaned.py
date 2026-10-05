class Material:
    def __init__(self, epsilon_r=0.0, sigma=0.0, mu_r=0.0, sigma_mag=0.0, name=""):
        self.relative_permittivity = epsilon_r
        self.conductivity = sigma
        self.relative_permeability = mu_r
        self.magnetic_loss = sigma_mag
        self.identifier = name
    def calculate_wave_velocity(self):
        speed_of_light = 299792458
        return speed_of_light / (self.relative_permittivity ** 0.5)
material1 = Material(epsilon_r=4.0, sigma=0.01, mu_r=1.0, sigma_mag=0.005, name="Material1")
material2 = Material(epsilon_r=3.5, sigma=0.02, mu_r=1.2, sigma_mag=0.007, name="Material2")
print("Material 1 Wave Velocity:", material1.calculate_wave_velocity())
print("Material 2 Wave Velocity:", material2.calculate_wave_velocity())