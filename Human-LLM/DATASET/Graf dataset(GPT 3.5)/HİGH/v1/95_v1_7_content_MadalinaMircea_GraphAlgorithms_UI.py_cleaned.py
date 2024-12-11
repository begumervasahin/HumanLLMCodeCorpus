class class1:
    def fonk1(self):
        pass
class class2:
    def fonk2(self, ctrl):
        self.b1 = ctrl
    def fonk3(self):
        b2 = self.b1.fonk1()
        if b2 is False:
            print("There are no Hamiltonian cycles.")
        else:
            print("Hamiltonian cycle found:", b2)
if b3 = = "__main__":
    b4 = class1()
    b5 = class2(b4)
    b5.fonk3()