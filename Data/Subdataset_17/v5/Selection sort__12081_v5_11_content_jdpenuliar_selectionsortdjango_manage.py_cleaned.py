import os
import sys
def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "selection_sort.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        handle_import_error()
    execute_from_command_line(sys.argv)
def handle_import_error():
    try:
        import django
    except ImportError:
        raise ImportError(
            "Couldn't import Django. Ensure it's installed and available on your PYTHONPATH environment variable. "
            "Did you forget to activate a virtual environment?"
        )
    raise
if __name__ == "__main__":
    main()