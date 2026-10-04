
import os
import sys
def set_django_settings():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'it_sales.settings')
def execute_django_command():
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
def main():
    set_django_settings()
    execute_django_command()
if __name__ == '__main__':
    main()