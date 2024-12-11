import utils
import filenames
class class1:
    def fonk1(self, b2, b3, b4):
        self.b1 = ""
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
    def fonk2(self):
        b5 = open(filenames.b11(self.b2, self.b3, self.b4), "w")
        b5.write(self.b1)
        b5.close()
    def fonk3(self, time):
        b6 = utils.humanize_time(time)
        self.b1 += f"Time for getting all the local descriptors of the training images was {b6}.\n"
    def fonk4(self, time):
        b6 = utils.humanize_time(time)
        self.b1 += f"Time for generating the codebook with b2-means was {b6}.\n"
    def fonk5(self, time):
        self.fonk13(time, "training")
    def fonk6(self, time):
        b6 = utils.humanize_time(time)
        self.b1 += f"Time for calculating the SVM was {b6}.\n"
    def fonk7(self, time):
        self.fonk13(time, "testing")
    def fonk8(self, time):
        b6 = utils.humanize_time(time)
        self.b1 += f"Elapsed time predicting the testing set is {b6}\n"
    def fonk9(self, accuracy):
        self.b1 += f"b7 = {accuracy}.\n"
    def fonk10(self, classes):
        self.b1 += f"b8 = {classes}\n"
    def fonk11(self, classes_counts):
        self.b1 += f"b8 Local Descriptors b9 = {classes_counts}\n"
    def fonk12(self, conf_mat):
        self.b1 += f"Confusion b10 = \n{conf_mat}"
    def fonk13(self, time, set_name):
        b6 = utils.humanize_time(time)
        self.b1 += f"Time for getting VLAD global descriptors of the {set_name} images was {b6}.\n"
b11 = class1(10, "sift", "rbf")
b11.fonk3(120)
b11.fonk4(300)
b11.fonk5(180)
b11.fonk6(150)
b11.fonk7(90)
b11.fonk8(60)
b11.fonk9(0.85)
b11.fonk10(["cat", "dog", "rabbit"])
b11.fonk11([100, 120, 80])
b11.fonk12("[[90, 5, 5], [10, 100, 10], [5, 5, 70]]")
b11.fonk2()