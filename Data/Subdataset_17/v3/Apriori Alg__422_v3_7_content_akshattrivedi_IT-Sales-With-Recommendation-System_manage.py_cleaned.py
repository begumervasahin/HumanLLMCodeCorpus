
import os
import sys
def set_django_settings_module():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'it_sales.settings')
def import_django_execute():
    try:
        from django.core.management import execute_from_command_line
        return execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Ensure it's installed and available on your PYTHONPATH environment variable. "
            "Did you forget to activate a virtual environment?"
        ) from exc
def main():
    set_django_settings_module()
    execute_from_command_line = import_django_execute()
    execute_from_command_line(sys.argv)
if __name__ == '__main__':
    main()