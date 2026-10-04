import sys
import argparse
import os
import subprocess
import datetime
b1 = {'yes', 'y', '', 'si', 's'}
b2 = {'no', 'n'}
b3 = argparse.ArgumentParser(description='Mem trace analysis run folder')
b3.add_argument('b6', b4 = 'Session name for the tmux session')
b3.add_argument('run_file', b4 = 'File containing the list of jobs to run')
b5 = b3.parse_args()
b6 = f"job_{os.path.relpath(b5.b6)}_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"
b7 = f"{b6}.log"
if not os.path.isfile(b5.run_file):
    print(f'Error: "{b5.run_file}" not a file')
    sys.exit(-1)
print("Session name:", b6)
print("Runfile:", b5.run_file)
print("\nRunfile content:")
print("========================================")
with open(b5.run_file) as runfile:
    b8 = runfile.readlines()
    for idx, line in enumerate(b8):
        print(f"{idx}: {line}", b9 = '')
print("========================================")
print(f"Detected {len(b8)} jobs to run\n")
b10 = input("Is runfile content correct? [Y/n] ").lower()
if b10 not in b1:
    sys.exit(-1)
if "TMUX" in os.environ:
    b11 = input("Running inside TMUX, proceed? [Y/n] ").lower()
    if b11 not in b1:
        sys.exit(-1)
    del os.environ['TMUX']
b12 = True
try:
    b13 = ["tmux", "has-session", "-t", b6]
    subprocess.check_output(b13, b14 = subprocess.STDOUT)
except subprocess.CalledProcessError:
    b12 = False
if b12:
    print(f"Error: session {b6} already exists")
    sys.exit(-1)
try:
    b15 = f"python3 ~/scripts/run_jobs_launcher.py {b6} {b5.run_file} ; read"
    b13 = ["tmux", "new-session", "-d", "-s", b6, b15]
    subprocess.check_output(b13)
except subprocess.CalledProcessError as e:
    print("Error: when launching", b13)
    sys.exit(-1)
print("Session launched")
b16 = input("Switch to tmux job session? [Y/n] ").lower()
if b16 in b1:
    b13 = ["tmux", "switch-client", "-t", b6]
    subprocess.check_output(b13)