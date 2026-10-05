from sklearn import svm
from sklearn import decomposition
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from PIL import Image
import os
def load_data(directory):
    data = []
    labels = []
    for filename in os.listdir(directory):
        if '.pgm' not in filename:
            with Image.open(os.path.join(directory, filename)) as image:
                image_data = list(image.getdata())
                transposed_data = np.transpose(image_data)
                data.append(transposed_data)
                label = int(filename.split('_')[0]) - 1
                labels.append(label)
    return data, labels
def main():
    data_directory = "/home/hosni/Downloads/faces/"
    data, labels = load_data(data_directory)
    pca = decomposition.PCA(n_components=165)
    transformed_data = pca.fit_transform(data)
    x_train, x_test, y_train, y_test = train_test_split(transformed_data, labels, test_size=0.33)
    svm_classifier = svm.SVC(kernel='linear', C=1, decision_function_shape='ovr')
    svm_classifier.fit(x_train, y_train)
    predictions = svm_classifier.predict(x_test)
    accuracy = accuracy_score(y_test, predictions)
    print("Accuracy:", accuracy)
if __name__ == "__main__":
    main()