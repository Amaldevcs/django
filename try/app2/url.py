from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views
from django.conf.urls import include
urlpatterns = [
                url(r'^$',views.play,name='play'),
                url(r'^contact/$',views.contact,name='contact'),
                url(r'^about/$',views.about,name="about"),
                url(r'^job/$',views.jobs,name="job"),
                url(r'^add/$',views.add,name="add"),
                url(r'^delete/(?P<pk>\d+)/$',views.deletes,name='deletes'),
                url(r'^apply/$',views.appl,name="apply"),
                url(r'^applicant/$',views.applicant,name="applicant"),
                url(r'^applied/$',views.applied,name="applied"),


                ]
if settings.DEBUG:
	urlpatterns+= static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
