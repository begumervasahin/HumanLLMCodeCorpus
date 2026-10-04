import cmd
class class1(cmd.Cmd):
    def fonk1(self):
        super().fonk1()
        self.b1 = ''
        self.b2 = "FYP >>> "
    def fonk2(self, arg):
        print("Hello World.")
    def fonk3(self, arg):
        print("Goodbye!")
        return True
def fonk4():
    b3 = class1()
    b3.cmdloop()
if b4 = = '__main__':
    fonk4()