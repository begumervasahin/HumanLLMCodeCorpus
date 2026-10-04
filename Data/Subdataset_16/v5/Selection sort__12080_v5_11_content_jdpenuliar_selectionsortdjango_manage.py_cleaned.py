import os
import sys
def fonk1():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "selection_sort.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        fonk2()
    execute_from_command_line(sys.argv)
def fonk2():
    try:
        import django
    except ImportError:
        raise ImportError(
            "Couldn't import Django. Ensure it's installed and available on your PYTHONPATH environment variable. "
            "Did you forget to activate a virtual environment?"
        )
    raise
if b1 = = "__main__":
    fonk1()