import numpy as np
def prototype_sharpness_ratio(input_samples, som_prototypes):
    input_size = int(np.sqrt(input_samples.shape[-1]))
    input_samples_reshaped = input_samples.reshape(-1, input_size, input_size, 1)
    som_size = int(np.sqrt(som_prototypes.shape[-1]))
    som_prototypes_reshaped = som_prototypes.reshape(-1, som_size, som_size, 1)
    data_sharpness = calculate_sharpness(input_samples_reshaped)
    som_sharpness = calculate_sharpness(som_prototypes_reshaped)
    return som_sharpness / data_sharpness
def calculate_sharpness(data):
    total_sharpness = 0.0
    for sample in data:
        gx, gy = np.gradient(sample[:, :, 0])
        gradient_norm = np.sqrt(gx ** 2 + gy ** 2)
        total_sharpness += np.mean(gradient_norm)
    return total_sharpness / data.shape[0]
if __name__ == "__main__":
    input_samples = np.random.rand(100, 64)
    som_prototypes = np.random.rand(10, 64)
    sharpness_ratio = prototype_sharpness_ratio(input_samples, som_prototypes)
    print("Sharpness Ratio:", sharpness_ratio)