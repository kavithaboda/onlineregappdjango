from django import forms
from adminapp.models import AdminnModel

class AdminForms(forms.ModelForm):

    # Coursename = forms.CharField(max_length=50)
    # Faculty = forms.CharField(max_length=100)
    # Date = forms.DateField(widget=forms.SelectDateWidget)
    # Time = forms.CharField()
    # Fee = forms.IntegerField()
    # Duration = forms.CharField(max_length=100)

    class Meta:
        model = AdminnModel
        fields = '__all__'