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
    def fonk5(b2):
        return None
    @staticmethod
    def fonk6(b3):
        pass
class class5:
    @staticmethod
    def fonk7(b2):
        b3 = class4.fonk5(b2)
        if not b3:
            return f"{b2} is not a recognized b3"
        if b3.b1:
            return f"{b2} is already a moderator"
        b3.b1 = True
        class4.fonk6(b3)
        return f"{b2} is now a moderator"
    @staticmethod
    def fonk8(b2):
        b3 = class4.fonk5(b2)
        if not b3:
            return f"{b2} is not a recognized b3"
        if not b3.b1:
            return f"{b2} is not a current moderator"
        b3.b1 = False
        class4.fonk6(b3)
        return f"{b2} is no longer a moderator"
class class6:
    @staticmethod
    def fonk9():
        class2.fonk2()
        class2.fonk3()
        return "Dropped all tables. Created all tables."
if b4 = = '__main__':
    b5 = sys.argv[1]
    if b5 = = 'mod':
        print(class5.fonk7(sys.argv[2]))
    elif b5 = = 'rmmod':
        print(class5.fonk8(sys.argv[2]))
    elif b5 = = 'newdb':
        b6 = input('This will delete all data. Are you sure? (Y/n): ')
        if b6.upper() == 'Y':
            print(class6.fonk9())