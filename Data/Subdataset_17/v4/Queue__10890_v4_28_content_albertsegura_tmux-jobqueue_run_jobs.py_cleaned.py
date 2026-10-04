import sys
import argparse
import os
import subprocess
import datetime
YES_ANSWERS = {'yes', 'y', '', 'si', 's'}
NO_ANSWERS = {'no', 'n'}
parser = argparse.ArgumentParser(description='Mem trace analysis run folder')
parser.add_argument('session_name', help='Session name for the tmux session')
parser.add_argument('run_file', help='File containing the list of jobs to run')
args = parser.parse_args()
session_name = f"job_{os.path.relpath(args.session_name)}_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"
session_logname = f"{session_name}.log"
if not os.path.isfile(args.run_file):
    print(f'Error: "{args.run_file}" not a file')
    sys.exit(-1)
print("Session name:", session_name)
print("Runfile:", args.run_file)
print("\nRunfile content:")
print("========================================")
with open(args.run_file) as runfile:
    lines = runfile.readlines()
    for idx, line in enumerate(lines):
        print(f"{idx}: {line}", end='')
print("========================================")
print(f"Detected {len(lines)} jobs to run\n")
iscorrect = input("Is runfile content correct? [Y/n] ").lower()
if iscorrect not in YES_ANSWERS:
    sys.exit(-1)
if "TMUX" in os.environ:
    insidetmux = input("Running inside TMUX, proceed? [Y/n] ").lower()
    if insidetmux not in YES_ANSWERS:
        sys.exit(-1)
    del os.environ['TMUX']
session_exists = True
try:
    cmd = ["tmux", "has-session", "-t", session_name]
    subprocess.check_output(cmd, stderr=subprocess.STDOUT)
except subprocess.CalledProcessError:
    session_exists = False
if session_exists:
    print(f"Error: session {session_name} already exists")
    sys.exit(-1)
try:
    tmux_cmds = f"python3 ~/scripts/run_jobs_launcher.py {session_name} {args.run_file} ; read"
    cmd = ["tmux", "new-session", "-d", "-s", session_name, tmux_cmds]
    subprocess.check_output(cmd)
except subprocess.CalledProcessError as e:
    print("Error: when launching", cmd)
    sys.exit(-1)
print("Session launched")
wantstoattach = input("Switch to tmux job session? [Y/n] ").lower()
if wantstoattach in YES_ANSWERS:
    cmd = ["tmux", "switch-client", "-t", session_name]
    subprocess.check_output(cmd)