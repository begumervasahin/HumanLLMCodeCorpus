import os
import sys
import json
import shutil
class Organize:
    def __init__(self, folder='Downloads'):
        self.folder = self.get_folder_path(folder)
        self.extension_map = self.load_extension_map()
    def get_folder_path(self, folder):
        path = os.path.join('~', folder)
        return os.path.expanduser(path)
    def load_extension_map(self):
        with open('extensions.json', 'r') as extension_file:
            return json.load(extension_file)
    def execute(self):
        print(f'\nWorking in directory: {self.folder}\n')
        files = os.listdir(self.folder)
        for file in files:
            name, extension = os.path.splitext(file)
            if extension:
                folder = self.map_folder(extension[1:])
                if folder:
                    self.organize_file(file, folder)
        print('\nProcess complete.\n')
    def map_folder(self, ext):
        for folder, extensions in self.extension_map.items():
            if ext.lower() in extensions:
                return folder.upper()
        return None
    def organize_file(self, file, folder):
        print(f'{folder} <--- {file}')
        file_path = os.path.join(self.folder, file)
        new_folder_path = os.path.join(self.folder, folder)
        if not os.path.isdir(new_folder_path):
            os.mkdir(new_folder_path)
        self.move(file_path, new_folder_path)
    def move(self, file_path, destination_folder):
        try:
            shutil.move(file_path, destination_folder)
        except shutil.Error as err:
            print(f"Replacing old file >>> {err}")
            shutil.copy(file_path, destination_folder)
            os.remove(file_path)
def main():
    os.chdir(os.path.dirname(__file__))
    arguments = sys.argv
    try:
        if len(arguments) > 1:
            for argument in arguments[1:]:
                Organize(argument).execute()
        else:
            Organize().execute()
    except FileNotFoundError as err:
        sys.exit(f'No such directory found. {err}')
if __name__ == '__main__':
    main()