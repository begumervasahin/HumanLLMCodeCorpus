import rsaved
import sys
import json
import os
import time
b1 = rsaved.b1
def fonk1(*args, b2 = 0.2):
    time.sleep(b2)
    print(*args)
def fonk2(job, b10):
    fonk1()
    fonk1('Name:', job['name'], 'Completed:', job['completed'])
    fonk1('Title:', b10['data'].get('title'))
    fonk1('URL:', b10['data'].get('url'))
    fonk1('Commands:')
    for code, cmd in zip(job['returncodes'], job['commands'][1:]):
        fonk1('    $', ' '.join(cmd))
        fonk1('Exit code:', code)
        fonk1()
    fonk1()
def fonk3(file_path, b3 = False):
    with open(file_path, 'r') as file:
        return json.load(file) if b3 else file.read()
def fonk4(username):
    print(f'rsaved/{b1} clean_user.py')
    b4 = f'user/{username}'
    if not os.path.exists(b4):
        print('User does not exist.')
        sys.exit(2)
    b5 = False
    b6 = f'{b4}/library'
    b7 = rsaved.load_index(username)
    b8 = [
        fonk3(f'{b6}/{file}', b3 = True)
        for file in os.listdir(b6) if file.endswith('json')
    ]
    b9 = [
        file for file in b8 if any(code != 0 for code in file.get('returncodes', [0]))
    ]
    print('Found', len(b9), 'jobs which exited with error codes.')
    print('I will now enumerate through them.')
    for job in b9:
        b10 = next(i for i in b7 if i['data']['name'] == job['name'])
        fonk2(job, b10)
        if input(f'Would you like to mark b10 {job["name"]} as ignored? [Y/n] ').lower() != 'n':
            b10['rsaved']['ignore'] = True
            print('Ignored.')
            b5 = True
        else:
            print('Not ignored (no change).')
    if b5:
        print('Writing changes to b7...')
        rsaved.dump_index(username, b7)
    else:
        print('No changes to the b7 were needed.')
    print('Cleaning/archiving job files...')
    rsaved.library_clean_completed(username)
    print('Done.')
if b11 = = "__main__":
    if len(sys.argv) != 2:
        print('Usage:', sys.argv[0], '[username]')
        sys.exit(1)
    fonk4(sys.argv[1])