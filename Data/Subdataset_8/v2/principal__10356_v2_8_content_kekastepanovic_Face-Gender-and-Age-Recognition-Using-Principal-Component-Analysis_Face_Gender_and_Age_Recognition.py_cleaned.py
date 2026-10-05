import numpy as np
import cv2
import os
import random
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix
folder_path = r"C:\Users\Computer\Desktop\KV"
folder_faces = os.path.join(folder_path, "Viola and Jones")
folder_similar_images = os.path.join(folder_path, "treniranje i testiranje")
folder_individual_faces = os.path.join(folder_path, "jedinicna lica")
folder_images_part1 = os.path.join(folder_path, "part1")
face_cascade_xml = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
def detect_faces(image_path, cascade_path):
    original_image = cv2.imread(image_path)
    grayscale_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cascade_path)
    detected_faces = face_cascade.detectMultiScale(grayscale_image)
    return grayscale_image, detected_faces
def preprocess_faces(image, detected_faces):
    preprocessed_faces = []
    for (x, y, w, h) in detected_faces:
        sub_face = cv2.resize(image[y:y+h, x:x+w], (360, 480))
        preprocessed_faces.append(sub_face)
    return preprocessed_faces
def extract_info_from_filename(filename):
    age, gender = filename.split("_")[:2]
    return int(age), gender
def plot_eigenvalues(singular_values):
    plt.plot(np.arange(1, len(singular_values) + 1), singular_values, marker='o', linewidth=2, markersize=12)
    plt.xlabel('Component')
    plt.ylabel('Eigenvalue')
    plt.title('Eigenvalues of PCA')
    plt.show()
face_images = []
genders = []
for _ in range(111):
    file_name = random.choice(os.listdir(folder_images_part1))
    file_path = os.path.join(folder_images_part1, file_name)
    grayscale_image, detected_faces = detect_faces(file_path, face_cascade_xml)
    preprocessed_faces = preprocess_faces(grayscale_image, detected_faces)
    for face_image in preprocessed_faces:
        age, gender = extract_info_from_filename(file_name)
        face_images.append(face_image)
        genders.append(gender)
face_images = np.array(face_images)
genders = np.array(genders)
X_train, X_test, y_train, y_test = train_test_split(face_images, genders, test_size=0.2, random_state=42)
X_train_flat = X_train.reshape(X_train.shape[0], -1)
X_test_flat = X_test.reshape(X_test.shape[0], -1)
pca = PCA(n_components=50)
X_train_pca = pca.fit_transform(X_train_flat)
X_test_pca = pca.transform(X_test_flat)
clf_gender = MLPClassifier(hidden_layer_sizes=(15, 10), max_iter=1000, solver='adam', batch_size='auto', early_stopping=True)
clf_gender.fit(X_train_pca, y_train)
y_pred_gender = clf_gender.predict(X_test_pca)
accuracy_gender = np.mean(y_pred_gender == y_test) * 100
conf_matrix_gender = confusion_matrix(y_test, y_pred_gender)
print("Gender Prediction Accuracy: {:.2f}%".format(accuracy_gender))
print("Confusion Matrix for Gender Prediction:")
print(conf_matrix_gender)
plot_eigenvalues(pca.singular_values_)