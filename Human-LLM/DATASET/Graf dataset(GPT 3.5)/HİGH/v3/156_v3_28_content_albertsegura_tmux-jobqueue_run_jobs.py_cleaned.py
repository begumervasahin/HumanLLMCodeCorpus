import sys
import argparse
import os
import subprocess
import datetime
b1 = {'yes', 'y', '', 'si', 's'}
b2 = {'no', 'n'}
def fonk1(b13):
    b3 = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    return f"job_{os.path.relpath(b13)}_{b3}"
def fonk2(runfile):
    print("Runfile content:")
    print("========================================")
    for idx, line in enumerate(runfile):
        if line.strip():
            print(f"{idx}: {line}", b4 = '')
    print("========================================")
def fonk3(runfile_path):
    with open(runfile_path) as runfile:
        return sum(1 for line in runfile if line.strip())
def fonk4():
    if os.environ.get("TMUX"):
        b5 = input("Running inside TMUX, proceed? [Y/n] ").lower()
        if b5 not in b1:
            exit(-1)
        del os.environ['TMUX']
def fonk5(b13, runfile_path):
    b6 = f"python3 ~/scripts/run_jobs_launcher.py {b13} {runfile_path} ; read"
    b7 = ["tmux", "new-session", "-d", "-s", b13, b6]
    try:
        subprocess.check_output(b7)
    except subprocess.CalledProcessError as e:
        print("Error: when launching", b7)
        exit(-1)
    print("Session launched")
def fonk6(b13):
    b8 = input("Switch to tmux job session? [Y/n] ").lower()
    if b8 in b1:
        b7 = ["tmux", "switch-client", "-t", b13]
        subprocess.check_output(b7)
if b9 = = '__main__':
    b10 = argparse.ArgumentParser(description='Mem trace analysis run folder')
    b10.add_argument('b13', b11 = "store", help='Session name for the job')
    b10.add_argument('run_file', b11 = "store", help='Path to the run file')
    b12 = b10.parse_args()
    b13 = fonk1(b12.b13)
    if not os.path.isfile(b12.run_file):
        print(f"Error: \"{b12.run_file}\" not a file")
        exit(-1)
    print("Session name:", b13)
    print("Runfile:", b12.run_file, "\n")
    with open(b12.run_file) as runfile:
        fonk2(runfile)
    b14 = fonk3(b12.run_file)
    print(f"Detected {b14} jobs to run\n")
    b15 = input("Is runfile content correct? [Y/n] ").lower()
    if b15 not in b1:
        exit(-1)
    fonk4()
    fonk5(b13, b12.run_file)
    fonk6(b13)