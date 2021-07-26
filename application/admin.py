from django.contrib import admin
from .models import Student, School, Book


# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


admin.site.register(StudentAdmin, Student)
admin.site.register(School)
admin.site.register(Book)
