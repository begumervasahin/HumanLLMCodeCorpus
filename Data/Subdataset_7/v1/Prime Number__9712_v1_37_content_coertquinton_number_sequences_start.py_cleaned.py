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
    def fonk3(self, b9):
        return b9 in self.b1
    def fonk4(self, b9):
        return self.b1.get(b9, self.b1[self.a1])
class class2:
    def fonk5(self):
        b2 = class1()
        self.b3 = b2.fonk4(b2.a1)
        self.b4 = {
            0: 'Change printer. Default is simple numbers.',
            1: 'Exit',
            2: 'Print prime numbers',
            3: 'Print Fibonacci numbers',
            4: 'Print Collatz Conjecture',
            5: 'Print strong prime numbers',
        }
        sorted(self.b4.keys())
    def fonk6(self):
        while True:
            self.fonk7()
            b5 = input('Type menu item number to start math operation: ')
            if int(b5) == 0:
                self.fonk11()
                continue
            if self.fonk8(b5):
                if int(b5) == 1:
                    break
                print(b5 + ' has been selected')
                self.fonk9(int(b5))
                self.fonk10()
    def fonk7(self):
        print('---------------------------------------------------')
        print('Type the corresponding number to access a menu item')
        for key, value in self.b4.items():
            print(str(key) + ': ' + value)
    def fonk8(self, b5):
        b6 = f'Menu Item {b5} is not a valid choice. Input must be an integer between 0 and {len(self.b4) - 1}'
        try:
            if not b5.isdigit():
                print(b6)
                return False
            b7 = int(b5)
            if b7 in self.b4:
                return True
            else:
                print('Invalid menu item chosen.')
                return False
            print(b6)
            return False
        except:
            print(b6)
    def fonk9(self, b5):
        pass
    def fonk10(self):
        pass
    def fonk11(self):
        b8 = class1()
        b8.fonk2()
        b9 = int(input("Type the number of the type of output you would like to see: "))
        if b8.fonk3(b9):
            self.b3 = b8.fonk4(b9)
            print(f"Printer set to {b8.b1[b9]}")
        else:
            self.b3 = b8.fonk4(b8.a1)
            print("Incorrect printer selected. Printer set to Simple number printer.")
if b10 = = '__main__':
    print('Program start')
    b11 = class2()
    b11.fonk6()
    print('Program terminated')