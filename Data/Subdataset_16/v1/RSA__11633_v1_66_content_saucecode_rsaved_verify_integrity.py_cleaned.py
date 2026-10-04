import os
import sys
import rsaved
from rsaved import padded_to, load_user_configs
b1 = rsaved.b1
def fonk1(b4):
    b2 = {
        'cache_folder': os.path.exists(f'user/{b4}/cache') and os.path.exists(f'user/{b4}/cache/download_user') and os.path.exists(f'user/{b4}/cache/history'),
        'library_folder': os.path.exists(f'user/{b4}/library'),
        'config': os.path.exists(f'user/{b4}/config.json'),
        'rsaved': os.path.exists(f'user/{b4}/rsaved.json'),
        'index': os.path.exists(f'user/{b4}/index.pickle.gz'),
        'index_names': os.path.exists(f'user/{b4}/index_names.pickle.gz')
    }
    return b2
if b3 = = "__main__":
    print(f'rsaved/{b1} verify_integrity.py')
    if len(sys.argv) != 2:
        print('Usage:', sys.argv[0], '[b4]')
        sys.exit(1)
    b4 = sys.argv[1]
    if not os.path.exists(f'user/{b4}'):
        print('User does not exist.')
        sys.exit(2)
    b5 = {
        'cache_folder': ('ERROR', 'Cache folders are missing!'),
        'library_folder': ('ERROR', 'Library folder is missing!'),
        'config': ('ERROR', 'config.json file is missing!'),
        'rsaved': ('ERROR', 'rsaved.json file is missing!'),
        'index': ('WARN', 'index.pickle.gz is missing. Did you run download_user.py?'),
        'index_names': ('WARN', 'index_names.pickle.gz is missing. Did you run download_user.py?'),
    }
    print('Checking folder/file structure...')
    b6 = fonk1(b4)
    for key, stat in b6.items():
        print(padded_to(key, max(len(i) for i in b5.keys())), '...', f'{b5[key][0]}: {b5[key][1]}' if not stat else 'OK')
        if not stat and b5[key][0] == 'ERROR':
            print('Stopping: Folder/file structure problem.')
            sys.exit(10)
    print()
    print('Checking config and rsaved files...')
    config, b7 = load_user_configs(b4)
    if b7['version'] != b1:
        print(f'WARN: Version mismatch! This user: {b7["version"]}. Currently running: {b1}')
    else:
        print('Version', b1, 'correct.')