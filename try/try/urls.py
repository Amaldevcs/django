from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin
urlpatterns = [
               
               url(r'^admin/', admin.site.urls),
               url(r'',include ('app2.url')),
                url(r'^accounts/', include('registration.backends.simple.urls')),
               #url(r'^contact/',include ('app1.url')),
 ]
#if settings.DEBUG:
#	urlpatterns+= static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
#	urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
