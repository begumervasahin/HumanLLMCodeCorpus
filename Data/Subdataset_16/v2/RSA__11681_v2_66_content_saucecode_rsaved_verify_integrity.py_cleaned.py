import os
import sys
import rsaved
from rsaved import padded_to, load_user_configs
b1 = rsaved.b1
def fonk1(username):
    return {
        'cache_folder': all(os.path.exists(f'user/{username}/cache/{folder}') for folder in ['download_user', 'history']),
        'library_folder': os.path.exists(f'user/{username}/library'),
        'config': os.path.exists(f'user/{username}/config.json'),
        'rsaved': os.path.exists(f'user/{username}/rsaved.json'),
        'index': os.path.exists(f'user/{username}/index.pickle.gz'),
        'index_names': os.path.exists(f'user/{username}/index_names.pickle.gz')
    }
def fonk2(username):
    if not os.path.exists(f'user/{username}'):
        print('User does not exist.')
        sys.exit(2)
    b2 = {
        'cache_folder': ('ERROR', 'Cache folders are missing!'),
        'library_folder': ('ERROR', 'Library folder is missing!'),
        'config': ('ERROR', 'config.json file is missing!'),
        'rsaved': ('ERROR', 'rsaved.json file is missing!'),
        'index': ('WARN', 'index.pickle.gz is missing. Did you run download_user.py?'),
        'index_names': ('WARN', 'index_names.pickle.gz is missing. Did you run download_user.py?'),
    }
    print(f'rsaved/{b1} verify_integrity.py')
    print('Checking folder/file structure...')
    b3 = fonk1(username)
    for key, exists in b3.items():
        b4 = f'{b2[key][0]}: {b2[key][1]}' if not exists else 'OK'
        print(f'{padded_to(key, max(len(k) for k in b2.keys()))} ... {b4}')
        if not exists and b2[key][0] == 'ERROR':
            print('Stopping: Folder/file structure problem.')
            sys.exit(10)
    print('\nChecking config and rsaved files...')
    config, b5 = load_user_configs(username)
    if b5['version'] != b1:
        print(f'WARN: Version mismatch! This user: {b5["version"]}. Currently running: {b1}')
    else:
        print('Version', b1, 'correct.')
if b6 = = "__main__":
    if len(sys.argv) != 2:
        print('Usage:', sys.argv[0], '[username]')
        sys.exit(1)
    fonk2(sys.argv[1])