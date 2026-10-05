import os
from PIL import Image
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.decomposition import PCA
from sklearn.svm import SVC
image_data = []
directory = "/home/hosni/Downloads/faces/"
for filename in os.listdir(directory):
    if '.pgm' not in filename:
        image = Image.open(os.path.join(directory, filename))
        data = np.array(image).flatten()
        image_data.append(data)
labels = []
for person_id in range(15):
    labels.extend([person_id] * 11)
pca = PCA(n_components=165)
reduced_image_data = pca.fit_transform(image_data)
x_train, x_test, y_train, y_test = train_test_split(reduced_image_data, labels, test_size=0.33)
clf = SVC(kernel='linear', C=1, decision_function_shape='ovr')
clf.fit(x_train, y_train)
predicted_labels = clf.predict(x_test)
accuracy = accuracy_score(y_test, predicted_labels)
print("Accuracy:", accuracy)