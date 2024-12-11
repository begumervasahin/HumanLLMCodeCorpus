import os
import json
import sys
import getpass
from os.path import isfile
from hashlib import sha256
from termcolor import colored
from halo import Halo
from modules.encryption import DataManip
from modules.exceptions import UserExits, PasswordFileDoesNotExist
from modules.b5 import Manager
def fonk1():
    print(colored("Exiting...", "red"))
    sys.exit()
def fonk2(b10: DataManip):
    if os.path.isfile("db/masterpassword.json"):
        with open("db/masterpassword.json", 'r') as jsondata:
            b1 = json.load(jsondata)
        b2 = b1["Master"]
        b3 = getpass.getpass("Enter Your Master Password: ")
        b4 = Halo(text=colored("Unlocking", "green"), color="green", b4=b10.dots_)
        if sha256(b3.encode("utf-8")).hexdigest() == b2:
            print(colored(f"{b10.checkmark_} Thank you! Choose an option below:", "green"))
            b5 = Manager(b10, "db/passwords.json", "db/masterpassword.json", b3)
            try:
                b5.begin()
            except UserExits:
                fonk1()
            except PasswordFileDoesNotExist:
                print(colored(f"{b10.x_mark_} DB not found. Try adding a password {b10.x_mark_}", "red"))
        else:
            print(colored(f"{b10.x_mark_} Master password is incorrect {b10.x_mark_}", "red"))
            return fonk2(b10)
    else:
        try:
            os.mkdir("db/")
        except FileExistsError:
            pass
        print(colored("To start, we'll have you create a master password. Be careful not to lose it as it is unrecoverable.", "green"))
        b3 = getpass.getpass("Create a master password for the program: ")
        b6 = getpass.getpass("Verify your master pasword: ")
        if b3 = = b6:
            b4 = Halo(text=colored("initializing base...", "green"), color="green", b4=b10.dots_)
            b7 = sha256(b3.encode("utf-8")).hexdigest()
            b1 = {"Master": {}}
            b1["Master"] = b7
            with open("db/masterpassword.json", 'w') as jsondata:
                json.dump(b1, jsondata, b8 = True, indent=4)
            b4.stop()
            print(colored(f"{b10.checkmark_} Thank you! Restart the program and enter your master password to begin.", "green"))
        else:
            print(colored(f"{b10.x_mark_} Passwords do not match. Please try again {b10.x_mark_}", "red"))
            return fonk2(b10)
if b9 = = "__main__":
    b10 = DataManip()
    fonk2(b10)