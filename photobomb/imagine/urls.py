from django.conf.urls import url
from photobomb.imagine.views import list


urlpatterns = [
    url(r'^list/$', list, name='list')
]
