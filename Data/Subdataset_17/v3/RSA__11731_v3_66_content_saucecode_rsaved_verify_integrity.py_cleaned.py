import os
import sys
import rsaved
from rsaved import padded_to, load_user_configs
__version__ = rsaved.__version__
def check_files(username):
    required_files = {
        'cache_folder': ['cache/download_user', 'cache/history'],
        'library_folder': 'library',
        'config': 'config.json',
        'rsaved': 'rsaved.json',
        'index': 'index.pickle.gz',
        'index_names': 'index_names.pickle.gz'
    }
    status = {}
    for key, path in required_files.items():
        if isinstance(path, list):
            status[key] = all(os.path.exists(f'user/{username}/{subpath}') for subpath in path)
        else:
            status[key] = os.path.exists(f'user/{username}/{path}')
    return status
def print_status(errors, files_status):
    for key, exists in files_status.items():
        status_message = f'{errors[key][0]}: {errors[key][1]}' if not exists else 'OK'
        print(f'{padded_to(key, max(len(k) for k in errors.keys()))} ... {status_message}')
        if not exists and errors[key][0] == 'ERROR':
            print('Stopping: Folder/file structure problem.')
            sys.exit(10)
def main(username):
    if not os.path.exists(f'user/{username}'):
        print('User does not exist.')
        sys.exit(2)
    errors = {
        'cache_folder': ('ERROR', 'Cache folders are missing!'),
        'library_folder': ('ERROR', 'Library folder is missing!'),
        'config': ('ERROR', 'config.json file is missing!'),
        'rsaved': ('ERROR', 'rsaved.json file is missing!'),
        'index': ('WARN', 'index.pickle.gz is missing. Did you run download_user.py?'),
        'index_names': ('WARN', 'index_names.pickle.gz is missing. Did you run download_user.py?')
    }
    print(f'rsaved/{__version__} verify_integrity.py')
    print('Checking folder/file structure...')
    files_status = check_files(username)
    print_status(errors, files_status)
    print('\nChecking config and rsaved files...')
    config, rs = load_user_configs(username)
    if rs['version'] != __version__:
        print(f'WARN: Version mismatch! This user: {rs["version"]}. Currently running: {__version__}')
    else:
        print('Version', __version__, 'correct.')
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage:', sys.argv[0], '[username]')
        sys.exit(1)
    main(sys.argv[1])