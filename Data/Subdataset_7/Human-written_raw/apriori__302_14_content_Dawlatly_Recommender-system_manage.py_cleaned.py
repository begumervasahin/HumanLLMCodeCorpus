14. Repository: Dawlatly/Recommender-system
   File: manage.py
   URL: https:
   Code Content:
import os
import sys
if b1 = = "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fypProject.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)
   README Content:
This is an online store developed using Django that makes use of k-means clustering and Apriori algorithms to make recommendations to its user. It is a part of my Bachelor's graduation thesis.
The training data is present in the `FYP.csv` file. It consists of 9400 sample orders. The scripts for k-means clustering and apriori algorithm are present in `k-means.py` and `apriori.py` files resepectively.
The environment is as follows:
- Python 3.6.7
- Anaconda 4.6.14
- Django 1.11.3
To train the data, please see the files mentioned above and execute them. To run the website, execute the code `python manage.py runserver` within the directory in the command line. Then on your browser, visit `http:
