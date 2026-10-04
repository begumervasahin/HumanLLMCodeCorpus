import sys
import argparse
import os
import subprocess
import datetime
b1 = {'yes', 'y', '', 'si', 's'}
b2 = {'no', 'n'}
def fonk1():
    b3 = argparse.ArgumentParser(description='Mem trace analysis run folder')
    b3.add_argument('b13', b4 = 'Session name for the tmux session')
    b3.add_argument('run_file', b4 = 'File containing the list of jobs to run')
    return b3.parse_args()
def fonk2(run_file):
    if not os.path.isfile(run_file):
        print(f'Error: "{run_file}" not a file')
        sys.exit(-1)
def fonk3(b13):
    return f"job_{os.path.relpath(b13)}_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"
def fonk4(run_file):
    print("\nRunfile content:")
    print("========================================")
    with open(run_file) as f:
        b5 = f.readlines()
        for idx, line in enumerate(b5):
            print(f"{idx}: {line}", b6 = '')
    print("========================================")
    print(f"Detected {len(b5)} jobs to run\n")
    return b5
def fonk5():
    b7 = input("Is runfile content correct? [Y/n] ").lower()
    if b7 not in b1:
        sys.exit(-1)
def fonk6():
    if "TMUX" in os.environ:
        b8 = input("Running inside TMUX, proceed? [Y/n] ").lower()
        if b8 not in b1:
            sys.exit(-1)
        del os.environ['TMUX']
def fonk7(b13):
    try:
        subprocess.check_output(["tmux", "has-session", "-t", b13], b9 = subprocess.STDOUT)
        return True
    except subprocess.CalledProcessError:
        return False
def fonk8(b13, run_file):
    try:
        b10 = f"python3 ~/scripts/run_jobs_launcher.py {b13} {run_file} ; read"
        subprocess.check_output(["tmux", "new-session", "-d", "-s", b13, b10])
    except subprocess.CalledProcessError:
        print("Error: when launching tmux session")
        sys.exit(-1)
    print("Session launched")
def fonk9(b13):
    b11 = input("Switch to tmux job session? [Y/n] ").lower()
    if b11 in b1:
        subprocess.check_output(["tmux", "switch-client", "-t", b13])
def fonk10():
    b12 = fonk1()
    fonk2(b12.run_file)
    b13 = fonk3(b12.b13)
    print("Session name:", b13)
    print("Runfile:", b12.run_file)
    b5 = fonk4(b12.run_file)
    fonk5()
    fonk6()
    if fonk7(b13):
        print(f"Error: session {b13} already exists")
        sys.exit(-1)
    fonk8(b13, b12.run_file)
    fonk9(b13)
if b14 = = '__main__':
    fonk10()