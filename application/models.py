from django.db import models


# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=20, help_text='The first name of the student')
    last_name = models.CharField(max_length=20, help_text='The last name of the student', blank=True, null=True)
    email = models.EmailField(max_length=30, help_text='The email id of the student')

    GENDER_OPTIONS = (
        ('m', 'Male'),
        ('f', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_OPTIONS, blank=True, null=True,
                              help_text='The gender of the student')
    school = models.ForeignKey('School', on_delete=models.SET_NULL, null=True, blank=True)
    books = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True, blank=True)


class School(models.Model):
    region_id = models.IntegerField(max_length=3, help_text='The region id of the school')
    school = models.CharField(max_length=50, primary_key=True, help_text='The name of the school')
    email = models.CharField(max_length=30, help_text='The email id associated with the school')
    principal = models.CharField(max_length=40, help_text='The name of the principal of the school')
    phone = models.CharField(max_length=8, help_text='The phone number associated with the school')
    address2 = models.CharField(max_length=100, help_text='The 2nd address line of the school')


class Book(models.Model):
    title = models.CharField(max_length=50, primary_key=True, help_text='The title of the book')
    author_name = models.CharField(max_length=50, blank=True, null=True, help_text='The name of the author of the book')
    date_of_publication = models.DateField(null=True, blank=True, help_text='The date of publication of the book')
    number_of_pages = models.IntegerField(max_length=10, help_text='The number of pages in the book')
