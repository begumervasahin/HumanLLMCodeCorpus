
import os
import sys
if b1 = = "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "root.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Please ensure it's installed and "
            "available on your PYTHONPATH environment variable. Also, check if you "
            "forgot to activate a virtual environment."
        ) from exc
    execute_from_command_line(sys.argv)