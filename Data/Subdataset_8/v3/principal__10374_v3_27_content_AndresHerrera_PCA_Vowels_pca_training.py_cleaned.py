import os
import cv2
import numpy as np
def unflatten_vector_to_image(vector, rows, cols):
    img = []
    cutter = 0
    while cutter + cols <= rows * cols:
        try:
            img.append(vector[cutter:cutter + cols])
        except:
            img = vector[cutter:cutter + cols]
        cutter += cols
    img = np.array(img)
    return img
IMAGE_WIDTH = 20
IMAGE_HEIGHT = 20
vowels = ['A', 'E', 'I', 'O', 'U']
def main():
    for vowel in vowels:
        images_matrix = None
        image_count = 0
        print('Processing vowel:', vowel)
        for file_name in os.listdir(os.path.join('training/', vowel)):
            image_count += 1
            print('Reading image:', file_name)
            image = cv2.imread(os.path.join('training/', vowel, file_name), cv2.IMREAD_GRAYSCALE)
            resized_image = cv2.resize(image, (IMAGE_WIDTH, IMAGE_HEIGHT))
            flattened_vector = resized_image.reshape(IMAGE_WIDTH * IMAGE_HEIGHT)
            try:
                images_matrix = np.vstack((images_matrix, flattened_vector))
            except:
                images_matrix = flattened_vector
        if images_matrix is not None:
            mean, eigenvectors = cv2.PCACompute(images_matrix, np.mean(images_matrix, axis=0).reshape(1, -1))
        mean_image = unflatten_vector_to_image(mean.transpose(), IMAGE_WIDTH, IMAGE_HEIGHT)
        cv2.imwrite('trained/pca_vowels_' + vowel + '.png', mean_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if __name__ == "__main__":
    main()