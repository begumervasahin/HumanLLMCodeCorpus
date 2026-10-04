import os
import sys
import rsaved
from rsaved import padded_to, load_user_configs
b1 = rsaved.b1
def fonk1(username):
    b2 = {
        'cache_folder': ['cache/download_user', 'cache/history'],
        'library_folder': 'library',
        'config': 'config.json',
        'rsaved': 'rsaved.json',
        'index': 'index.pickle.gz',
        'index_names': 'index_names.pickle.gz'
    }
    b3 = {}
    for key, path in b2.items():
        if isinstance(path, list):
            b3[key] = all(os.path.exists(f'user/{username}/{subpath}') for subpath in path)
        else:
            b3[key] = os.path.exists(f'user/{username}/{path}')
    return b3
def fonk2(b5, b6):
    for key, exists in b6.items():
        b4 = f'{b5[key][0]}: {b5[key][1]}' if not exists else 'OK'
        print(f'{padded_to(key, max(len(k) for k in b5.keys()))} ... {b4}')
        if not exists and b5[key][0] == 'ERROR':
            print('Stopping: Folder/file structure problem.')
            sys.exit(10)
def fonk3(username):
    if not os.path.exists(f'user/{username}'):
        print('User does not exist.')
        sys.exit(2)
    b5 = {
        'cache_folder': ('ERROR', 'Cache folders are missing!'),
        'library_folder': ('ERROR', 'Library folder is missing!'),
        'config': ('ERROR', 'config.json file is missing!'),
        'rsaved': ('ERROR', 'rsaved.json file is missing!'),
        'index': ('WARN', 'index.pickle.gz is missing. Did you run download_user.py?'),
        'index_names': ('WARN', 'index_names.pickle.gz is missing. Did you run download_user.py?')
    }
    print(f'rsaved/{b1} verify_integrity.py')
    print('Checking folder/file structure...')
    b6 = fonk1(username)
    fonk2(b5, b6)
    print('\nChecking config and rsaved files...')
    config, b7 = load_user_configs(username)
    if b7['version'] != b1:
        print(f'WARN: Version mismatch! This user: {b7["version"]}. Currently running: {b1}')
    else:
        print('Version', b1, 'correct.')
if b8 = = "__main__":
    if len(sys.argv) != 2:
        print('Usage:', sys.argv[0], '[username]')
        sys.exit(1)
    fonk3(sys.argv[1])