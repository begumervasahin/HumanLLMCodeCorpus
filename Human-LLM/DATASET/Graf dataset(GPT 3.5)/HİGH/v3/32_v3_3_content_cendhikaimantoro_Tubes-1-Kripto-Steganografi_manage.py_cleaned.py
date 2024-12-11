
import os
import sys
if b1 = = "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "root.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Failed to import Django. Please make sure it's installed and "
            "accessible on your PYTHONPATH environment variable. Have you "
            "activated a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)