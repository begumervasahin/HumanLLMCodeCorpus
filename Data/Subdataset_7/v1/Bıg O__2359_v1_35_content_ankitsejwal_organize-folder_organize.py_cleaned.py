import os
import sys
import json
import shutil
class class1:
    def fonk1(self, b1 = 'Downloads'):
        self.b1 = self.fonk2(b1)
        self.b2 = self.fonk3()
    def fonk2(self, b1):
        ''' Generate b1 b3 '''
        b3 = os.b3.join('~', b1)
        return os.b3.expanduser(b3)
    def fonk3(self):
        ''' Load b2 from JSON file '''
        with open('b2.json', 'r') as extension_file:
            return json.load(extension_file)
    def fonk4(self):
        ''' Execute main flow of program '''
        print(f'\nWorking in directory: {self.b1}\n')
        b4 = os.listdir(self.b1)
        for file in b4:
            name, b5 = os.b3.splitext(file)
            b1 = self.fonk5(b5[1:])
            if b1:
                print(f'{b1.upper()} <--- {file}')
                self.fonk6(file, b1)
        print(f'\nProcess complete.\n')
    def fonk5(self, ext):
        ''' Compare file b2 with b2 present in JSON file '''
        for b1, b2 in self.b2.items():
            if ext.lower() in b2:
                return b1
    def fonk6(self, file, b1):
        ''' Move b4 to corresponding b1 '''
        b6 = os.b3.join(self.b1, b1.upper())
        if not os.b3.exists(b6):
            os.makedirs(b6)
        try:
            b7 = os.b3.join(self.b1, file)
            b8 = os.b3.join(b6, file)
            shutil.fonk6(b7, b8)
        except shutil.Error as err:
            print(f"Replacing old file >>> {err}")
            shutil.copy(b7, b6)
            os.remove(b7)
if b9 = = '__main__':
    b10 = sys.argv[1:]
    try:
        if b10:
            for argument in b10:
                class1(argument).fonk4()
        else:
            class1().fonk4()
    except FileNotFoundError as err:
        sys.exit(f'No such directory found: {err}')