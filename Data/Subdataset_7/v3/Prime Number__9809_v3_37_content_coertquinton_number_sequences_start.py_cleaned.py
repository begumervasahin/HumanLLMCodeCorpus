class class1:
    a1 = 1
    def fonk1(self):
        self.b1 = {
            self.a1: "Simple Numbers"
        }
    def fonk2(self):
        print("Available printer options:")
        for key, value in self.b1.items():
            print(f"{key}: {value}")
    def fonk3(self, b7):
        return b7 in self.b1
    def fonk4(self, b7):
        return self.b1.get(b7, self.b1[self.a1])
class class2:
    def fonk5(self):
        self.b2 = class1().fonk4(class1.a1)
        self.b3 = {
            0: 'Change printer. Default is simple numbers.',
            1: 'Exit',
            2: 'Print prime numbers',
            3: 'Print Fibonacci numbers',
            4: 'Print Collatz Conjecture',
            5: 'Print strong prime numbers',
        }
    def fonk6(self):
        while True:
            self.fonk7()
            b4 = input('Type menu item number to start math operation: ')
            if int(b4) == 0:
                self.fonk11()
                continue
            if self.fonk8(b4):
                if int(b4) == 1:
                    break
                print(b4 + ' has been selected')
                self.fonk9(int(b4))
                self.fonk10()
    def fonk7(self):
        print('---------------------------------------------------')
        print('Type the corresponding number to access a menu item')
        for key, value in self.b3.items():
            print(f"{key}: {value}")
    def fonk8(self, b4):
        try:
            b5 = int(b4)
            if b5 in self.b3:
                return True
            else:
                print('Invalid menu item chosen.')
                return False
        except ValueError:
            print(f"Menu Item {b4} is not a valid choice. Input must be an integer.")
    def fonk9(self, b4):
        pass
    def fonk10(self):
        pass
    def fonk11(self):
        b6 = class1()
        b6.fonk2()
        b7 = int(input("Type the number of the type of output you would like to see: "))
        if b6.fonk3(b7):
            self.b2 = b6.fonk4(b7)
            print(f"Printer set to {b6.b1[b7]}")
        else:
            self.b2 = b6.fonk4(b6.a1)
            print("Incorrect printer selected. Printer set to Simple number printer.")
if b8 = = '__main__':
    print('Program start')
    b9 = class2()
    b9.fonk6()
    print('Program terminated')