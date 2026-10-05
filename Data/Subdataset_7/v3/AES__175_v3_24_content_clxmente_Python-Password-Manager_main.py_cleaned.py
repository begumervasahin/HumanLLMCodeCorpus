import os
import json
import sys
import getpass
from hashlib import sha256
from termcolor import colored
from halo import Halo
from modules.encryption import DataManip
from modules.exceptions import UserExits, PasswordFileDoesNotExist
from modules.b6 import Manager
def fonk1():
    print(colored("Exiting...", "red"))
    sys.exit()
def fonk2(b12: DataManip):
    b1 = "db/masterpassword.json"
    if os.path.isfile(b1):
        with open(b1, 'r') as json_file:
            b2 = json.load(json_file)
        b3 = b2["Master"]
        b4 = getpass.getpass("Enter Your Master Password: ")
        b5 = Halo(text=colored("Unlocking", "green"), color="green", b5=b12.dots_)
        if sha256(b4.encode("utf-8")).hexdigest() == b3:
            print(colored(f"{b12.checkmark_} Thank you! Choose an option below:", "green"))
            b6 = Manager(b12, "db/passwords.json", b1, b4)
            try:
                b6.begin()
            except UserExits:
                fonk1()
            except PasswordFileDoesNotExist:
                print(colored(f"{b12.x_mark_} DB not found. Try adding a password {b12.x_mark_}", "red"))
        else:
            print(colored(f"{b12.x_mark_} Master password is incorrect {b12.x_mark_}", "red"))
            return fonk2(b12)
    else:
        try:
            os.mkdir("db/")
        except FileExistsError:
            pass
        print(colored("To start, we'll have you create a master password. Be careful not to lose it as it is unrecoverable.", "green"))
        b7 = getpass.getpass("Create a master password for the program: ")
        b8 = getpass.getpass("Verify your master password: ")
        if b7 = = b8:
            b5 = Halo(text=colored("initializing base...", "green"), color="green", b5=b12.dots_)
            b9 = sha256(b7.encode("utf-8")).hexdigest()
            b2 = {"Master": {}}
            b2["Master"] = b9
            with open(b1, 'w') as json_file:
                json.dump(b2, json_file, b10 = True, indent=4)
            b5.stop()
            print(colored(f"{b12.checkmark_} Thank you! Restart the program and enter your master password to begin.", "green"))
        else:
            print(colored(f"{b12.x_mark_} Passwords do not match. Please try again {b12.x_mark_}", "red"))
            return fonk2(b12)
if b11 = = "__main__":
    b12 = DataManip()
    fonk2(b12)