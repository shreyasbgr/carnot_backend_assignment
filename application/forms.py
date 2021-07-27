from django import forms


class StudentSearchForm(forms.Form):
    student_id = forms.IntegerField(help_text='Enter the id of the student', required=False, blank=True, null=True)
    student_name = forms.CharField(help_text='Enter the first name of the student', required=False, blank=True, null=True)
