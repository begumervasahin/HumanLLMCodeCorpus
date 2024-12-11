import sys
import argparse
import os
import subprocess
import datetime
b1 = {'yes', 'y', '', 'si', 's'}
b2 = {'no', 'n'}
b3 = argparse.ArgumentParser(description='Mem trace analysis run folder')
b3.add_argument('b6', b4 = "store", help='Session name')
b3.add_argument('run_file', b4 = "store", help='Path to the run file')
b5 = b3.parse_args()
b6 = "job_" + os.path.relpath(b5.b6) + "_" + str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
b7 = b6 + ".log"
if not os.path.isfile(b5.run_file):
    print("Error: \"" + b5.run_file + "\" is not a file")
    exit(-1)
print("Session name:", b6)
print("Runfile:", b5.run_file, "\n")
print("Runfile content:")
print("========================================")
with open(b5.run_file) as runfile:
    for idx, line in enumerate(runfile):
        b8 = line.rstrip('\n')
        if b8 != "":
            print(str(idx) + ": " + b8)
print("========================================")
print("Detected", idx, "jobs to run")
b9 = input("Is runfile content correct? [Y/n] ").lower()
if b9 not in b1:
    exit(-1)
if os.environ.copy().get("TMUX") is not None:
    b10 = input("Running inside TMUX, proceed? [Y/n] ").lower()
    if b10 not in b1:
        exit(-1)
    del os.environ['TMUX']
b11 = os.path.exists(b6)
if b11:
    print("Error: session", b6, "already exists")
    exit(-1)
try:
    b12 = "python3 ~/scripts/run_jobs_launcher.py " + b6 + " " + b5.run_file
    b12 += " ; read"
    b13 = ["tmux", "new-session", "-d", "-s", b6, b12]
    b14 = subprocess.check_output(b13)
except subprocess.CalledProcessError as e:
    print("Error: when launching", b13)
    exit(-1)
print("Session launched")
b15 = input("Switch to tmux job session? [Y/n] ").lower()
if b15 in b1:
    b13 = ["tmux", "switch-client", "-t", b6]
    b14 = subprocess.check_output(b13)