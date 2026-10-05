import utils
import filenames
class class1:
    def fonk1(self, b2, b3, b4):
        self.b1 = ""
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
    def fonk2(self):
        b5 = filenames.b7(self.b2, self.b3, self.b4)
        with open(b5, "w") as file:
            file.write(self.b1)
    def fonk3(self, time):
        b6 = utils.humanize_time(time)
        self.b1 += f"Time taken to collect local descriptors of training images: {b6}.\n"
    def fonk4(self, time):
        b6 = utils.humanize_time(time)
        self.b1 += f"Time taken to generate codebook with b2-means: {b6}.\n"
    def fonk5(self, time):
        b6 = utils.humanize_time(time)
        self.b1 += f"Time taken to compute VLAD global descriptors for training: {b6}.\n"
    def fonk6(self, time):
        b6 = utils.humanize_time(time)
        self.b1 += f"Time taken to compute SVM: {b6}.\n"
    def fonk7(self, time):
        b6 = utils.humanize_time(time)
        self.b1 += f"Time taken to compute VLAD global descriptors for testing: {b6}.\n"
    def fonk8(self, time):
        b6 = utils.humanize_time(time)
        self.b1 += f"Elapsed time for predicting the testing set: {b6}\n"
    def fonk9(self, accuracy):
        self.b1 += f"Accuracy: {accuracy}.\n"
    def fonk10(self, classes):
        self.b1 += f"Classes: {classes}\n"
    def fonk11(self, classes_counts):
        self.b1 += f"Counts of local descriptors per class: {classes_counts}\n"
    def fonk12(self, conf_mat):
        self.b1 += f"Confusion Matrix:\n{conf_mat}"
b7 = class1(10, "sift", "rbf")
b7.fonk3(120)
b7.fonk4(300)
b7.fonk5(180)
b7.fonk6(150)
b7.fonk7(90)
b7.fonk8(60)
b7.fonk9(0.85)
b7.fonk10(["cat", "dog", "rabbit"])
b7.fonk11([100, 120, 80])
b7.fonk12("[[90, 5, 5], [10, 100, 10], [5, 5, 70]]")
b7.fonk2()