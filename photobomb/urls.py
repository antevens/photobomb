from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import photobomb.imagine.views

# Examples:
# url(r'^$', 'photobomb.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', photobomb.imagine.views.index, name='index'),
#    url(r'^admin/', include(admin.site.urls)),
]
