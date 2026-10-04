import utils
import filenames
class Log:
    def __init__(self, k, des_name, svm_kernel):
        self.text = ""
        self.k = k
        self.des_name = des_name
        self.svm_kernel = svm_kernel
    def save(self):
        log_path = filenames.log(self.k, self.des_name, self.svm_kernel)
        with open(log_path, "w") as file:
            file.write(self.text)
    def _append_time_log(self, description, time):
        elapsed_time = utils.humanize_time(time)
        self.text += f"{description} {elapsed_time}.\n"
    def train_des_time(self, time):
        self._append_time_log("Time for getting all the local descriptors of the training images was", time)
    def codebook_time(self, time):
        self._append_time_log("Time for generating the codebook with k-means was", time)
    def train_vlad_time(self, time):
        self._append_time_log("Time for getting VLAD global descriptors of the training images was", time)
    def svm_time(self, time):
        self._append_time_log("Time for calculating the SVM was", time)
    def test_vlad_time(self, time):
        self._append_time_log("Time for getting VLAD global descriptors of the testing images was", time)
    def predict_time(self, time):
        self._append_time_log("Elapsed time predicting the testing set is", time)
    def accuracy(self, accuracy):
        self.text += f"Accuracy = {accuracy}.\n"
    def classes(self, classes):
        self.text += f"Classes = {classes}\n"
    def classes_counts(self, classes_counts):
        self.text += f"Classes Local Descriptors Counts = {classes_counts}\n"
    def confusion_matrix(self, conf_mat):
        self.text += f"Confusion Matrix =\n{conf_mat}\n"