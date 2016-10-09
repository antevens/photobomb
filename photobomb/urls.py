from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.contrib import admin

admin.autodiscover()

import photobomb.imagine.views

# Examples:
# url(r'^$', 'photobomb.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
#    url(r'^$', photobomb.imagine.views.index, name='index'),
    url(r'^imagine/', include('photobomb.imagine.urls')),
    url(r'^$', RedirectView.as_view(url='/imagine/list/', permanent=True)),
#    url(r'^admin/', include(admin.site.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
