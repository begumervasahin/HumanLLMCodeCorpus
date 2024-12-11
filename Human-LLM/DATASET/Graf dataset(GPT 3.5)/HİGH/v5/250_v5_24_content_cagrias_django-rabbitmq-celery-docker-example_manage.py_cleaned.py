import os
import sys
from django.core.management import execute_from_command_line
def fonk1():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mypubsub.settings')
def fonk2():
    try:
        execute_from_command_line(sys.argv)
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
def fonk3():
    fonk1()
    fonk2()
if b1 = = '__main__':
    fonk3()