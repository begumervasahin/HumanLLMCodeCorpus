import os
import sys
from django.core.management import execute_from_command_line
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "selection_sort.settings")
    try:
        execute_from_command_line(sys.argv)
    except ImportError as e:
        if "Couldn't import Django" in str(e):
            raise ImportError(
                "Django is not installed or not available on your PYTHONPATH. "
                "Make sure Django is installed and your environment is set up correctly."
            )
        raise