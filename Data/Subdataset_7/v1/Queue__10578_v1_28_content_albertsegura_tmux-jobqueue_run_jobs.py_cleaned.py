import sys
import argparse
import os
import subprocess
import datetime
b1 = {'yes', 'y', '', 'si', 's'}
b2 = {'no', 'n'}
b3 = argparse.ArgumentParser(description='Mem trace analysis run folder')
b3.add_argument('b6', b4 = "store", help='')
b3.add_argument('run_file', b4 = "store", help='')
b5 = b3.parse_args()
b6 = "job_" + os.path.relpath(b5.b6) + "_" + str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
b7 = b6 + ".log"
if not os.path.isfile(b5.run_file):
    print("Error: \"" + b5.run_file + "\" not a file")
    exit(-1)
print("Session name:", b6)
print("Runfile:", b5.run_file, "\n")
print("Runfile content:")
with open(b5.run_file) as runfile:
    print("========================================")
    for b10, line in enumerate(runfile):
        b8 = line.rstrip('\n')
        if b8 != "":
            print(str(b10) + ": " + line, b9 = '')
    print("========================================")
b10 = sum(1 for line in open(b5.run_file) if line.strip())
print("Detected " + str(b10) + " jobs to run\n")
b11 = input("Is runfile content correct? [Y/n] ").lower()
if b11 not in b1:
    exit(-1)
if os.environ.get("TMUX") is not None:
    b12 = input("Running inside TMUX, proceed? [Y/n] ").lower()
    if b12 not in b1:
        exit(-1)
    del os.environ['TMUX']
b13 = os.system("tmux has-session -t " + b6 + " > /dev/null 2>&1") == 0
if b13:
    print("Error: session", b6, "already exists")
    exit(-1)
b14 = "python3 ~/scripts/run_jobs_launcher.py " + b6 + " " + b5.run_file
b14 += " ; read"
b15 = ["tmux", "new-session", "-d", "-s", b6, b14]
try:
    subprocess.check_output(b15)
except subprocess.CalledProcessError as e:
    print("Error: when launching", b15)
    exit(-1)
print("Session launched")
b16 = input("Switch to tmux job session? [Y/n] ").lower()
if b16 in b1:
    b15 = ["tmux", "switch-client", "-t", b6]
    subprocess.check_output(b15)