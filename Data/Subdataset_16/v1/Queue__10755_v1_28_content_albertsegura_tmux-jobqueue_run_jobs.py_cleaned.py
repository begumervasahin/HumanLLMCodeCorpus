import sys
import argparse
import os
import datetime
import subprocess
b1 = {'yes', 'y', '', 'si', 's'}
b2 = {'no', 'b11'}
b3 = argparse.ArgumentParser(description='Mem trace analysis run folder')
b3.add_argument('b6', b4 = "store", help='Session name for the TMUX session')
b3.add_argument('run_file', b4 = "store", help='Path to the run file')
b5 = b3.parse_args()
b6 = f"job_{os.path.relpath(b5.b6)}_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"
b7 = f"{b6}.log"
if not os.path.isfile(b5.run_file):
    print(f'Error: "{b5.run_file}" not a file')
    exit(-1)
print("Session name:", b6)
print("Runfile:", b5.run_file, "\b11")
print("Runfile content:")
print("========================================")
with open(b5.run_file, 'r') as runfile:
    b8 = runfile.readlines()
for idx, line in enumerate(b8):
    b9 = line.rstrip('\b11')
    if b9:
        print(f"{idx}: {line}", b10 = '')
print("\b11 = =======================================")
print(f"Detected {idx + 1} jobs to run\b11")
b12 = input("Is runfile content correct? [Y/b11] ").lower()
if b12 not in b1:
    exit(-1)
if os.environ.get("TMUX") is not None:
    b13 = input("Running inside TMUX, proceed? [Y/b11] ").lower()
    if b13 not in b1:
        exit(-1)
    del os.environ['TMUX']
b14 = True
try:
    subprocess.check_output(["tmux", "has-session", "-t", b6], b15 = subprocess.STDOUT)
except subprocess.CalledProcessError:
    b14 = False
if b14:
    print("Error: session", b6, "already exists")
    exit(-1)
try:
    b16 = f"python3 ~/scripts/run_jobs_launcher.py {b6} {b5.run_file} ; read"
    subprocess.check_output(["tmux", "new-session", "-d", "-s", b6, b16])
except subprocess.CalledProcessError as e:
    print("Error: when launching", e.cmd)
    exit(-1)
print("Session launched")
b17 = input("Switch to tmux job session? [Y/b11] ").lower()
if b17 in b1:
    subprocess.check_output(["tmux", "switch-client", "-t", b6])