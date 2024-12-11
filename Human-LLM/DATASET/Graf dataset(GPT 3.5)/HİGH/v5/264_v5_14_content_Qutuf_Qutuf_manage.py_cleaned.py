import os
import sys
def fonk1():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webservice.settings")
def fonk2():
    try:
        from django.core.management import execute_from_command_line
        execute_from_command_line(sys.argv)
    except ImportError as e:
        fonk3(e)
def fonk3(error):
    try:
        import django
    except ImportError:
        raise ImportError(
            "Couldn't import Django. Please ensure it's installed "
            "and available on your PYTHONPATH environment variable. "
            "Did you forget to activate a virtual environment?"
        ) from error
if b1 = = "__main__":
    fonk1()
    fonk2()