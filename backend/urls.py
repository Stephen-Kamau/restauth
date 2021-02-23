from django.conf.urls import  url
from django.urls import path
from . import views
from .views import UserRegistrationView , UserLoginView


urlpatterns =[

    path('' , views.index),
    path('signup/', UserRegistrationView.as_view()),
    path('signin/', UserLoginView.as_view()),
]
