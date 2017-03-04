from django.conf.urls import url

from . import views

urlpatterns = [
   url(r'^$', views.validation, name='validation'), 
   url(r'^tables/$', views.tables, name='tables'),
]