import shelve
class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
class class2:
    def fonk2(self):
        self.b4 = class1("hippo")
    def fonk3(self):
        print("Welcome to 20 Questions.")
        self.b4 = self.fonk4(self.b4)
    def fonk4(self, b6):
        if b6.b2 is None and b6.b3 is None:
            return self.fonk5(b6)
        else:
            print(b6.b1)
            b5 = input("Is it what you were thinking of? (y/n) ")
            if b5 = = "y":
                b6 = self.fonk4(b6.b3)
            elif b5 = = "n":
                b6 = self.fonk4(b6.b2)
            else:
                b6 = self.fonk4(b6)
            return b6
    def fonk5(self, b6):
        print("You're thinking of:", b6.b1)
        b5 = input("Is it what you were thinking of? (y/n) ")
        if b5 = = "y":
            print("I win!!")
            return b6
        else:
            return self.fonk6(b6)
    def fonk6(self, old_node):
        b7 = input("Enter the thing you were thinking of: ")
        b8 = input("Enter your disambiguating b8: ")
        b9 = input("Is the answer 'yes' or 'no' for your thing? (y/n) ")
        b7 = class1(b7)
        b10 = class1(b8)
        if b9 = = "y":
            b10.b3 = b7
            b10.b2 = old_node
        elif b9 = = "n":
            b10.b3 = old_node
            b10.b2 = b7
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
            return self.fonk6(old_node)
        return b10
def fonk7():
    b11 = shelve.open("b12.save")
    b12 = b11.get("tree", class2())
    try:
        b12.fonk3()
        b13 = True
        while b13:
            b11["tree"] = b12
            b5 = input("Do you want to play again? (y/n) ")
            if b5 = = "y":
                b12.fonk3()
            elif b5 = = "n":
                print("Thanks for playing! Goodbye.")
                b13 = False
            else:
                print("I'm sorry, I didn't understand you. Please enter 'y' or 'n'.")
    finally:
        b11.close()
if b14 = = "__main__":
    fonk7()