import os
import sys
import json
import shutil
class Organize:
    def __init__(self, folder='Downloads'):
        self.folder = self.get_folder_path(folder)
        self.extensions = self.load_extensions()
    def get_folder_path(self, folder):
        ''' Generate folder path '''
        path = os.path.join('~', folder)
        return os.path.expanduser(path)
    def load_extensions(self):
        ''' Load extensions from JSON file '''
        with open('extensions.json', 'r') as extension_file:
            return json.load(extension_file)
    def execute(self):
        ''' Execute main flow of program '''
        print(f'\nWorking in directory: {self.folder}\n')
        files = os.listdir(self.folder)
        for file in files:
            name, extension = os.path.splitext(file)
            folder = self.map_folder(extension[1:])
            if folder:
                print(f'{folder.upper()} <--- {file}')
                self.move(file, folder)
        print(f'\nProcess complete.\n')
    def map_folder(self, ext):
        ''' Compare file extensions with extensions present in JSON file '''
        for folder, extensions in self.extensions.items():
            if ext.lower() in extensions:
                return folder
    def move(self, file, folder):
        ''' Move files to corresponding folder '''
        folder_path = os.path.join(self.folder, folder.upper())
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        try:
            src_path = os.path.join(self.folder, file)
            dst_path = os.path.join(folder_path, file)
            shutil.move(src_path, dst_path)
        except shutil.Error as err:
            print(f"Replacing old file >>> {err}")
            shutil.copy(src_path, folder_path)
            os.remove(src_path)
if __name__ == '__main__':
    arguments = sys.argv[1:]
    try:
        if arguments:
            for argument in arguments:
                Organize(argument).execute()
        else:
            Organize().execute()
    except FileNotFoundError as err:
        sys.exit(f'No such directory found: {err}')