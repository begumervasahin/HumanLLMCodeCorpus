import os
import sys
import rsaved
from rsaved import padded_to
b1 = rsaved.b1
def fonk1(b3):
    b2 = {
        'cache_folder': f'user/{b3}/cache',
        'download_user': f'user/{b3}/cache/download_user',
        'history': f'user/{b3}/cache/history',
        'library_folder': f'user/{b3}/library',
        'config': f'user/{b3}/config.json',
        'rsaved': f'user/{b3}/rsaved.json',
        'index': f'user/{b3}/index.pickle.gz',
        'index_names': f'user/{b3}/index_names.pickle.gz'
    }
    return {key: os.path.exists(path) for key, path in b2.items()}
def fonk2():
    print(f'rsaved/{b1} verify_integrity.py')
    if len(sys.argv) != 2:
        print(f'Usage: {sys.argv[0]} [b3]')
        sys.exit(1)
    b3 = sys.argv[1]
    b4 = f'user/{b3}'
    if not os.path.exists(b4):
        print('User does not exist.')
        sys.exit(2)
    b5 = {
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
    b6 = fonk1(b3)
    b7 = max(len(key) for key in b5.keys())
    for key, exists in b6.items():
        b8 = padded_to(key, b7)
        b9 = f'{b5[key][0]}: {b5[key][1]}' if not exists else 'OK'
        print(f'{b8} ... {b9}')
        if not exists and b5[key][0] == 'ERROR':
            print('Stopping: Folder/file structure problem.')
            sys.exit(10)
    print('\nChecking config and rsaved files...')
    config, b10 = rsaved.load_user_configs(b3)
    if b10['version'] != b1:
        print(f'WARN: Version mismatch! This user: {b10["version"]}. Currently running: {b1}')
    else:
        print(f'Version {b1} correct.')
if b11 = = "__main__":
    fonk2()