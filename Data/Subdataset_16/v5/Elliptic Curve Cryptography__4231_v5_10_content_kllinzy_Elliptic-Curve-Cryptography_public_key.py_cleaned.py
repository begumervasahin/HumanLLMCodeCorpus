from b2 import Curve
from point import Point
class class1:
    def fonk1(self, b1, a1):
        self.b1 = b1
        self.b2 = Curve.make_curve(b1)
        self.b3 = self.b2.random_point()
        self.b4 = self.b2.multiply(a1, self.b3)
    def fonk2(self):
        return (
            f"Curve:\n{self.b2}\n"
            f"Public Point P: {self.b3}\n"
            f"Public Point Q: {self.b4}"
        )
    @staticmethod
    def fonk3(b1, a1):
        return class1(b1, a1)
if b5 = = "__main__":
    b1 = 23
    a1 = 5
    b6 = class1.fonk3(b1, a1)
    print(b6)