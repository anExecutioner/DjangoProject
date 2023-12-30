from django.urls import path
from django.conf import urls
from playground import views

urlpatterns = [
    path("", views.index,name='home'),
    path("help/",views.help,name = 'help')
 ]
