import rsaved
import sys
import json
import os
import time
__version__ = rsaved.__version__
def sprint(*args, delay=0.2):
    time.sleep(delay)
    print(*args)
def print_job(job, item):
    sprint()
    sprint('Name:', job['name'], 'Completed:', job['completed'])
    sprint('Title:', item['data'].get('title'))
    sprint('URL:', item['data'].get('url'))
    sprint('Commands:')
    for code, cmd in zip(job['returncodes'], job['commands'][1:]):
        sprint('    $', ' '.join(cmd))
        sprint('Exit code:', code)
        sprint()
    sprint()
def load_file(fname, json_load=False):
    with open(fname, 'r') as f:
        return json.load(f) if json_load else f.read()
if __name__ == "__main__":
    print(f'rsaved/{__version__} clean_user.py')
    if len(sys.argv) != 2:
        print('Usage:', sys.argv[0], '[username]')
        sys.exit(1)
    username = sys.argv[1]
    user_folder = f'user/{username}'
    if not os.path.exists(user_folder):
        print('User does not exist.')
        sys.exit(2)
    changes_made = False
    library_folder = f'{user_folder}/library'
    index = rsaved.load_index(username)
    json_files = [load_file(f'{library_folder}/{file}', True) for file in os.listdir(library_folder) if file.endswith('json')]
    errored_jobs = [file for file in json_files if any(code != 0 for code in file.get('returncodes', [0]))]
    print('Found', len(errored_jobs), 'jobs which exited with error codes.')
    print('I will now enumerate through them.')
    for job in errored_jobs:
        item = next(i for i in index if i['data']['name'] == job['name'])
        print_job(job, item)
        if input(f'Would you like to mark item {job["name"]} as ignored? [Y/n] ').lower() != 'n':
            item['rsaved']['ignore'] = True
            print('Ignored.')
            changes_made = True
        else:
            print('Not ignored (no change).')
    if changes_made:
        print('Writing changes to index...')
        rsaved.dump_index(username, index)
    else:
        print('No changes to the index were needed.')
    print('Cleaning/archiving job files...')
    rsaved.library_clean_completed(username)
    print('Done.')