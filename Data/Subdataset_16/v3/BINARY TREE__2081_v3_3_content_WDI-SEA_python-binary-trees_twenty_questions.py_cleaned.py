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
        if self.fonk5(node):
            return self.fonk6(node)
        else:
            return self.fonk7(node)
    def fonk5(self, node):
        return node.b2 is None and node.b3 is None
    def fonk6(self, node):
        print(f"You're thinking of: {node.b1}")
        b5 = self.fonk9("Is it correct (y/n)? ")
        if b5 = = "y":
            print("I win!!")
            return node
        else:
            return self.fonk8(node)
    def fonk7(self, node):
        print(node.b1)
        b5 = self.fonk9("y/n? ")
        if b5 = = "y":
            node.b3 = self.fonk4(node.b3)
        elif b5 = = "n":
            node.b2 = self.fonk4(node.b2)
        return node
    def fonk8(self, old_node):
        b6 = input("Enter the thing you were thinking of: ").strip()
        b7 = input("Enter your disambiguating b7: ").strip()
        b8 = self.fonk9("Is your thing the answer to the b7 (y/n)? ")
        b9 = class1(b6)
        b10 = class1(b7)
        if b8 = = "y":
            b10.b3 = b9
            b10.b2 = old_node
        elif b8 = = "n":
            b10.b3 = old_node
            b10.b2 = b9
        return b10
    def fonk9(self, prompt):
        while True:
            b5 = input(prompt).strip().lower()
            if b5 in {"y", "n"}:
                return b5
            print("Invalid input. Please enter 'y' or 'n'.")
def fonk10():
    with shelve.open("b11.save") as savefile:
        b11 = savefile.get("tree", class2())
        b11.fonk3()
        while True:
            savefile["tree"] = b11
            b5 = input("Do you want to play again (y/n)? ").strip().lower()
            if b5 = = "y":
                b11.fonk3()
            elif b5 = = "n":
                print("Thanks for playing! Goodbye.")
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'.")
if b12 = = "__main__":
    fonk10()