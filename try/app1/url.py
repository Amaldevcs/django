from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views
from django.conf.urls import include
urlpatterns = [
                url(r'^$',views.play,name='play'),
                url(r'^contact/$',views.contact,name='contact'),
                url(r'^about/$',views.about,name='about'),
                url(r'^marksheet/$',views.marks,name='marksheet'),
               #url(r'^accounts/',include('registration.backends.default.urls'
               url(r'^add/$',views.add,name='add'),
                url(r'^delete/(?P<pk>\d+)/$',views.deletes,name='deletes'),
               url(r'^tweets/$',views.tweets,name='tweets'),
               url(r'^converter/$',views.converter,name='converter'),
               url(r'^rss/$',views.rsss,name='rss'),
               url(r'^chat/$',views.chat,name='chat'),


                ]
if settings.DEBUG:
	urlpatterns+= static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
