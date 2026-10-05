import os
import sys
import json
import shutil
class Organize:
    def __init__(self, folder='Downloads'):
        self.folder = self.get_folder_path(folder)
        self.json_data = self.load_json()
    def get_folder_path(self, folder):
        ''' Generate folder path '''
        path = os.path.join('~', folder)
        return os.path.expanduser(path)
    def load_json(self):
        ''' Load json file '''
        with open('extensions.json', 'r') as extension_file:
            return json.load(extension_file)
    def execute(self):
        ''' Execute main flow of program '''
        print(f'\nWorking in directory: {self.folder}\n')
        files = os.listdir(self.folder)
        for file in files:
            name, extension = os.path.splitext(file)
            folder = self.map_folder(extension[1:])
            if folder is not None:
                print(f'{folder.upper()} <--- {file}')
                folder = folder.upper()
                file_path = os.path.join(self.folder, file)
                new_folder = os.path.join(self.folder, folder)
                if not os.path.isdir(new_folder):
                    os.mkdir(new_folder)
                self.move(file_path, new_folder)
        print(f'\nProcess complete.\n')
    def map_folder(self, ext):
        ''' Compare file extensions with extensions present in json file '''
        for folder, extensions in self.json_data.items():
            if ext.lower() in extensions:
                return folder
    def move(self, file_path, folder):
        ''' Move files to a folder '''
        try:
            shutil.move(file_path, folder)
        except shutil.Error as err:
            print(f"Replacing old file >>> {err}")
            shutil.copy(file_path, folder)
            os.remove(file_path)
if __name__ == '__main__':
    arguments = sys.argv
    try:
        if len(arguments) > 1:
            for argument in arguments[1:]:
                Organize(argument).execute()
        else:
            Organize().execute()
    except FileNotFoundError as err:
        sys.exit(f'No such directory found. {err}')