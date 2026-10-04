import os
import sys
import rsaved
from rsaved import padded_to, load_user_configs
__version__ = rsaved.__version__
def check_files(username):
    status = {
        'cache_folder': os.path.exists(f'user/{username}/cache') and os.path.exists(f'user/{username}/cache/download_user') and os.path.exists(f'user/{username}/cache/history'),
        'library_folder': os.path.exists(f'user/{username}/library'),
        'config': os.path.exists(f'user/{username}/config.json'),
        'rsaved': os.path.exists(f'user/{username}/rsaved.json'),
        'index': os.path.exists(f'user/{username}/index.pickle.gz'),
        'index_names': os.path.exists(f'user/{username}/index_names.pickle.gz')
    }
    return status
if __name__ == "__main__":
    print(f'rsaved/{__version__} verify_integrity.py')
    if len(sys.argv) != 2:
        print('Usage:', sys.argv[0], '[username]')
        sys.exit(1)
    username = sys.argv[1]
    if not os.path.exists(f'user/{username}'):
        print('User does not exist.')
        sys.exit(2)
    errors = {
        'cache_folder': ('ERROR', 'Cache folders are missing!'),
        'library_folder': ('ERROR', 'Library folder is missing!'),
        'config': ('ERROR', 'config.json file is missing!'),
        'rsaved': ('ERROR', 'rsaved.json file is missing!'),
        'index': ('WARN', 'index.pickle.gz is missing. Did you run download_user.py?'),
        'index_names': ('WARN', 'index_names.pickle.gz is missing. Did you run download_user.py?'),
    }
    print('Checking folder/file structure...')
    files_status = check_files(username)
    for key, stat in files_status.items():
        print(padded_to(key, max(len(i) for i in errors.keys())), '...', f'{errors[key][0]}: {errors[key][1]}' if not stat else 'OK')
        if not stat and errors[key][0] == 'ERROR':
            print('Stopping: Folder/file structure problem.')
            sys.exit(10)
    print()
    print('Checking config and rsaved files...')
    config, rs = load_user_configs(username)
    if rs['version'] != __version__:
        print(f'WARN: Version mismatch! This user: {rs["version"]}. Currently running: {__version__}')
    else:
        print('Version', __version__, 'correct.')