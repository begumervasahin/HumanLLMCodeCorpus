import numpy as np
def prototype_sharpness_ratio(input_samples, som_prototypes):
    input_samples_reshaped = reshape_data(input_samples)
    som_prototypes_reshaped = reshape_data(som_prototypes)
    data_sharpness = calculate_sharpness(input_samples_reshaped)
    som_sharpness = calculate_sharpness(som_prototypes_reshaped)
    return som_sharpness / data_sharpness
def reshape_data(data):
    size = int(np.sqrt(data.shape[-1]))
    return data.reshape(-1, size, size, 1)
def calculate_sharpness(data):
    total_sharpness = 0.0
    for sample in data:
        gx, gy = np.gradient(sample[:, :, 0])
        gradient_norm = np.sqrt(gx ** 2 + gy ** 2)
        total_sharpness += np.mean(gradient_norm)
    return total_sharpness / len(data)
if __name__ == "__main__":
    input_samples = np.random.rand(100, 64)
    som_prototypes = np.random.rand(10, 64)
    sharpness_ratio = prototype_sharpness_ratio(input_samples, som_prototypes)
    print("Sharpness Ratio:", sharpness_ratio)