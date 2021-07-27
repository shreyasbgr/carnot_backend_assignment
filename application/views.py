from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.shortcuts import get_object_or_404

from .models import Student, School, Book


# Create your views here.
def hello_application(request):
    return HttpResponse('Hello from the application!')


class StudentListView(generic.ListView):
    model = Student


class StudentDetailView(generic.DetailView):
    model = Student

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['school'] = School.objects.get(context['student'].school)
        context['book'] = Book.objects.get(context['student'].books)
        return context
