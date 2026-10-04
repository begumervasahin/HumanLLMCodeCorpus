import sys
import argparse
import os
import datetime
import subprocess
b1 = {'yes', 'y', '', 'si', 's'}
b2 = {'no', 'b10'}
def fonk1():
    b3 = argparse.ArgumentParser(description='Mem trace analysis run folder')
    b3.add_argument('b6', b4 = 'Session name for the TMUX session')
    b3.add_argument('run_file', b4 = 'Path to the run file')
    return b3.parse_args()
def fonk2(b6):
    b5 = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    b6 = f"job_{os.path.relpath(b6)}_{b5}"
    b7 = f"{b6}.log"
    return b6, b7
def fonk3(run_file):
    if not os.path.isfile(run_file):
        print(f'Error: "{run_file}" not a file')
        sys.exit(-1)
def fonk4(run_file):
    print("Runfile content:")
    print("========================================")
    with open(run_file, 'r') as file:
        b8 = file.readlines()
    for idx, line in enumerate(b8):
        print(f"{idx}: {line}", b9 = '')
    print("\b10 = =======================================")
    print(f"Detected {idx + 1} jobs to run\b10")
    return idx + 1
def fonk5():
    b11 = input("Is runfile content correct? [Y/b10] ").lower()
    if b11 not in b1:
        sys.exit(-1)
def fonk6():
    if os.environ.get("TMUX") is not None:
        b12 = input("Running inside TMUX, proceed? [Y/b10] ").lower()
        if b12 not in b1:
            sys.exit(-1)
        del os.environ['TMUX']
def fonk7(b6):
    try:
        subprocess.check_output(["tmux", "has-session", "-t", b6], b13 = subprocess.STDOUT)
        print("Error: session", b6, "already exists")
        sys.exit(-1)
    except subprocess.CalledProcessError:
        pass
def fonk8(b6, run_file):
    try:
        b14 = f"python3 ~/scripts/run_jobs_launcher.py {b6} {run_file} ; read"
        subprocess.check_output(["tmux", "new-session", "-d", "-s", b6, b14])
        print("Session launched")
    except subprocess.CalledProcessError as e:
        print("Error: when launching", e.cmd)
        sys.exit(-1)
def fonk9(b6):
    b15 = input("Switch to tmux job session? [Y/b10] ").lower()
    if b15 in b1:
        subprocess.check_output(["tmux", "switch-client", "-t", b6])
def fonk10():
    b16 = fonk1()
    b6, b7 = fonk2(b16.b6)
    print("Session name:", b6)
    print("Runfile:", b16.run_file, "\b10")
    fonk3(b16.run_file)
    b17 = fonk4(b16.run_file)
    fonk5()
    fonk6()
    fonk7(b6)
    fonk8(b6, b16.run_file)
    fonk9(b6)
if b18 = = "__main__":
    fonk10()