import numpy as np
def calculate_sharpness(data):
    sharpness_total = 0.0
    for sample in data:
        gradient_x, gradient_y = np.gradient(sample[:, :, 0])
        gradient_norm = np.sqrt(gradient_x ** 2 + gradient_y ** 2)
        sharpness_total += np.mean(gradient_norm)
    return sharpness_total / data.shape[0]
def prototype_sharpness_ratio(input_samples, som_prototypes):
    size = int(np.sqrt(input_samples.shape[-1]))
    input_samples = input_samples.reshape(-1, size, size, 1)
    som_prototypes = som_prototypes.reshape(-1, size, size, 1)
    data_sharpness = calculate_sharpness(input_samples)
    som_sharpness = calculate_sharpness(som_prototypes)
    return som_sharpness / data_sharpness
if __name__ == "__main__":
    input_samples = np.random.rand(100, 64)
    som_prototypes = np.random.rand(10, 64)
    sharpness_ratio = prototype_sharpness_ratio(input_samples, som_prototypes)
    print("Sharpness Ratio:", sharpness_ratio)