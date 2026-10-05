import sys
import argparse
import os
import subprocess
import datetime
yes_answers = {'yes', 'y', '', 'si', 's'}
no_answers = {'no', 'n'}
parser = argparse.ArgumentParser(description='Mem trace analysis run folder')
parser.add_argument('session_name', action="store", help='Session name')
parser.add_argument('run_file', action="store", help='Path to the run file')
args = parser.parse_args()
session_name = "job_" + os.path.relpath(args.session_name) + "_" + str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
session_logname = session_name + ".log"
if not os.path.isfile(args.run_file):
    print("Error: \"" + args.run_file + "\" is not a file")
    exit(-1)
print("Session name:", session_name)
print("Runfile:", args.run_file, "\n")
print("Runfile content:")
print("========================================")
with open(args.run_file) as runfile:
    for idx, line in enumerate(runfile):
        linecmd = line.rstrip('\n')
        if linecmd != "":
            print(str(idx) + ": " + linecmd)
print("========================================")
print("Detected", idx, "jobs to run")
iscorrect = input("Is runfile content correct? [Y/n] ").lower()
if iscorrect not in yes_answers:
    exit(-1)
if os.environ.copy().get("TMUX") is not None:
    insidetmux = input("Running inside TMUX, proceed? [Y/n] ").lower()
    if insidetmux not in yes_answers:
        exit(-1)
    del os.environ['TMUX']
session_exists = os.path.exists(session_name)
if session_exists:
    print("Error: session", session_name, "already exists")
    exit(-1)
try:
    tmux_cmds = "python3 ~/scripts/run_jobs_launcher.py " + session_name + " " + args.run_file
    tmux_cmds += " ; read"
    cmd = ["tmux", "new-session", "-d", "-s", session_name, tmux_cmds]
    output = subprocess.check_output(cmd)
except subprocess.CalledProcessError as e:
    print("Error: when launching", cmd)
    exit(-1)
print("Session launched")
wantstoattach = input("Switch to tmux job session? [Y/n] ").lower()
if wantstoattach in yes_answers:
    cmd = ["tmux", "switch-client", "-t", session_name]
    output = subprocess.check_output(cmd)