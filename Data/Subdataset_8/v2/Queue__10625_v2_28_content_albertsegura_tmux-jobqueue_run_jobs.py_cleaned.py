import sys
import argparse
import os
import subprocess
import datetime
yes_answers = {'yes', 'y', '', 'si', 's'}
no_answers = {'no', 'n'}
def generate_session_name(session_name):
    return "job_" + os.path.relpath(session_name) + "_" + datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
def print_runfile_content(runfile):
    print("Runfile content:")
    print("========================================")
    for idx, line in enumerate(runfile):
        linecmd = line.rstrip('\n')
        if linecmd != "":
            print(str(idx) + ": " + line, end='')
    print("========================================")
def count_jobs_in_runfile(runfile_path):
    return sum(1 for line in open(runfile_path) if line.strip())
def check_tmux():
    if os.environ.get("TMUX") is not None:
        insidetmux = input("Running inside TMUX, proceed? [Y/n] ").lower()
        if insidetmux not in yes_answers:
            exit(-1)
        del os.environ['TMUX']
def launch_tmux_session(session_name, runfile_path):
    tmux_cmds = "python3 ~/scripts/run_jobs_launcher.py " + session_name + " " + runfile_path
    tmux_cmds += " ; read"
    cmd = ["tmux", "new-session", "-d", "-s", session_name, tmux_cmds]
    try:
        subprocess.check_output(cmd)
    except subprocess.CalledProcessError as e:
        print("Error: when launching", cmd)
        exit(-1)
    print("Session launched")
def switch_to_tmux_session(session_name):
    wantstoattach = input("Switch to tmux job session? [Y/n] ").lower()
    if wantstoattach in yes_answers:
        cmd = ["tmux", "switch-client", "-t", session_name]
        subprocess.check_output(cmd)
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Mem trace analysis run folder')
    parser.add_argument('session_name', action="store", help='')
    parser.add_argument('run_file', action="store", help='')
    args = parser.parse_args()
    session_name = generate_session_name(args.session_name)
    if not os.path.isfile(args.run_file):
        print("Error: \"" + args.run_file + "\" not a file")
        exit(-1)
    print("Session name:", session_name)
    print("Runfile:", args.run_file, "\n")
    with open(args.run_file) as runfile:
        print_runfile_content(runfile)
    idx = count_jobs_in_runfile(args.run_file)
    print("Detected " + str(idx) + " jobs to run\n")
    iscorrect = input("Is runfile content correct? [Y/n] ").lower()
    if iscorrect not in yes_answers:
        exit(-1)
    check_tmux()
    launch_tmux_session(session_name, args.run_file)
    switch_to_tmux_session(session_name)