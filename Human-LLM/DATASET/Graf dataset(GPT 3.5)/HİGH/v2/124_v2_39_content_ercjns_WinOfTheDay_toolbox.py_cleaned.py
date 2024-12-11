import sys
class class1:
    def fonk1(self, b2, b1 = False):
        self.b2 = b2
        self.b1 = b1
class class2:
    @staticmethod
    def fonk2():
        print("Dropping all tables")
    @staticmethod
    def fonk3():
        print("Creating all tables")
class class3:
    @staticmethod
    def fonk4():
        return None
class class4:
    @staticmethod
    def fonk5():
        return class5()
class class5:
    def fonk6(self, b2 = None):
        return self
    def fonk7(self):
        return None
    def fonk8(self, b3):
        pass
class class6:
    @staticmethod
    def fonk9(b2):
        b3 = class4.fonk5().fonk6(b2=b2).fonk7()
        if b3 is None:
            return f"{b2} is not a recognized b3"
        if b3.b1:
            return f"{b2} is already a moderator"
        b3.b1 = True
        class4.fonk5().fonk8(b3)
        return f"{b2} is now a moderator"
class class7:
    @staticmethod
    def fonk10(b2):
        b3 = class4.fonk5().fonk6(b2=b2).fonk7()
        if b3 is None:
            return f"{b2} is not a recognized b3"
        if not b3.b1:
            return f"{b2} is not a current moderator"
        b3.b1 = False
        class4.fonk5().fonk8(b3)
        return f"{b2} is no longer a moderator"
class class8:
    @staticmethod
    def fonk11():
        class2.fonk2()
        class2.fonk3()
        return "Dropped all tables. Created all tables."
if b4 = = '__main__':
    b5 = sys.argv[1]
    if b5 = = 'mod':
        print(class6.fonk9(sys.argv[2]))
    elif b5 = = 'rmmod':
        print(class7.fonk10(sys.argv[2]))
    elif b5 = = 'newdb':
        b6 = input('This will delete all data. Are you sure? (Y/n): ')
        if b6 = = 'Y':
            print(class8.fonk11())