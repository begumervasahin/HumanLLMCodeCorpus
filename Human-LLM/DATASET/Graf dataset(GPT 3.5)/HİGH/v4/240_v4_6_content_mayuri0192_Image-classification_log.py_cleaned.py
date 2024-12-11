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
    def fonk3(self, activity, time, b5 = None):
        b6 = utils.humanize_time(time)
        if b5:
            b7 = f"Time for {activity} {b5} was {b6}.\n"
        else:
            b7 = f"Time for {activity} was {b6}.\n"
        self.b1 += b7
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
        self.b1 += f"b8 = {accuracy}.\n"
    def fonk11(self, classes):
        self.b1 += f"b9 = {classes}\n"
    def fonk12(self, classes_counts):
        self.b1 += f"b9 Local Descriptors b10 = {classes_counts}\n"
    def fonk13(self, conf_mat):
        self.b1 += f"Confusion b11 = \n{conf_mat}"