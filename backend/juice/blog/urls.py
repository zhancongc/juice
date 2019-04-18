from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user/pass', views.user_pass, name='user_pass'),
]
