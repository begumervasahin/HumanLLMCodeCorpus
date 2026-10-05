import cv2
import numpy as np
from sklearn.decomposition import PCA
def rescale_image(img):
    height, width, _ = img.shape
    target_width = 900
    scaling_factor = target_width / width
    new_width, new_height = int(width * scaling_factor), int(height * scaling_factor)
    return new_width, new_height
def main():
    for num in range(1, 3):
        print(f"Processing image {num}")
        image = cv2.imread(str(num) + '.jpg')
        image_copy = image.copy()
        height, width, channels = image.shape
        flattened_img = np.reshape(image, (height, width * channels))
        pca = PCA(n_components=350)
        pca_fit = pca.fit(flattened_img)
        transformed_img = pca_fit.transform(flattened_img)
        reconstructed_img = pca_fit.inverse_transform(transformed_img)
        reconstructed_img = np.reshape(reconstructed_img, (height, width, channels))
        compressed_img = np.uint8(reconstructed_img)
        cv2.imwrite(f'quantizedImages/op-{num}.jpg', compressed_img)
        resized_original = cv2.resize(image_copy, rescale_image(image))
        cv2.imshow("Original", resized_original)
        resized_compressed = cv2.resize(compressed_img, rescale_image(image))
        cv2.imshow("Compressed", resized_compressed)
        cv2.waitKey()
if __name__ == "__main__":
    main()