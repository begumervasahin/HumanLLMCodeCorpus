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
        ''' Load json file '''
        with open('extensions.json', 'r') as extension_file:
            return json.load(extension_file)
    def fonk4(self):
        ''' Execute main flow of program '''
        print(f'\nWorking in directory: {self.b1}\n')
        b4 = os.listdir(self.b1)
        for file in b4:
            name, b5 = os.b3.splitext(file)
            b1 = self.fonk5(b5[1:])
            if b1 is not None:
                print(f'{b1.upper()} <--- {file}')
                b1 = b1.upper()
                b6 = os.b3.join(self.b1, file)
                b7 = os.b3.join(self.b1, b1)
                if not os.b3.isdir(b7):
                    os.mkdir(b7)
                self.fonk6(b6, b7)
        print(f'\nProcess complete.\n')
    def fonk5(self, ext):
        ''' Compare file extensions with extensions present in json file '''
        for b1, extensions in self.b2.items():
            if ext.lower() in extensions:
                return b1
    def fonk6(self, b6, b1):
        ''' Move b4 to a b1 '''
        try:
            shutil.fonk6(b6, b1)
        except shutil.Error as err:
            print(f"Replacing old file >>> {err}")
            shutil.copy(b6, b1)
            os.remove(b6)
if b8 = = '__main__':
    b9 = sys.argv
    try:
        if len(b9) > 1:
            for argument in b9[1:]:
                class1(argument).fonk4()
        else:
            class1().fonk4()
    except FileNotFoundError as err:
        sys.exit(f'No such directory found. {err}')