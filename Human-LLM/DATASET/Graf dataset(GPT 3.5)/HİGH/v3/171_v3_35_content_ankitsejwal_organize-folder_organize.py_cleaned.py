import os
import sys
import json
import shutil
class class1:
    def fonk1(self, b1 = 'Downloads'):
        self.b2 = self.fonk2(b1)
        self.b3 = self.fonk3()
    def fonk2(self, b7):
        b4 = os.b4.join('~', b7)
        return os.b4.expanduser(b4)
    def fonk3(self):
        with open('b3.json', 'r') as extension_file:
            return json.load(extension_file)
    def fonk4(self):
        print(f'\nWorking in directory: {self.b2}\n')
        b5 = os.listdir(self.b2)
        for file_name in b5:
            name, b6 = os.b4.splitext(file_name)
            b7 = self.fonk5(b6[1:])
            if b7:
                print(f'{b7.upper()} <--- {file_name}')
                self.fonk6(file_name, b7)
        print(f'\nOrganizing process complete.\n')
    def fonk5(self, ext):
        for b7, b3 in self.b3.items():
            if ext.lower() in b3:
                return b7
    def fonk6(self, file_name, b7):
        b2 = os.b4.join(self.b2, b7.upper())
        if not os.b4.exists(b2):
            os.makedirs(b2)
        try:
            b8 = os.b4.join(self.b2, file_name)
            b9 = os.b4.join(b2, file_name)
            shutil.move(b8, b9)
        except shutil.Error as err:
            print(f"Error moving file: {err}")
            shutil.copy(b8, b2)
            os.remove(b8)
if b10 = = '__main__':
    try:
        b11 = sys.argv[1:]
        if b11:
            for b7 in b11:
                class1(b7).fonk4()
        else:
            class1().fonk4()
    except FileNotFoundError as err:
        sys.exit(f'Error: {err} - No such directory found.')