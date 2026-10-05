import os
import sys
from django.core.management import execute_from_command_line
def set_django_settings_module():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mypubsub.settings')
def execute_django_command_line():
    try:
        execute_from_command_line(sys.argv)
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
def main():
    set_django_settings_module()
    execute_django_command_line()
if __name__ == '__main__':
    main()