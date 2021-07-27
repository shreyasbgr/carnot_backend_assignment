from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import Student


# Create your views here.
def hello_application(request):
    return HttpResponse('Hello from the application!')


class StudentListView(generic.ListView):
    model = Student


class StudentDetailView(generic.DetailView):
    model = Student
