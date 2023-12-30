from django.contrib import admin
from django.urls import path
from playground import views
from django.conf.urls import include
from playground.views import index


urlpatterns = [
    path("admin/", admin.site.urls),
    path("playground", include('playground.urls')),
    path("", views.index, name = 'index')

]
