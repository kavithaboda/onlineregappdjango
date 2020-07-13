from django import forms
from student.models import StudentModel

class StudentForms(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = '__all__'

