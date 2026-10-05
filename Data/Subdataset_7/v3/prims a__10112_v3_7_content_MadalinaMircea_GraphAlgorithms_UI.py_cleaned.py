class class1:
    def fonk1(self):
        pass
class class2:
    def fonk2(self, b1):
        self.b1 = b1
    def fonk3(self):
        b2 = self.b1.fonk1()
        if b2 is False:
            print("No Hamiltonian cycles found.")
        else:
            print("Hamiltonian cycle found:", b2)
if b3 = = "__main__":
    b1 = class1()
    b4 = class2(b1)
    b4.fonk3()