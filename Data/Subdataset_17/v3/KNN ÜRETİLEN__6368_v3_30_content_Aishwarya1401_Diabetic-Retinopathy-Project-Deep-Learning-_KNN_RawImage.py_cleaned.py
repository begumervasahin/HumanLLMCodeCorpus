import os
import numpy as np
import pandas as pd
from PIL import Image
from sklearn.decomposition import PCA
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
IMAGE_PATH = "gray2"
LABELS_FILE = 'trainLabels.csv'
df_label = pd.read_csv(LABELS_FILE)
def get_label(image_name):
    image_id = image_name.split(os.path.sep)[-1].split(".")[0]
    label = df_label.loc[df_label['id'] == image_id, 'label'].values[0]
    return int(label)
def load_images_and_labels(image_path):
    files = os.listdir(image_path)
    image_vectors = []
    labels = []
    for file in files:
        image = Image.open(os.path.join(image_path, file))
        image_vector = np.array(image).flatten()
        image_vectors.append(image_vector)
        label = get_label(file)
        labels.append(label)
    return np.array(image_vectors, dtype='float32'), np.array(labels)
def evaluate_knn_classifier(train_vectors, train_labels, test_vectors, test_labels, k_values):
    for k in k_values:
        print(f"Evaluating raw pixel accuracy with k = {k}")
        model = KNeighborsClassifier(n_neighbors=k)
        model.fit(train_vectors, train_labels)
        accuracy = model.score(test_vectors, test_labels)
        print(f"Raw pixel accuracy: {accuracy * 100:.2f}%")
def main():
    img_vectors, labels = load_images_and_labels(IMAGE_PATH)
    train_vectors, test_vectors, train_labels, test_labels = train_test_split(img_vectors, labels, test_size=0.25, random_state=42)
    k_values = [1, 3, 5, 10, 20, 50, 100]
    evaluate_knn_classifier(train_vectors, train_labels, test_vectors, test_labels, k_values)
if __name__ == "__main__":
    main()