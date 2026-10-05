import sys
import argparse
import os
import subprocess
import datetime
b1 = {'yes', 'y', '', 'si', 's'}
b2 = {'no', 'n'}
def fonk1(b13):
    return "job_" + os.path.relpath(b13) + "_" + datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
def fonk2(runfile):
    print("Runfile content:")
    print("========================================")
    for b14, line in enumerate(runfile):
        b3 = line.rstrip('\n')
        if b3 != "":
            print(str(b14) + ": " + line, b4 = '')
    print("========================================")
def fonk3(runfile_path):
    return sum(1 for line in open(runfile_path) if line.strip())
def fonk4():
    if os.environ.get("TMUX") is not None:
        b5 = input("Running inside TMUX, proceed? [Y/n] ").lower()
        if b5 not in b1:
            exit(-1)
        del os.environ['TMUX']
def fonk5(b13, runfile_path):
    b6 = "python3 ~/scripts/run_jobs_launcher.py " + b13 + " " + runfile_path
    b6 += " ; read"
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
    b10.add_argument('b13', b11 = "store", help='')
    b10.add_argument('run_file', b11 = "store", help='')
    b12 = b10.parse_args()
    b13 = fonk1(b12.b13)
    if not os.path.isfile(b12.run_file):
        print("Error: \"" + b12.run_file + "\" not a file")
        exit(-1)
    print("Session name:", b13)
    print("Runfile:", b12.run_file, "\n")
    with open(b12.run_file) as runfile:
        fonk2(runfile)
    b14 = fonk3(b12.run_file)
    print("Detected " + str(b14) + " jobs to run\n")
    b15 = input("Is runfile content correct? [Y/n] ").lower()
    if b15 not in b1:
        exit(-1)
    fonk4()
    fonk5(b13, b12.run_file)
    fonk6(b13)