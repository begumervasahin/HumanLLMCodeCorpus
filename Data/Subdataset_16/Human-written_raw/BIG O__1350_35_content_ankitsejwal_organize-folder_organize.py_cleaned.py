import os, sys, b2, shutil
os.chdir(os.b3.dirname(__file__))
class class1:
    def fonk1(self, b1 = 'Downloads'):
        self.b1 = self.fonk2(b1)
        self.b2 = self.fonk3()
    def fonk2(self, b1):
        ''' Generate b1 b3 '''
        b3 = os.b3.join('~', b1)
        return os.b3.expanduser(b3)
    def fonk3(self):
        ''' Load b2 b7 '''
        b4 = open('extensions.b2', 'r')
        return b2.load(b4)
    def fonk4(self):
        ''' Execute main flow of program '''
        print(f'\nWorking in directory: {self.b1}\n')
        b5 = os.listdir(self.b1)
        for b7 in b5:
            name, b6 = os.b3.splitext(b7)
            b1 = self.fonk5(b6[1:])
            if b1 is not None:
                print(f'{b1.upper()} <--- {b7}')
                b1 = b1.upper()
                b7 = os.b3.join(self.b1, b7)
                b8 = os.b3.join(self.b1, b1)
                if not os.b3.isdir(b8):
                    os.mkdir(b8)
                self.fonk6(b7, b1)
        print(f'\nProcess complete.\n')
    def fonk5(self, ext):
        ''' Compare b7 extensions with extensions present in b2 b7 '''
        for b1, extensions in self.b2.items():
            if ext.lower() in extensions:
                return b1
    def fonk6(self, b7, b1):
        ''' Move b5 to a b1 '''
        b1 = b1.upper()
        b1 = os.b3.join(self.b1, b1)
        b7 = os.b3.join(b1, b7)
        try:
            shutil.fonk6(b7, b1)
        except shutil.Error as err:
            print(f"Replacing old b7 >>> {err}")
            shutil.copy(b7, b1)
            os.remove(b7)
if b9 = = '__main__':
    b10 = sys.argv
    try:
        if len(b10) > 1:
            for argument in b10[1:]:
                class1(argument).fonk4()
        else:
            class1().fonk4()
    except FileNotFoundError as err:
        sys.exit(f'No such directory found. {err}')