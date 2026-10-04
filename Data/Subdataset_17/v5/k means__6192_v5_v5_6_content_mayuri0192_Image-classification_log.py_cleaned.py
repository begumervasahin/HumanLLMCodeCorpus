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
    def log_time(self, activity, time, set_name=None):
        time_str = utils.humanize_time(time)
        activity_message = f"Time for {activity}"
        if set_name:
            activity_message += f" {set_name}"
        activity_message += f" was {time_str}.\n"
        self.text += activity_message
    def train_des_time(self, time):
        self.log_time("getting all the local descriptors of the training images", time)
    def codebook_time(self, time):
        self.log_time("generating the codebook with k-means", time)
    def train_vlad_time(self, time):
        self.log_time("getting VLAD global descriptors of the training set", time)
    def svm_time(self, time):
        self.log_time("calculating the SVM", time)
    def test_vlad_time(self, time):
        self.log_time("getting VLAD global descriptors of the testing set", time)
    def predict_time(self, time):
        self.log_time("predicting the testing set", time)
    def accuracy(self, accuracy):
        self.text += f"Accuracy = {accuracy}.\n"
    def classes(self, classes):
        self.text += f"Classes = {classes}\n"
    def classes_counts(self, classes_counts):
        self.text += f"Classes Local Descriptors Counts = {classes_counts}\n"
    def confusion_matrix(self, conf_mat):
        self.text += f"Confusion Matrix =\n{conf_mat}"