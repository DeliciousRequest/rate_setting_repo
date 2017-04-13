from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   url(r'^$', views.validation, name='validation'), 
   url(r'^tables/$', views.tables, name='tables'),
   url(r'^validate_tables/$', views.validate_tables, name='validate_tables'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)