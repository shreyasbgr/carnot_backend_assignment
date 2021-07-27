from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.shortcuts import get_object_or_404

from .models import Student, School, Book
from .forms import StudentSearchForm


# Create your views here.
def hello_application(request):
    return HttpResponse('Hello from the application!')


class StudentListView(generic.ListView):
    model = Student


class StudentDetailView(generic.DetailView):
    model = Student

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['school'] = School.objects.get(school=context['student'].school)

        except School.DoesNotExist:
            pass

        try:
            context['book'] = Book.objects.get(title=context['student'].books)

        except Book.DoesNotExist:
            pass
        return context


def student_search_form(request):
    if request.method == "GET":
        form = StudentSearchForm()
        context = {'form': form}
        request_params_included = False
        try:
            if 'student_id' in request.GET and request.GET['student_id']:
                student = Student.objects.get(id=request.GET['student_id'])
                context['student'] = student
                request_params_included = True

            elif 'student_name' in request.GET and request.GET['student_name']:
                student = Student.objects.get(first_name=request.GET['student_name'])
                context['student'] = student
                request_params_included = True

        except Student.DoesNotExist:
            pass

        try:
            if request_params_included:
                school = School.objects.get(school=context['student'].school)
                context['school'] = school

        except School.DoesNotExist:
            pass

        try:
            if request_params_included:
                book = Book.objects.get(title=context['student'].books)
                context['book'] = book

        except Book.DoesNotExist:
            pass

    return render(request, 'application/student_search_form.html', context)
