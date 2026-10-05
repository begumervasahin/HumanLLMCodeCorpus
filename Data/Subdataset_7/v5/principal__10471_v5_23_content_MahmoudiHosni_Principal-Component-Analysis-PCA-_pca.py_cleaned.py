import os
from PIL import Image
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.decomposition import PCA
from sklearn.svm import SVC
b1 = []
b2 = "/home/hosni/Downloads/faces/"
for filename in os.listdir(b2):
    if '.pgm' not in filename:
        b3 = Image.open(os.path.join(b2, filename))
        b4 = np.array(b3).flatten()
        b1.append(b4)
b5 = []
for person_id in range(15):
    b5.extend([person_id] * 11)
b6 = PCA(n_components=165)
b7 = b6.fit_transform(b1)
x_train, x_test, y_train, b8 = train_test_split(b7, b5, test_size=0.33)
b9 = SVC(kernel='linear', C=1, decision_function_shape='ovr')
b9.fit(x_train, y_train)
b10 = b9.predict(x_test)
b11 = accuracy_score(b8, b10)
print("Accuracy:", b11)