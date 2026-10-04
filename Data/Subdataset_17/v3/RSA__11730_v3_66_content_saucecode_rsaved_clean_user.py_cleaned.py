import os
import sys
import json
import time
import pickle
import rsaved
__version__ = rsaved.__version__
def print_job_details(job, item):
    def delayed_print(*args):
        time.sleep(0.2)
        print(*args)
    delayed_print()
    delayed_print('Name:', job['name'], 'Completed:', job['completed'])
    delayed_print('Title:', item['data'].get('title'))
    delayed_print('URL:', item['data'].get('url'))
    delayed_print('Commands:')
    for code, cmd in zip(job['returncodes'], job['commands'][1:]):
        delayed_print('    $', ' '.join(cmd))
        delayed_print('Exit code:', code)
        delayed_print()
    delayed_print()
def load_file_contents(filename, parse_as_json=False):
    with open(filename, 'r') as file:
        return json.load(file) if parse_as_json else file.read()
def enumerate_errored_jobs(username, index, errored_jobs):
    changes_made = False
    for job in errored_jobs:
        item = next((i for i in index if i['data']['name'] == job['name']), None)
        if item is None:
            continue
        print_job_details(job, item)
        user_input = input(f'Would you like to mark item {job["name"]} as ignored? [Y/n] ').lower()
        if user_input != 'n':
            item['rsaved']['ignore'] = True
            print('Ignored.')
            changes_made = True
        else:
            print('Not ignored (no change).')
    return changes_made
def main():
    print(f'rsaved/{__version__} clean_user.py')
    if len(sys.argv) != 2:
        print(f'Usage: {sys.argv[0]} [username]')
        sys.exit(1)
    username = sys.argv[1]
    user_folder = f'user/{username}'
    library_folder = f'{user_folder}/library'
    if not os.path.exists(user_folder):
        print('User does not exist.')
        sys.exit(2)
    index = rsaved.load_index(username)
    json_files = [
        load_file_contents(f'{library_folder}/{file}', parse_as_json=True)
        for file in os.listdir(library_folder) if file.endswith('json')
    ]
    errored_jobs = [
        file for file in json_files if any(code != 0 for code in file.get('returncodes', [0]))
    ]
    print(f'Found {len(errored_jobs)} jobs which exited with error codes.')
    print('I will now enumerate through them.')
    changes_made = enumerate_errored_jobs(username, index, errored_jobs)
    if changes_made:
        print('Writing changes to index...')
        rsaved.dump_index(username, index)
    else:
        print('No changes to the index were needed.')
    print('Cleaning/archiving job files...')
    rsaved.library_clean_completed(username)
    print('Done.')
if __name__ == "__main__":
    main()