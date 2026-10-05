import os
import sys
from django.core.management import execute_from_command_line
def set_django_settings_module():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
def execute_management_command():
    execute_from_command_line(sys.argv)
if __name__ == "__main__":
    set_django_settings_module()
    execute_management_command()