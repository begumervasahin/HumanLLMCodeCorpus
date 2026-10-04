
import numpy as np
def prototype_sharpness_ratio(X, som):
    image_size = int(np.sqrt(X.shape[-1]))
    X_reshaped = X.reshape(-1, image_size, image_size, 1)
    som_reshaped = som.reshape(-1, image_size, image_size, 1)
    data_sharpness = calculate_average_sharpness(X_reshaped)
    som_sharpness = calculate_average_sharpness(som_reshaped)
    return som_sharpness / data_sharpness
def calculate_average_sharpness(images):
    total_sharpness = 0.0
    for img in images:
        gx, gy = np.gradient(img[:, :, 0])
        gradient_norm = np.sqrt(gx**2 + gy**2)
        total_sharpness += np.mean(gradient_norm)
    return total_sharpness / images.shape[0]
if __name__ == "__main__":
    n_samples = 10
    input_dim = 64
    n_prototypes = 5
    X = np.random.rand(n_samples, input_dim)
    som = np.random.rand(n_prototypes, input_dim)
    ratio = prototype_sharpness_ratio(X, som)
    print("Prototype Sharpness Ratio:", ratio)