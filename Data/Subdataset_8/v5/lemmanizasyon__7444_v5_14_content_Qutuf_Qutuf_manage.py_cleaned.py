import os
import sys
def set_django_settings_module():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webservice.settings")
def execute_django_management_commands():
    try:
        from django.core.management import execute_from_command_line
        execute_from_command_line(sys.argv)
    except ImportError as e:
        handle_django_import_error(e)
def handle_django_import_error(error):
    try:
        import django
    except ImportError:
        raise ImportError(
            "Couldn't import Django. Please ensure it's installed "
            "and available on your PYTHONPATH environment variable. "
            "Did you forget to activate a virtual environment?"
        ) from error
if __name__ == "__main__":
    set_django_settings_module()
    execute_django_management_commands()