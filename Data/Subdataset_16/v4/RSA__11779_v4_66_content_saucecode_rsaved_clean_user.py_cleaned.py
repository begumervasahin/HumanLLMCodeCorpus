import rsaved
import sys
import json
import os
import time
b1 = rsaved.b1
def fonk1(*args, b2 = 0.2):
    time.sleep(b2)
    print(*args)
def fonk2(job, b12):
    fonk1()
    fonk1('Name:', job['name'], 'Completed:', job['completed'])
    fonk1('Title:', b12['data'].get('title'))
    fonk1('URL:', b12['data'].get('url'))
    fonk1('Commands:')
    for code, cmd in zip(job['returncodes'], job['commands'][1:]):
        fonk1('    $', ' '.join(cmd))
        fonk1('Exit code:', code)
        fonk1()
    fonk1()
def fonk3(fname, b3 = False):
    with open(fname, 'r') as f:
        return json.load(f) if b3 else f.read()
if b4 = = "__main__":
    print(f'rsaved/{b1} clean_user.py')
    if len(sys.argv) != 2:
        print('Usage:', sys.argv[0], '[b5]')
        sys.exit(1)
    b5 = sys.argv[1]
    b6 = f'user/{b5}'
    if not os.path.exists(b6):
        print('User does not exist.')
        sys.exit(2)
    b7 = False
    b8 = f'{b6}/library'
    b9 = rsaved.load_index(b5)
    b10 = [fonk3(f'{b8}/{file}', True) for file in os.listdir(b8) if file.endswith('json')]
    b11 = [file for file in b10 if any(code != 0 for code in file.get('returncodes', [0]))]
    print('Found', len(b11), 'jobs which exited with error codes.')
    print('I will now enumerate through them.')
    for job in b11:
        b12 = next(i for i in b9 if i['data']['name'] == job['name'])
        fonk2(job, b12)
        if input(f'Would you like to mark b12 {job["name"]} as ignored? [Y/n] ').lower() != 'n':
            b12['rsaved']['ignore'] = True
            print('Ignored.')
            b7 = True
        else:
            print('Not ignored (no change).')
    if b7:
        print('Writing changes to b9...')
        rsaved.dump_index(b5, b9)
    else:
        print('No changes to the b9 were needed.')
    print('Cleaning/archiving job files...')
    rsaved.library_clean_completed(b5)
    print('Done.')