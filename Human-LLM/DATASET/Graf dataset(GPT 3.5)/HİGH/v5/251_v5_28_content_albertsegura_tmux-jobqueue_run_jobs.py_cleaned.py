import sys
import argparse
import os
import subprocess
import datetime
b1 = {'yes', 'y', '', 'si', 's'}
b2 = {'no', 'n'}
def fonk1():
    b3 = argparse.ArgumentParser(description='Mem trace analysis run folder')
    b3.add_argument('b13', b4 = "store", help='Session name')
    b3.add_argument('run_file', b4 = "store", help='Path to the run file')
    return b3.parse_args()
def fonk2(b13):
    b5 = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    return f"job_{os.path.relpath(b13)}_{b5}"
def fonk3(run_file):
    print("Runfile content:")
    print("========================================")
    with open(run_file) as file:
        for idx, line in enumerate(file):
            b6 = line.rstrip('\n')
            if b6 != "":
                print(f"{idx}: {b6}")
    print("========================================")
    return idx
def fonk4():
    b7 = input("Is runfile content correct? [Y/n] ").lower()
    return b7 in b1
def fonk5():
    if os.environ.copy().get("TMUX") is not None:
        b8 = input("Running inside TMUX, proceed? [Y/n] ").lower()
        if b8 not in b1:
            exit(-1)
        del os.environ['TMUX']
def fonk6(b13, runfile):
    b9 = f"python3 ~/scripts/run_jobs_launcher.py {b13} {runfile} ; read"
    b10 = ["tmux", "new-session", "-d", "-s", b13, b9]
    try:
        subprocess.check_output(b10)
        print("Session launched")
    except subprocess.CalledProcessError:
        print("Error: failed to launch TMUX session")
        exit(-1)
def fonk7(b13):
    b11 = input("Switch to tmux job session? [Y/n] ").lower()
    if b11 in b1:
        b10 = ["tmux", "switch-client", "-t", b13]
        try:
            subprocess.check_output(b10)
        except subprocess.CalledProcessError:
            print("Error: failed to switch to TMUX job session")
def fonk8():
    b12 = fonk1()
    b13 = fonk2(b12.b13)
    print("Session name:", b13)
    print("Runfile:", b12.run_file, "\n")
    b14 = fonk3(b12.run_file)
    if not fonk4():
        exit(-1)
    fonk5()
    if os.path.exists(b13):
        print("Error: session", b13, "already exists")
        exit(-1)
    fonk6(b13, b12.run_file)
    fonk7(b13)
if b15 = = '__main__':
    fonk8()