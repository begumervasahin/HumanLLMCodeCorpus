import os
import sys
def fonk1():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mypubsub.settings')
def fonk2():
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Make sure it's installed and "
            "available on your PYTHONPATH environment variable. Also, "
            "ensure that you've activated a virtual environment if needed."
        ) from exc
    execute_from_command_line(sys.argv)
def fonk3():
    fonk1()
    fonk2()
if b1 = = '__main__':
    fonk3()