import sys
import argparse
import collections
import os
import math
import subprocess
import datetime
import re
import time
b1 = {'yes','y', '', 'si', 's'}
b2 = {'no','n'}
b3 = argparse.ArgumentParser(description = 'Mem trace analysis run folder')
b3.add_argument('b6', b4 = "store", help='');
b3.add_argument('run_file', b4 = "store", help='');
b5 = b3.parse_args();
b6 = "job_"+os.path.relpath(b5.b6)+"_"+str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
b7 = b6+".log"
if not os.path.isfile(b5.run_file):
	print("Error: \""+b5.run_file+"\" not a file")
	exit(-1)
print ("Session name:", b6)
print ("Runfile:", b5.run_file,"\n")
print ("Runfile content:")
b8 = open(b5.run_file)
print ("========================================")
a1 = 0
for line in b8:
    b9 = line.rstrip('\n')
    if b9 != "":
        print(str(a1)+": "+line,b10 = '')
        a1 += 1
b8.close()
print ("========================================")
print("Detected "+str(a1)+" jobs to run")
print ("")
b11 = input("Is b8 content correct? [Y/n] ").lower()
if b11 not in b1:
	exit(-1)
if os.environ.copy().get("TMUX") != None:
    b12 = input("Running inside TMUX, procede? [Y/n] ").lower()
    if b12 not in b1:
        exit(-1)
    del os.environ['TMUX']
b13 = True
try:
    b14 = ["tmux", "has-session", "-t", b6]
    b15 = subprocess.check_output(b14, stderr=subprocess.STDOUT)
except subprocess.CalledProcessError as e:
    b13 = False
if b13:
    print("Error: session", b6, "already exists")
    exit(-1)
try:
    b16 = "python3 ~/scripts/run_jobs_launcher.py "+b6+" "+b5.run_file
    b16 += " ; read"
    b14 = ["tmux", "new-session", "-d", "-s", b6, b16]
    b15 = subprocess.check_output(b14)
except subprocess.CalledProcessError as e:
    print("Error: when launching",b14)
    exit(-1)
print("Session launched")
b17 = input("Switch to tmux job session? [Y/n] ").lower()
if b17 in b1:
	b14 = ["tmux", "switch-client", "-t", b6]
	b15 = subprocess.check_output(b14)