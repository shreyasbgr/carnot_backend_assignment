from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_application, name='Application index'),
    path('students/', views.StudentListView.as_view(), name='students'),
    path('students/search', views.student_search_form, name='student-search-form'),
    path('student/<int:pk>', views.StudentDetailView.as_view(), name='student-detail'),
]
