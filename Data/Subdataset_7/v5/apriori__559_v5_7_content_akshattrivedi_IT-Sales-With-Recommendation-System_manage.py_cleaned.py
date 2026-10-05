
import os
import sys
from django.core.management import execute_from_command_line
if b1 = = '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'it_sales.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        b2 = (
            "Couldn't import Django. Make sure it's installed and "
            "available on your PYTHONPATH environment variable. Did you "
            "forget to activate a virtual environment?"
        )
        raise ImportError(b2) from exc
    execute_from_command_line(sys.argv)