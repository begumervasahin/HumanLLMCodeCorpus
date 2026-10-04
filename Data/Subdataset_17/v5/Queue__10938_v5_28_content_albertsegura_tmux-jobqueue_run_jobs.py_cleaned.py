import sys
import argparse
import os
import subprocess
import datetime
YES_ANSWERS = {'yes', 'y', '', 'si', 's'}
NO_ANSWERS = {'no', 'n'}
def parse_arguments():
    parser = argparse.ArgumentParser(description='Mem trace analysis run folder')
    parser.add_argument('session_name', help='Session name for the tmux session')
    parser.add_argument('run_file', help='File containing the list of jobs to run')
    return parser.parse_args()
def check_run_file_exists(run_file):
    if not os.path.isfile(run_file):
        print(f'Error: "{run_file}" not a file')
        sys.exit(-1)
def create_session_name(session_name):
    return f"job_{os.path.relpath(session_name)}_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"
def print_runfile_content(run_file):
    print("\nRunfile content:")
    print("========================================")
    with open(run_file) as f:
        lines = f.readlines()
        for idx, line in enumerate(lines):
            print(f"{idx}: {line}", end='')
    print("========================================")
    print(f"Detected {len(lines)} jobs to run\n")
    return lines
def confirm_runfile_content():
    iscorrect = input("Is runfile content correct? [Y/n] ").lower()
    if iscorrect not in YES_ANSWERS:
        sys.exit(-1)
def check_tmux_environment():
    if "TMUX" in os.environ:
        insidetmux = input("Running inside TMUX, proceed? [Y/n] ").lower()
        if insidetmux not in YES_ANSWERS:
            sys.exit(-1)
        del os.environ['TMUX']
def check_tmux_session_exists(session_name):
    try:
        subprocess.check_output(["tmux", "has-session", "-t", session_name], stderr=subprocess.STDOUT)
        return True
    except subprocess.CalledProcessError:
        return False
def launch_tmux_session(session_name, run_file):
    try:
        tmux_cmds = f"python3 ~/scripts/run_jobs_launcher.py {session_name} {run_file} ; read"
        subprocess.check_output(["tmux", "new-session", "-d", "-s", session_name, tmux_cmds])
    except subprocess.CalledProcessError:
        print("Error: when launching tmux session")
        sys.exit(-1)
    print("Session launched")
def switch_to_tmux_session(session_name):
    wantstoattach = input("Switch to tmux job session? [Y/n] ").lower()
    if wantstoattach in YES_ANSWERS:
        subprocess.check_output(["tmux", "switch-client", "-t", session_name])
def main():
    args = parse_arguments()
    check_run_file_exists(args.run_file)
    session_name = create_session_name(args.session_name)
    print("Session name:", session_name)
    print("Runfile:", args.run_file)
    lines = print_runfile_content(args.run_file)
    confirm_runfile_content()
    check_tmux_environment()
    if check_tmux_session_exists(session_name):
        print(f"Error: session {session_name} already exists")
        sys.exit(-1)
    launch_tmux_session(session_name, args.run_file)
    switch_to_tmux_session(session_name)
if __name__ == '__main__':
    main()