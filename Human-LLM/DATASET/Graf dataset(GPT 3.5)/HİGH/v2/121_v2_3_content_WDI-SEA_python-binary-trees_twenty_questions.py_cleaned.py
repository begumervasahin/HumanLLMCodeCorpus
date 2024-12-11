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
    def fonk4(self, node):
        if node.b2 is None and node.b3 is None:
            print("You're thinking of:", node.b1)
            b5 = input("Is it what you were thinking of? (y/n) ")
            if b5 = = "y":
                print("I win!!")
                return node
            else:
                return self.fonk5(node)
        else:
            print(node.b1)
            b5 = input("Is it what you were thinking of? (y/n) ")
            if b5 = = "y":
                node.b3 = self.fonk4(node.b3)
            elif b5 = = "n":
                node.b2 = self.fonk4(node.b2)
            else:
                self.fonk4(node)
            return node
    def fonk5(self, old_node):
        b6 = input("Enter the thing you were thinking of: ")
        b7 = input("Enter your disambiguating b7: ")
        b8 = input("Is the answer 'yes' or 'no' for your thing? (y/n) ")
        b6 = class1(b6)
        b9 = class1(b7)
        if b8 = = "y":
            b9.b3 = b6
            b9.b2 = old_node
        elif b8 = = "n":
            b9.b3 = old_node
            b9.b2 = b6
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
            return self.fonk5(old_node)
        return b9
b10 = shelve.open("b11.save")
if "tree" in b10:
    b11 = b10["tree"]
else:
    b11 = class2()
b11.fonk3()
b12 = True
while b12:
    b10["tree"] = b11
    b5 = input("Do you want to play again? (y/n) ")
    if b5 = = "y":
        b11.fonk3()
    elif b5 = = "n":
        print("Thanks for playing! Goodbye.")
        b12 = False
    else:
        print("I'm sorry, I didn't understand you. Please enter 'y' or 'n'.")
b10.close()