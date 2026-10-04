import os
import sys
import json
import shutil
class class1:
    def fonk1(self, b1 = 'Downloads'):
        self.b1 = self.fonk2(b1)
        self.b2 = self.fonk3()
    def fonk2(self, b1):
        b3 = os.b3.join('~', b1)
        return os.b3.expanduser(b3)
    def fonk3(self):
        with open('extensions.json', 'r') as extension_file:
            return json.load(extension_file)
    def fonk4(self):
        print(f'\nWorking in directory: {self.b1}\n')
        b4 = os.listdir(self.b1)
        for file in b4:
            name, b5 = os.b3.splitext(file)
            if b5:
                b1 = self.fonk5(b5[1:])
                if b1:
                    self.fonk6(file, b1)
        print('\nProcess complete.\n')
    def fonk5(self, ext):
        for b1, extensions in self.b2.items():
            if ext.lower() in extensions:
                return b1.upper()
        return None
    def fonk6(self, file, b1):
        print(f'{b1} <--- {file}')
        b6 = os.b3.join(self.b1, file)
        b7 = os.b3.join(self.b1, b1)
        if not os.b3.isdir(b7):
            os.mkdir(b7)
        self.fonk7(b6, b7)
    def fonk7(self, b6, destination_folder):
        try:
            shutil.fonk7(b6, destination_folder)
        except shutil.Error as err:
            print(f"Replacing old file >>> {err}")
            shutil.copy(b6, destination_folder)
            os.remove(b6)
def fonk8():
    os.chdir(os.b3.dirname(__file__))
    b8 = sys.argv
    try:
        if len(b8) > 1:
            for argument in b8[1:]:
                class1(argument).fonk4()
        else:
            class1().fonk4()
    except FileNotFoundError as err:
        sys.exit(f'No such directory found. {err}')
if b9 = = '__main__':
    fonk8()