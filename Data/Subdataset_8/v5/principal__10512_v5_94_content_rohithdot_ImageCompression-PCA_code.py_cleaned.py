import numpy as np
import cv2
from sklearn.decomposition import PCA
def rescale_image(img):
    height, width, _ = img.shape
    target_width = 900
    scaling_factor = target_width / width
    new_width = int(width * scaling_factor)
    new_height = int(height * scaling_factor)
    return new_width, new_height
def process_image(image_path):
    image = cv2.imread(image_path)
    original_image = image.copy()
    height, width, depth = image.shape
    flattened_img = np.reshape(image, (height, width * depth))
    pca_model = PCA(n_components=350).fit(flattened_img)
    transformed_img = pca_model.transform(flattened_img)
    explained_variance = np.sum(pca_model.explained_variance_ratio_)
    reconstructed_img = pca_model.inverse_transform(transformed_img)
    reconstructed_img = np.reshape(reconstructed_img, (height, width, depth))
    compressed_image = np.uint8(reconstructed_img)
    return original_image, compressed_image
def main():
    for num in range(1, 3):
        print("Processing image", num)
        original_image, compressed_image = process_image(str(num) + '.jpg')
        cv2.imwrite('quantizedImages/op-' + str(num) + '.jpg', compressed_image)
        resized_original = cv2.resize(original_image, rescale_image(original_image))
        resized_compressed = cv2.resize(compressed_image, rescale_image(original_image))
        cv2.imshow("Original", resized_original)
        cv2.imshow("Compressed", resized_compressed)
        cv2.waitKey()
if __name__ == "__main__":
    main()