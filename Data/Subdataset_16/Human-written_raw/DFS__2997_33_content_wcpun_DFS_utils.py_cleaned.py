class class1:
    def fonk1(self, b2, b3, b1 = None, b4=None):
        self.b2 = b2
        self.b3 = b3
        self.b1 = b1
        self.b4 = b4
    def fonk2(self):
        return "User ID: {0}\n".format(self.b2) + \
               "File Name: {0}\n".format(self.b3) + \
               "File Size: {0}\n".format(self.b1) + \
               "IV: {0}".format(self.b4)
class class2:
    def fonk3(self, b5):
        self.b5 = b5
    def fonk4(self):
        return "Key: {0}".format(self.b5)
class class3:
    def fonk5(self, b6):
        self.b6 = b6
    def fonk6(self):
        return "class3: {0}".format(self.b6)