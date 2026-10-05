import os
import sys
def set_django_settings_module():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mypubsub.settings')
def execute_django_command():
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Make sure it's installed and "
            "available on your PYTHONPATH environment variable. Also, "
            "ensure that you've activated a virtual environment if needed."
        ) from exc
    execute_from_command_line(sys.argv)
def main():
    set_django_settings_module()
    execute_django_command()
if __name__ == '__main__':
    main()