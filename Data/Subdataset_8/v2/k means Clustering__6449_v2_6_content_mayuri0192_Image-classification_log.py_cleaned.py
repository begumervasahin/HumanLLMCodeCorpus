import utils
import filenames
class Log:
    def __init__(self, k, des_name, svm_kernel):
        self.text = ""
        self.k = k
        self.des_name = des_name
        self.svm_kernel = svm_kernel
    def save(self):
        file_path = filenames.log(self.k, self.des_name, self.svm_kernel)
        with open(file_path, "w") as file:
            file.write(self.text)
    def train_des_time(self, time):
        elapsed_time = utils.humanize_time(time)
        self.text += f"Time taken to collect local descriptors of training images: {elapsed_time}.\n"
    def codebook_time(self, time):
        elapsed_time = utils.humanize_time(time)
        self.text += f"Time taken to generate codebook with k-means: {elapsed_time}.\n"
    def train_vlad_time(self, time):
        elapsed_time = utils.humanize_time(time)
        self.text += f"Time taken to compute VLAD global descriptors for training: {elapsed_time}.\n"
    def svm_time(self, time):
        elapsed_time = utils.humanize_time(time)
        self.text += f"Time taken to compute SVM: {elapsed_time}.\n"
    def test_vlad_time(self, time):
        elapsed_time = utils.humanize_time(time)
        self.text += f"Time taken to compute VLAD global descriptors for testing: {elapsed_time}.\n"
    def predict_time(self, time):
        elapsed_time = utils.humanize_time(time)
        self.text += f"Elapsed time for predicting the testing set: {elapsed_time}\n"
    def accuracy(self, accuracy):
        self.text += f"Accuracy: {accuracy}.\n"
    def classes(self, classes):
        self.text += f"Classes: {classes}\n"
    def classes_counts(self, classes_counts):
        self.text += f"Counts of local descriptors per class: {classes_counts}\n"
    def confusion_matrix(self, conf_mat):
        self.text += f"Confusion Matrix:\n{conf_mat}"
log = Log(10, "sift", "rbf")
log.train_des_time(120)
log.codebook_time(300)
log.train_vlad_time(180)
log.svm_time(150)
log.test_vlad_time(90)
log.predict_time(60)
log.accuracy(0.85)
log.classes(["cat", "dog", "rabbit"])
log.classes_counts([100, 120, 80])
log.confusion_matrix("[[90, 5, 5], [10, 100, 10], [5, 5, 70]]")
log.save()