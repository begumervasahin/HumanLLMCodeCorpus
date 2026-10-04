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
            file_name, b5 = os.b3.splitext(file)
            b6 = self.fonk5(b5[1:])
            if b6:
                b6 = b6.upper()
                print(f'{b6} <--- {file}')
                b7 = os.b3.join(self.b1, file)
                b8 = os.b3.join(self.b1, b6)
                if not os.b3.isdir(b8):
                    os.mkdir(b8)
                self.fonk6(b7, b8)
        print(f'\nProcess complete.\n')
    def fonk5(self, extension):
        for b1, extensions in self.b2.items():
            if extension.lower() in extensions:
                return b1
        return None
    def fonk6(self, b7, b8):
        try:
            shutil.move(b7, b8)
        except shutil.Error as err:
            print(f"Replacing old file >>> {err}")
            shutil.copy(b7, b8)
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