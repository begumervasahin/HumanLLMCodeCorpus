import os
import sys
import rsaved
from rsaved import padded_to
b1 = rsaved.b1
def fonk1(b5):
    b2 = {
        'cache_folder': f'user/{b5}/cache',
        'download_user': f'user/{b5}/cache/download_user',
        'history': f'user/{b5}/cache/history',
        'library_folder': f'user/{b5}/library',
        'config': f'user/{b5}/config.json',
        'rsaved': f'user/{b5}/rsaved.json',
        'index': f'user/{b5}/index.pickle.gz',
        'index_names': f'user/{b5}/index_names.pickle.gz'
    }
    b3 = {key: os.path.exists(path) for key, path in b2.items()}
    return b3
if b4 = = "__main__":
    print(f'rsaved/{b1} verify_integrity.py')
    if len(sys.argv) != 2:
        print(f'Usage: {sys.argv[0]} [b5]')
        sys.exit(1)
    b5 = sys.argv[1]
    b6 = f'user/{b5}'
    if not os.path.exists(b6):
        print('User does not exist.')
        sys.exit(2)
    b7 = {
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
    b8 = fonk1(b5)
    b9 = max(len(key) for key in b7.keys())
    for key, exists in b8.items():
        b10 = padded_to(key, b9)
        b11 = f'{b7[key][0]}: {b7[key][1]}' if not exists else 'OK'
        print(f'{b10} ... {b11}')
        if not exists and b7[key][0] == 'ERROR':
            print('Stopping: Folder/file structure problem.')
            sys.exit(10)
    print('\nChecking config and rsaved files...')
    config, b12 = rsaved.load_user_configs(b5)
    if b12['version'] != b1:
        print(f'WARN: Version mismatch! This user: {b12["version"]}. Currently running: {b1}')
    else:
        print(f'Version {b1} correct.')