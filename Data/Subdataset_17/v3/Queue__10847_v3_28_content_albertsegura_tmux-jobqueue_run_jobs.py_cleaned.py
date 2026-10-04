import sys
import argparse
import os
import datetime
import subprocess
YES_ANSWERS = {'yes', 'y', '', 'si', 's'}
NO_ANSWERS = {'no', 'n'}
def setup_argument_parser():
    parser = argparse.ArgumentParser(description='Mem trace analysis run folder')
    parser.add_argument('session_name', help='Session name for the TMUX session')
    parser.add_argument('run_file', help='Path to the run file')
    return parser.parse_args()
def generate_session_names(session_name):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    session_name = f"job_{os.path.basename(session_name)}_{timestamp}"
    session_logname = f"{session_name}.log"
    return session_name, session_logname
def check_run_file(run_file):
    if not os.path.isfile(run_file):
        print(f'Error: "{run_file}" not a file')
        sys.exit(-1)
def display_run_file_content(run_file):
    print("Runfile content:")
    print("========================================")
    with open(run_file, 'r') as file:
        lines = file.readlines()
    for idx, line in enumerate(lines):
        print(f"{idx}: {line}", end='')
    print("\n========================================")
    print(f"Detected {idx + 1} jobs to run\n")
    return idx + 1
def confirm_run_file_content():
    is_correct = input("Is runfile content correct? [Y/n] ").lower()
    if is_correct not in YES_ANSWERS:
        sys.exit(-1)
def check_tmux_environment():
    if os.environ.get("TMUX"):
        inside_tmux = input("Running inside TMUX, proceed? [Y/n] ").lower()
        if inside_tmux not in YES_ANSWERS:
            sys.exit(-1)
        del os.environ['TMUX']
def check_tmux_session_exists(session_name):
    try:
        subprocess.check_output(["tmux", "has-session", "-t", session_name], stderr=subprocess.STDOUT)
        print(f"Error: session {session_name} already exists")
        sys.exit(-1)
    except subprocess.CalledProcessError:
        pass
def launch_tmux_session(session_name, run_file):
    try:
        tmux_cmds = f"python3 ~/scripts/run_jobs_launcher.py {session_name} {run_file} ; read"
        subprocess.check_output(["tmux", "new-session", "-d", "-s", session_name, tmux_cmds])
        print("Session launched")
    except subprocess.CalledProcessError as e:
        print(f"Error: when launching {e.cmd}")
        sys.exit(-1)
def ask_to_attach_tmux_session(session_name):
    wants_to_attach = input("Switch to tmux job session? [Y/n] ").lower()
    if wants_to_attach in YES_ANSWERS:
        subprocess.check_output(["tmux", "switch-client", "-t", session_name])
def main():
    args = setup_argument_parser()
    session_name, session_logname = generate_session_names(args.session_name)
    print("Session name:", session_name)
    print("Runfile:", args.run_file, "\n")
    check_run_file(args.run_file)
    display_run_file_content(args.run_file)
    confirm_run_file_content()
    check_tmux_environment()
    check_tmux_session_exists(session_name)
    launch_tmux_session(session_name, args.run_file)
    ask_to_attach_tmux_session(session_name)
if __name__ == "__main__":
    main()