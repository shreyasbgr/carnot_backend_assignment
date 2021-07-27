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


def student_detail_view(request, primary_key):
    student = get_object_or_404(Student, pk=primary_key)
    school = get_object_or_404(School, student.school)
    book = get_object_or_404(Book, student.books)
    return render(request, 'application/student_detail.html', context={'student': student, 'school': school,
                                                                       'book': book})



