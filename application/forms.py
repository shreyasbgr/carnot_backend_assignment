from django import forms


class StudentSearchForm(forms.Form):
    student_id = forms.IntegerField(help_text='Enter the id of the student', required=True)
    student_name = forms.CharField(help_text='Enter the full name of the student', required=False)
