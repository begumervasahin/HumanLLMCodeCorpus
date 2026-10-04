import utils
import filenames
class class1:
    def fonk1(self, b2, b3, b4):
        self.b1 = ""
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
    def fonk2(self):
        with open(filenames.log(self.b2, self.b3, self.b4), "w") as file:
            file.write(self.b1)
    def fonk3(self, description, time):
        b5 = utils.humanize_time(time)
        self.b1 += f"{description} {b5}.\n"
    def fonk4(self, time):
        self.fonk3("Time for getting all the local descriptors of the training images was", time)
    def fonk5(self, time):
        self.fonk3("Time for generating the codebook with b2-means was", time)
    def fonk6(self, time):
        self.fonk3("Time for getting VLAD global descriptors of the training images was", time)
    def fonk7(self, time):
        self.fonk3("Time for calculating the SVM was", time)
    def fonk8(self, time):
        self.fonk3("Time for getting VLAD global descriptors of the testing images was", time)
    def fonk9(self, time):
        self.fonk3("Elapsed time predicting the testing set is", time)
    def fonk10(self, accuracy):
        self.b1 += f"b6 = {accuracy}.\n"
    def fonk11(self, classes):
        self.b1 += f"b7 = {classes}\n"
    def fonk12(self, classes_counts):
        self.b1 += f"b7 Local Descriptors b8 = {classes_counts}\n"
    def fonk13(self, conf_mat):
        self.b1 += f"Confusion b9 = \n{conf_mat}\n"