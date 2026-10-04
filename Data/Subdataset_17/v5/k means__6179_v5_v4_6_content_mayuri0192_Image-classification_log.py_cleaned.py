import utils
import filenames
class Log:
    def __init__(self, k, des_name, svm_kernel):
        self.text = ""
        self.k = k
        self.des_name = des_name
        self.svm_kernel = svm_kernel
    def save(self):
        log_filename = filenames.log(self.k, self.des_name, self.svm_kernel)
        with open(log_filename, "w") as file:
            file.write(self.text)
    def log_time(self, activity, duration, extra_info=None):
        time_str = utils.humanize_time(duration)
        if extra_info:
            message = f"Time for {activity} {extra_info} was {time_str}.\n"
        else:
            message = f"Time for {activity} was {time_str}.\n"
        self.text += message
    def train_des_time(self, duration):
        self.log_time("getting all the local descriptors of the training images", duration)
    def codebook_time(self, duration):
        self.log_time("generating the codebook with k-means", duration)
    def train_vlad_time(self, duration):
        self.log_time("getting VLAD global descriptors of the", duration, "training")
    def svm_time(self, duration):
        self.log_time("calculating the SVM", duration)
    def test_vlad_time(self, duration):
        self.log_time("getting VLAD global descriptors of the", duration, "testing")
    def predict_time(self, duration):
        self.log_time("predicting the testing set", duration)
    def accuracy(self, accuracy):
        self.text += f"Accuracy = {accuracy}.\n"
    def classes(self, classes):
        self.text += f"Classes = {classes}\n"
    def classes_counts(self, class_counts):
        self.text += f"Classes Local Descriptors Counts = {class_counts}\n"
    def confusion_matrix(self, conf_matrix):
        self.text += f"Confusion Matrix =\n{conf_matrix}\n"
