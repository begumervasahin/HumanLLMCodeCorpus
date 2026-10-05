from sklearn import svm
from sklearn import decomposition
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from PIL import Image
import os
def fonk1(directory):
    b1 = []
    b2 = []
    for filename in os.listdir(directory):
        if '.pgm' not in filename:
            with Image.open(os.path.join(directory, filename)) as image:
                b3 = list(image.getdata())
                b4 = np.transpose(b3)
                b1.append(b4)
                b5 = int(filename.split('_')[0]) - 1
                b2.append(b5)
    return b1, b2
def fonk2():
    b6 = "/home/hosni/Downloads/faces/"
    b1, b2 = fonk1(b6)
    b7 = decomposition.PCA(n_components=165)
    b8 = b7.fit_transform(b1)
    x_train, x_test, y_train, b9 = train_test_split(b8, b2, test_size=0.33)
    b10 = svm.SVC(kernel='linear', C=1, decision_function_shape='ovr')
    b10.fit(x_train, y_train)
    b11 = b10.predict(x_test)
    b12 = accuracy_score(b9, b11)
    print("Accuracy:", b12)
if b13 = = "__main__":
    fonk2()