
from django.conf.urls import url
from webservice.views import index
b1 = [
    url(r'^$', index, b2 = 'index')
]