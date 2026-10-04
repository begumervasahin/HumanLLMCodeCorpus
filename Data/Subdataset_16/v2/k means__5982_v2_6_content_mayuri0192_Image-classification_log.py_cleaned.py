import utils
import filenames
class class1:
    def fonk1(self, b2, b3, b4):
        self.b1 = ""
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
    def fonk2(self):
        b5 = filenames.b12(self.b2, self.b3, self.b4)
        with open(b5, "w") as file:
            file.write(self.b1)
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
    def fonk13(self, time, set):
        b6 = utils.humanize_time(time)
        self.b1 += f"Time for getting VLAD global descriptors of the {set} images was {b6}.\n"
if b11 = = "__main__":
    b12 = class1(b2=10, b3="SIFT", b4="linear")
    b12.fonk3(120)
    b12.fonk4(300)
    b12.fonk5(180)
    b12.fonk6(60)
    b12.fonk7(90)
    b12.fonk8(30)
    b12.fonk9(0.85)
    b12.fonk10(["cat", "dog"])
    b12.fonk11({"cat": 100, "dog": 120})
    b12.fonk12([[90, 10], [20, 100]])
    b12.fonk2()