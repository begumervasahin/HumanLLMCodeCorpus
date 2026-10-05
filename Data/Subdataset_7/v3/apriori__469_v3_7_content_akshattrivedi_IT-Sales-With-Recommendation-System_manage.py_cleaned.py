import os
import sys
from django.core.management import execute_from_command_line
from django.db import models
class class1(models.Model):
    b1 = models.CharField(max_length=100)
class class2(models.Model):
    b1 = models.CharField(max_length=100)
class class3(models.Model):
    b2 = models.ForeignKey(class1, on_delete=models.CASCADE)
    b3 = models.ForeignKey(class2, on_delete=models.CASCADE)
def fonk1():
    pass
if b4 = = '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'it_sales.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Make sure it's installed and available "
            "on your PYTHONPATH environment variable. Did you forget to "
            "activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)