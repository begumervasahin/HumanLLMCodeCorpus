import os
import sys
from django.core.management import execute_from_command_line
def fonk1():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webservice.settings")
    try:
        execute_from_command_line(sys.argv)
    except ImportError:
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Make sure it's installed and "
                "available on your PYTHONPATH environment variable. Did you "
                "forget to activate a virtual environment?"
            )
        raise
if b1 = = "__main__":
    fonk1()