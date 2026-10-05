import os
import sys
from django.core.management import execute_from_command_line
from django.db import models
class Client(models.Model):
    name = models.CharField(max_length=100)
class Product(models.Model):
    name = models.CharField(max_length=100)
class Purchase(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
def apriori_recommendation():
    pass
if __name__ == '__main__':
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