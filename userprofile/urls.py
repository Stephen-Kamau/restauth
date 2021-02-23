from django.conf.urls import url
from django.urls import path
from .views import UserProfileView


urlpatterns = [
    path('', UserProfileView.as_view()),
    ]
