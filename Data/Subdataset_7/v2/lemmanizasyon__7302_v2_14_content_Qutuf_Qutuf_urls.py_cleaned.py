
from django.conf.urls import url
from webservice.views import index
b1 = [
    url(
        r'^$',
        index,
        b2 = 'index'
    )
]
def fonk1(request):
    return "Welcome to the index page!"
if b3 = = "__main__":
    for url_pattern in b1:
        print(url_pattern)