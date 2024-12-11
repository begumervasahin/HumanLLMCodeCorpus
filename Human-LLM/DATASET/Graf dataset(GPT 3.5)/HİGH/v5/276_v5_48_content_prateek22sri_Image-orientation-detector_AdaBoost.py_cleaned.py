from Model import Model
class class1(Model):
    def fonk1(self):
        super().fonk1()
        self.b1 = "adaboost"
b2 = class1()
print("class1 model type:", b2.b1)