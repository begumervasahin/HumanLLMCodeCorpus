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
def main():
    sample_material = TMaterial(epsilon_r=4.0, sigma=0.01, mu_r=1.0, sigma_mag=0.0, name="SampleMaterial")
    wave_velocity = sample_material.velocity()
    print(f"The velocity of the electromagnetic wave in {sample_material.name} is {wave_velocity:.2f} m/s")
if __name__ == "__main__":
    main()