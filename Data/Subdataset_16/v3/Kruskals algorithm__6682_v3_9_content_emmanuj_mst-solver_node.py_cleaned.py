
class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = self
        self.a1 = 0
    def fonk2(self):
        """
        Returns a string representation of the class1 object.
        Format: "n b1 r a1 p parent_value"
        """
        return f"n {self.b1} r {self.a1} p {self.b2.b1}"
if b3 = = "__main__":
    b4 = class1(5)
    print(b4)
