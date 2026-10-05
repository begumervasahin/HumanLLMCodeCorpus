import os
import sys
import json
import shutil
class FileOrganizer:
    def __init__(self, folder='Downloads'):
        self.folder_path = self.get_folder_path(folder)
        self.extensions = self.load_extensions()
    def get_folder_path(self, folder_name):
        path = os.path.join('~', folder_name)
        return os.path.expanduser(path)
    def load_extensions(self):
        with open('extensions.json', 'r') as extension_file:
            return json.load(extension_file)
    def execute(self):
        print(f'\nWorking in directory: {self.folder_path}\n')
        files = os.listdir(self.folder_path)
        for file_name in files:
            name, extension = os.path.splitext(file_name)
            folder_name = self.map_folder(extension[1:])
            if folder_name:
                print(f'{folder_name.upper()} <--- {file_name}')
                self.move_file(file_name, folder_name)
        print(f'\nOrganizing process complete.\n')
    def map_folder(self, ext):
        for folder_name, extensions in self.extensions.items():
            if ext.lower() in extensions:
                return folder_name
    def move_file(self, file_name, folder_name):
        folder_path = os.path.join(self.folder_path, folder_name.upper())
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        try:
            source_path = os.path.join(self.folder_path, file_name)
            destination_path = os.path.join(folder_path, file_name)
            shutil.move(source_path, destination_path)
        except shutil.Error as err:
            print(f"Error moving file: {err}")
            shutil.copy(source_path, folder_path)
            os.remove(source_path)
if __name__ == '__main__':
    try:
        arguments = sys.argv[1:]
        if arguments:
            for folder_name in arguments:
                FileOrganizer(folder_name).execute()
        else:
            FileOrganizer().execute()
    except FileNotFoundError as err:
        sys.exit(f'Error: {err} - No such directory found.')