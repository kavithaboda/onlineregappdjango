from django import forms
from student.models import StudentModel
# import re
# from student.mixins import RegistrationMixin

class StudentForms(forms.ModelForm):
    # Password=forms.CharField(validators=[RegistrationMixin.check_Password])
    class Meta:
        model = StudentModel
        fields = '__all__'

