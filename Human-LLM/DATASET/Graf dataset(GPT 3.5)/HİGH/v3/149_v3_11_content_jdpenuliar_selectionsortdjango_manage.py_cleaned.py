import os
import sys
from django.core.management import execute_from_command_line
def fonk1():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
def fonk2():
    execute_from_command_line(sys.argv)
if b1 = = "__main__":
    fonk1()
    fonk2()