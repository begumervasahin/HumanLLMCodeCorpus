import cv2
import numpy as np
import pickle
import os
import matplotlib.pyplot as plt
from scipy.misc import imread
def extract_features(image_path, vector_size=32):
    image = imread(image_path, mode="RGB")
    try:
        kaze = cv2.KAZE_create()
        keypoints = kaze.detect(image)
        keypoints = sorted(keypoints, key=lambda x: -x.response)[:vector_size]
        keypoints, descriptors = kaze.compute(image, keypoints)
        descriptors = descriptors.flatten()
        needed_size = vector_size * 64
        if descriptors.size < needed_size:
            descriptors = np.concatenate([descriptors, np.zeros(needed_size - descriptors.size)])
    except cv2.error as e:
        print(f'Error: {e}')
        return None
    return descriptors
def batch_extractor(images_path, pickled_db_path="features.pck"):
    image_files = [os.path.join(images_path, p) for p in sorted(os.listdir(images_path))]
    features = {}
    for image_file in image_files:
        print(f'Extracting features from image {image_file}')
        image_name = os.path.basename(image_file).lower()
        features[image_name] = extract_features(image_file)
    with open(pickled_db_path, 'wb') as fp:
        pickle.dump(features, fp, protocol=pickle.HIGHEST_PROTOCOL)
if __name__ == '__main__':
    images_path = 'path/to/images'
    pickled_db_path = 'features.pck'
    batch_extractor(images_path, pickled_db_path)