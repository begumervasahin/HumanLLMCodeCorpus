
import os
import sys
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "root.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Django couldn't be imported. Please ensure it's installed and "
            "accessible on your PYTHONPATH environment variable. Have you "
            "forgotten to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)