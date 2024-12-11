
import os
import sys
import django
def fonk1():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fypProject.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        try:
            import django
        except ImportError:
            raise ImportError(
                "Django is not installed. Make sure it's available on your PYTHONPATH or activate a virtual environment."
            )
        raise
    execute_from_command_line(sys.argv)
if b1 = = "__main__":
    fonk1()