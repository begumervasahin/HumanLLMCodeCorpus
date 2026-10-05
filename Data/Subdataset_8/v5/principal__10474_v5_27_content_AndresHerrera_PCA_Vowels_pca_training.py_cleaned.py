import os
import cv2
import numpy as np
def unflatten_vector(vector, rows, cols):
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
VOWELS = ['A', 'E', 'I', 'O', 'U']
def main():
    for vowel in VOWELS:
        print(f'Reading from: {vowel} Directory')
        in_matrix = None
        image_count = 0
        for file_name in os.listdir(os.path.join('training/', vowel)):
            image_count += 1
            print(file_name)
            img = cv2.imread(os.path.join('training/', vowel, file_name), cv2.IMREAD_GRAYSCALE)
            img_resized = cv2.resize(img, (IMAGE_WIDTH, IMAGE_HEIGHT))
            image_vector = img_resized.reshape(IMAGE_WIDTH * IMAGE_HEIGHT)
            try:
                in_matrix = np.vstack((in_matrix, image_vector))
            except:
                in_matrix = image_vector
        if in_matrix is not None:
            mean, eigenvectors = cv2.PCACompute(in_matrix, np.mean(in_matrix, axis=0).reshape(1, -1))
            avg_image = unflatten_vector(mean.transpose(), IMAGE_WIDTH, IMAGE_HEIGHT)
            cv2.imwrite(f'trained/pca_vowels_{vowel}.png', avg_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if __name__ == "__main__":
    main()