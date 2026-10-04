import utils
import filenames
class class1:
    def fonk1(self, b2, b3, b4):
        self.b1 = ""
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
    def fonk2(self):
        b5 = filenames.log(self.b2, self.b3, self.b4)
        with open(b5, "w") as file:
            file.write(self.b1)
    def fonk3(self, activity, time, b6 = None):
        b7 = utils.humanize_time(time)
        if b6:
            b8 = f"Time for {activity} {b6} was {b7}.\n"
        else:
            b8 = f"Time for {activity} was {b7}.\n"
        self.b1 += b8
    def fonk4(self, time):
        self.fonk3("getting all the local descriptors of the training images", time)
    def fonk5(self, time):
        self.fonk3("generating the codebook with b2-means", time)
    def fonk6(self, time):
        self.fonk3("getting VLAD global descriptors of the", time, "training")
    def fonk7(self, time):
        self.fonk3("calculating the SVM", time)
    def fonk8(self, time):
        self.fonk3("getting VLAD global descriptors of the", time, "testing")
    def fonk9(self, time):
        self.fonk3("predicting the testing set", time)
    def fonk10(self, accuracy):
        self.b1 += f"b9 = {accuracy}.\n"
    def fonk11(self, classes):
        self.b1 += f"b10 = {classes}\n"
    def fonk12(self, classes_counts):
        self.b1 += f"b10 Local Descriptors b11 = {classes_counts}\n"
    def fonk13(self, conf_mat):
        self.b1 += f"Confusion b12 = \n{conf_mat}"