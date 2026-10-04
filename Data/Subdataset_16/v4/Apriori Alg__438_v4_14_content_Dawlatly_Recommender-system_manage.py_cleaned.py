
import os
import sys
def fonk1():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fypProject.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        fonk2(exc)
    execute_from_command_line(sys.argv)
def fonk2(exc):
    try:
        import django
    except ImportError:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    raise exc
if b1 = = "__main__":
    fonk1()