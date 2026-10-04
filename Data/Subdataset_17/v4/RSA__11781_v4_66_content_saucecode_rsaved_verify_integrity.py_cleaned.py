import os
import sys
import rsaved
from rsaved import padded_to
__version__ = rsaved.__version__
def check_files(username):
    paths = {
        'cache_folder': f'user/{username}/cache',
        'download_user': f'user/{username}/cache/download_user',
        'history': f'user/{username}/cache/history',
        'library_folder': f'user/{username}/library',
        'config': f'user/{username}/config.json',
        'rsaved': f'user/{username}/rsaved.json',
        'index': f'user/{username}/index.pickle.gz',
        'index_names': f'user/{username}/index_names.pickle.gz'
    }
    status = {key: os.path.exists(path) for key, path in paths.items()}
    return status
if __name__ == "__main__":
    print(f'rsaved/{__version__} verify_integrity.py')
    if len(sys.argv) != 2:
        print(f'Usage: {sys.argv[0]} [username]')
        sys.exit(1)
    username = sys.argv[1]
    user_path = f'user/{username}'
    if not os.path.exists(user_path):
        print('User does not exist.')
        sys.exit(2)
    error_messages = {
        'cache_folder': ('ERROR', 'Cache folders are missing!'),
        'download_user': ('ERROR', 'Download user folder is missing!'),
        'history': ('ERROR', 'History folder is missing!'),
        'library_folder': ('ERROR', 'Library folder is missing!'),
        'config': ('ERROR', 'config.json file is missing!'),
        'rsaved': ('ERROR', 'rsaved.json file is missing!'),
        'index': ('WARN', 'index.pickle.gz is missing. Did you run download_user.py?'),
        'index_names': ('WARN', 'index_names.pickle.gz is missing. Did you run download_user.py?')
    }
    print('Checking folder/file structure...')
    files_status = check_files(username)
    max_key_length = max(len(key) for key in error_messages.keys())
    for key, exists in files_status.items():
        padded_key = padded_to(key, max_key_length)
        status_msg = f'{error_messages[key][0]}: {error_messages[key][1]}' if not exists else 'OK'
        print(f'{padded_key} ... {status_msg}')
        if not exists and error_messages[key][0] == 'ERROR':
            print('Stopping: Folder/file structure problem.')
            sys.exit(10)
    print('\nChecking config and rsaved files...')
    config, rs = rsaved.load_user_configs(username)
    if rs['version'] != __version__:
        print(f'WARN: Version mismatch! This user: {rs["version"]}. Currently running: {__version__}')
    else:
        print(f'Version {__version__} correct.')