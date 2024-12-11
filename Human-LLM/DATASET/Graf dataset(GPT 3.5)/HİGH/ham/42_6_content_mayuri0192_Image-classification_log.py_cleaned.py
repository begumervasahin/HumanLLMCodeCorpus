import utils
import filenames
class class1:
    def fonk1(self, b2, b3, b4):
        self.b1 = ""
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
    def fonk2(self):
        b5 = open(filenames.log(self.b2, self.b3, self.b4), "w")
        b5.write(self.b1)
        b5.close()
    def fonk3(self, time):
        b6 = "Time for getting all the local descriptors of the training images was {0}.\n"
        b7 = utils.humanize_time(time)
        self.b1 += b6.format(b7)
    def fonk4(self, time):
        b6 = "Time for generating the codebook with b2-means was {0}.\n"
        b7 = utils.humanize_time(time)
        self.b1 += b6.format(b7)
    def fonk5(self, time):
        self.fonk13(time, "training")
    def fonk6(self, time):
        b6 = "Time for calculating the SVM was {0}.\n"
        b7 = utils.humanize_time(time)
        self.b1 += b6.format(b7)
    def fonk7(self, time):
        self.fonk13(time, "testing")
    def fonk8(self, time):
        b7 = utils.humanize_time(time)
        self.b1 += "Elapsed time predicting the testing set is {0}\n".format(b7)
    def fonk9(self, accuracy):
        self.b1 += "b8 = {0}.\n".format(accuracy)
    def fonk10(self, classes):
        self.b1 += "b9 = {0}\n".format(classes)
    def fonk11(self, classes_counts):
        self.b1 += "b9 Local Descriptors b10 = {0}\n".format(classes_counts)
    def fonk12(self, conf_mat):
        self.b1 += "Confusion b11 = \n{0}".format(conf_mat)
    def fonk13(self, time, set):
        b6 = "Time for getting VLAD global descriptors of the {0} images was {1}.\n"
        b7 = utils.humanize_time(time)
        self.b1 += b6.format(set, b7)