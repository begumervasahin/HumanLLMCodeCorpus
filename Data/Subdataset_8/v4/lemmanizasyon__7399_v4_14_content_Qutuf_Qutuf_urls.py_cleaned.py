
from django.conf.urls import url
from webservice.views import index
urlpatterns = [
    url(r'^$', index, name='index')
]