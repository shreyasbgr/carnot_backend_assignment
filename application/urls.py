from django.urls import path
from . import views

urlpatterns = [
    path('', views.helloApplication, name='Application index'),
]