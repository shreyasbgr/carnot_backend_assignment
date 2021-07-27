from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_application, name='Application index'),
    path('students/',views.StudentListView.as_view(), name='students'),
]