from django.db import models

from adminapp.models import AdminnModel


class StudentModel(models.Model):
    Name = models.CharField(max_length=50)
    Contactno = models.IntegerField(primary_key=True)
    Email = models.EmailField()
    Password = models.CharField(max_length=20)

class EnroleListModel(models.Model):
    Contactno = models.ForeignKey(StudentModel, on_delete=models.CASCADE)
    idno = models.ForeignKey(AdminnModel, on_delete=models.CASCADE)