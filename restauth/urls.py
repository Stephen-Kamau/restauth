from django.conf.urls import include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/' ,include('backend.urls')),
    path('api/v1/profile/' ,include('userprofile.urls')),

]
