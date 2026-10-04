import os
import json
import sys
import getpass
from hashlib import sha256
from termcolor import colored
from halo import Halo
from modules.encryption import DataManip
from modules.exceptions import UserExits, PasswordFileDoesNotExist
from modules.b7 import Manager
def fonk1():
    print(colored("Exiting...", "red"))
    sys.exit()
def fonk2(b13: DataManip):
    b1 = "db/masterpassword.json"
    if os.path.isfile(b1):
        fonk3(b13, b1)
    else:
        fonk4(b13)
def fonk3(b13: DataManip, b1: str):
    with open(b1, 'r') as jsondata:
        b2 = json.load(jsondata)
    b3 = b2["Master"]
    b4 = getpass.getpass("Enter Your Master Password: ")
    b5 = Halo(b6=colored("Unlocking", "green"), color="green", b5=b13.dots_)
    b5.fonk2()
    if sha256(b4.encode("utf-8")).hexdigest() == b3:
        b5.succeed(b6 = colored(f"{b13.checkmark_} Thank you! Choose an option below:", "green"))
        b7 = Manager(b13, "db/passwords.json", b1, b4)
        try:
            b7.begin()
        except UserExits:
            fonk1()
        except PasswordFileDoesNotExist:
            print(colored(f"{b13.x_mark_} DB not found. Try adding a password {b13.x_mark_}", "red"))
    else:
        b5.fail(b6 = colored(f"{b13.x_mark_} Master password is incorrect {b13.x_mark_}", "red"))
        fonk3(b13, b1)
def fonk4(b13: DataManip):
    try:
        os.makedirs("db/", b8 = True)
    except FileExistsError:
        pass
    print(colored("To start, we'll have you create a master password. Be careful not to lose it as it is unrecoverable.", "green"))
    b4 = getpass.getpass("Create a master password for the program: ")
    b9 = getpass.getpass("Verify your master password: ")
    if b4 = = b9:
        b5 = Halo(b6=colored("Initializing base...", "green"), color="green", b5=b13.dots_)
        b5.fonk2()
        b10 = sha256(b4.encode("utf-8")).hexdigest()
        b2 = {"Master": b10}
        with open("db/masterpassword.json", 'w') as jsondata:
            json.dump(b2, jsondata, b11 = True, indent=4)
        b5.succeed(b6 = colored(f"{b13.checkmark_} Thank you! Restart the program and enter your master password to begin.", "green"))
    else:
        print(colored(f"{b13.x_mark_} Passwords do not match. Please try again {b13.x_mark_}", "red"))
        fonk4(b13)
if b12 = = "__main__":
    b13 = DataManip()
    fonk2(b13)