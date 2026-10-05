from django.conf.urls import url
from webservice.views import index
urlpatterns = [
    url(r'^$', index, name='index')
]
def index(request):
    return "Welcome to the index page!"
if __name__ == "__main__":
    for url_pattern in urlpatterns:
        print(url_pattern)