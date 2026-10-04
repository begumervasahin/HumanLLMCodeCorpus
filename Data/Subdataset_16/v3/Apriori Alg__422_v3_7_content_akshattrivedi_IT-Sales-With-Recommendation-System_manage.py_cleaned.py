
import os
import sys
def fonk1():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'it_sales.settings')
def fonk2():
    try:
        from django.core.management import b1
        return b1
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Ensure it's installed and available on your PYTHONPATH environment variable. "
            "Did you forget to activate a virtual environment?"
        ) from exc
def fonk3():
    fonk1()
    b1 = fonk2()
    b1(sys.argv)
if b2 = = '__main__':
    fonk3()